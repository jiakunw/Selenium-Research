from locust import HttpUser, TaskSet, between, task, events
from credentials import *
from transactioncreds import *
import json, time

# Two classes for two different users are defined: LoginUser and CreateAccountUser
# Both user classes have mint and spend transactions with other accounts

class LoginUser(TaskSet):
    wait_time = between(1, 5)
    username = "NOT_FOUND" # only used for error checking, unnecessary right now
    password = ""
    token = ""
    id = "" 
    logged_in = False
    role = ""

    # called first and only once
    def on_start(self):

        # getting username and password from credentials.py
        if len(USER_CREDENTIALS) > 0:
            self.username, self.password = USER_CREDENTIALS.pop()
        
        if "NOT_FOUND" in self.username:
            self.logged_in = False
            self.on_stop()
        
        # login
        res = self.client.post("/api/login", json={'username': self.username, 'password': self.password})

        if (res.status_code != 200):
            self.on_stop()

        # get token and other information for this logged in user
        self.token = json.loads(res._content)['token']
        self.id = json.loads(res._content)['id']
        self.role = json.loads(res._content)['roles']
        
        self.client.headers["authorization"] = "Bearer " + self.token
        self.logged_in = True

    @task
    def spend_transactions(self):
        # getting username and id from transactioncreds.py
        for tmp_user, _ in TRANSACTION_CREDS:
            if (tmp_user != self.username):
                self.single_spend(tmp_user)

    @task # for merchant only
    def mint(self):
        if "merchant" in self.role:
            specid = ""

            # find bolt that can be minted 
            mintable_bolt = False
            res = self.client.get("/api/user/my-bolts")
            stuff = json.loads(res._content)['bolts']
            for check_issuer in stuff:
                if self.username in check_issuer["bolt"]["issuerName"]:
                    specid = check_issuer["bolt"]["specID"]
                    mintable_bolt = True
                    break

            if (mintable_bolt):
                # mint 1 bolt of the found spec
                self.client.post("/api/bolt/mint", json={"specID": specid, "value": 1.00})



    def single_spend(self, tmp_user):

        other_user = tmp_user
        other_id = ""
        boltid = ""
        specid = ""
        other_username = ""

        # find bolt that can be transfered (want amount = 1.00)
        found = False
        res = self.client.get("/api/user/my-bolts")
        stuff = json.loads(res._content)['bolts']
        for bolt_info in stuff:
            if (bolt_info["amount"] > 1):
                boltid = bolt_info["_id"]
                specid = bolt_info["bolt"]["specID"]
                found = True
                break

        if found:

            url_get_id = "https://boltplace.com/api/user/search?query=" + other_user 
            customer_content = self.client.get(url_get_id)
            tmp_user_info = json.loads(customer_content._content)['users'][0]
            other_id = tmp_user_info["id"]
            other_username = tmp_user_info["username"]

            # make transaction
            data = {"amount": 1.00, "boltID": specid, "tip": 0, "userID": other_id}
            self.client.headers["referer"] = "https://boltplace.com/wallet"
            res = self.client.post("/api/v2/transaction", json=data)


    # called last and only once
    def on_stop(self):
        time.sleep(1000)
        return super().on_stop()



class CreateAccountUser(TaskSet):
    # wait_time = between(1, 5)
    username = ""
    password = "asdF" # only requirements: > 4 chars, one uppercase
    email = ""
    token = ""
    id = "" 
    role = ""
    spaddle_auth = ""

    # called first and only once
    def on_start(self):

        # create new account
        self.client.headers["referer"] = "https://boltplace.com/register"

        # get avaliable username
        avaliable_username = False
        cur_time = (str(time.time())).replace(".", "")
        url = ""
        for i in range(5): 
            url = "/api/user/check-username/help" + cur_time
            res = self.client.get(url)

            if ((json.loads(res._content)['username'])['available']):
                tmp_username = "help" + cur_time
                avaliable_username = True
                break

        if avaliable_username:

            # log in as spaddle and start logging emails
            res = self.client.post("/api/login", json={'username': "spaddle", 'password': "asdF"})
            if (res.status_code != 200):
                self.on_stop()
            self.token = json.loads(res._content)['token']
            self.id = json.loads(res._content)['id']
            self.role = json.loads(res._content)['roles']
            self.client.headers["authorization"] = "Bearer " + self.token
            self.spaddle_auth = "Bearer " + self.token
            res = self.client.post("/api/general/setemailtest", json={"save": 1}) # logging emails api
                
            # create account
            tmp_role = "customer"
            # tmp_email = "testingperformance422@gmail.com"
            # tmp_email = "testingperformance422+" + cur_time + "@gmail.com"
            tmp_email = "sarapate+" + cur_time + "@andrew.cmu.edu"
            res = self.client.post("/api/user", json={"Content-Type":"application/json;charset=UTF-8", "email": tmp_email, "firstName": tmp_username, "lastName": tmp_username, "password": "asdF", "phone": "9086729322", "role": "customer", 'username': tmp_username})
            if (res.status_code != 200):
                self.on_stop()

            # getting username and password from credentials.py
            TRANSACTION_CREDS.append((tmp_username, "asdF"))

            # email verification
            emaildata = self.client.get("/api/general/getemaildata")
            if "success" not in (json.loads(emaildata._content)["status"]):
                self.on_stop()
            
            # getting link to verify email
            verification_link = ""
            info = (json.loads(emaildata._content)["data"])["info"]
            for i in range((json.loads(emaildata._content)["data"])["last"]):
                # print(info[i]["Destination"]["ToAddresses"])
                if tmp_email in info[i]["Destination"]["ToAddresses"][0]:
                    verification_link = json.loads(info[i]["TemplateData"])["verificationLink"]
                    break

            # using verification link
            self.client.headers.pop("referer") # this headers shouldn't be in register get request
            self.client.headers.pop("authorization") # this headers shouldn't be in register get request

            res = self.client.get(verification_link) # TODO: 404 not found for url
            # print(verification_link)
            # print(res.status_code)
            # https://boltplace.com/api/user/verify-email/482?token=651464712198665bbc749b333056628c
            # https://boltplace.com/api/user/verify-email/482?token=651464712198665bbc749b333056628c
            # print("content")
            # print(res._content)
            # print('headers')
            # print(res.headers)
            # print()
            if (res.status_code != 200 or res.status_code != 312):
                # turn off logging emails
                self.client.headers["authorization"] = self.spaddle_auth
                res = self.client.post("/api/general/setemailtest", json={"save": 0})

                self.on_stop()

            res = self.client.get("/email-verification?verified=true")


            # turn off logging emails
            self.client.headers["authorization"] = self.spaddle_auth
            res = self.client.post("/api/general/setemailtest", json={"save": 0})
            
            self.username = tmp_username
            self.password = "asdF"
            self.role = tmp_role
            self.email = tmp_email

            
            # login
            res = self.client.post("/api/login", json={'username': self.username, 'password': self.password})

            if (res.status_code != 200):
                self.on_stop()

            # getting token
            self.token = json.loads(res._content)['token']
            self.id = json.loads(res._content)['id']
            
            self.client.headers["authorization"] = "Bearer " + self.token
            self.logged_in = True

        else:
            # if no avaliable username
            self.on_stop()


    # tasks are called in random order  
    @task
    def test_connection(self):
        url = "/api/user" + str(self.id)
        res = self.client.get(url)
    @task
    def connect_to_my_bolts(self):
        res = self.client.get("/api/user/my-bolts")
    @task
    def connect_to_user_txns(self):
        res = self.client.get("/api/v2/transaction/user-txns")

    @task
    def spend_transactions(self):
        # getting username and id from transactioncreds.py
        for tmp_user, _ in TRANSACTION_CREDS:
            if (tmp_user != self.username):
                self.single_spend(tmp_user)

    @task # for merchant only
    def mint(self):
        if "merchant" in self.role:
            specid = ""

            # find bolt that can be minted 
            mintable_bolt = False
            res = self.client.get("/api/user/my-bolts")
            stuff = json.loads(res._content)['bolts']
            for check_issuer in stuff:
                if self.username in check_issuer["bolt"]["issuerName"]:
                    specid = check_issuer["bolt"]["specID"]
                    mintable_bolt = True
                    break
            
            # mint 1 bolt of the found spec
            if (mintable_bolt):
                self.client.post("/api/bolt/mint", json={"specID": specid, "value": 1.00})



    def single_spend(self, tmp_user):

        other_user = tmp_user
        other_id = ""
        boltid = ""
        specid = ""
        other_username = ""

        # find bolt that can be transfered (want amount = 1.00)
        found = False
        res = self.client.get("/api/user/my-bolts")
        stuff = json.loads(res._content)['bolts']
        for bolt_info in stuff:
            if (bolt_info["amount"] > 1):
                boltid = bolt_info["_id"]
                specid = bolt_info["bolt"]["specID"]
                found = True
                break

        if found:

            url_get_id = "https://boltplace.com/api/user/search?query=" + other_user 
            customer_content = self.client.get(url_get_id)
            tmp_user_info = json.loads(customer_content._content)['users'][0]
            other_id = tmp_user_info["id"]
            other_username = tmp_user_info["username"]

            # make transaction
            data = {"amount": 1.00, "boltID": specid, "tip": 0, "userID": other_id}
            self.client.headers["referer"] = "https://boltplace.com/wallet"
            res = self.client.post("/api/v2/transaction", json=data)


    # called last and only once
    def on_stop(self):
        time.sleep(1000)
        return super().on_stop()


class Users(HttpUser):

    # both different types of users are spawned if # users > 1
    tasks = [LoginUser, CreateAccountUser]
    host = "https://boltplace.com"