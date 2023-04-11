from locust import HttpUser, TaskSet, task
import logging, sys
from credentials import *
from transactioncreds import *
import json, time

# TO DO:
# create account user
# add minting and selling transactions

class LoginUser(TaskSet):
    username = "NOT_FOUND"
    password = "NOT_FOUND"
    token = "NOT_FOUND"
    id = "NOT_FOUND" 
    logged_in = False
    role = "NOT_FOUND"

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

        self.token = json.loads(res._content)['token']
        self.id = json.loads(res._content)['id']
        self.role = json.loads(res._content)['roles']
        
        self.client.headers["authorization"] = "Bearer " + self.token
        self.logged_in = True

    # tasks are called in random order     
    @task
    def test_connection(self):
        self.client.get("/api/user/99")

    @task
    def connect_to_my_bolts(self):
        self.client.get("/api/user/my-bolts")

    @task
    def connect_to_user_txns(self):
        self.client.get("/api/v2/transaction/user-txns")

    @task
    def transactions(self):
        # getting username and id from transactioncreds.py
        for tmp_user, _ in TRANSACTION_CREDS:
            if (tmp_user != self.username):
                self.single_transaction(tmp_user)

    
    # @task
    # def tasks_for_merchant(self):
  

    def single_transaction(self, tmp_user):

        other_user = tmp_user
        other_id = ""
        boltid = "NOT_FOUND"
        specid = ""
        other_username = ""

        # find bolt that can be transfered (want amount = 1.00)
        res = self.client.get("/api/user/my-bolts")
        stuff = json.loads(res._content)['bolts']
        for bolt_info in stuff:
            if (bolt_info["amount"] > 1):
                boltid = bolt_info["_id"]
                specid = bolt_info["bolt"]["specID"]
                break

        if "NOT_FOUND" not in boltid:

            url_get_id = "https://boltplace.com/api/user/search?query=" + other_user 
            customer_content = self.client.get(url_get_id)
            tmp_user_info = json.loads(customer_content._content)['users'][0]
            other_id = tmp_user_info["id"]
            other_username = tmp_user_info["username"]

            # make transaction
            data = {"amount": 1.00, "boltID": specid, "tip": 0, "userID": other_id}
            self.client.headers["referer"] = "https://boltplace.com/wallet"
            res = self.client.post("/api/v2/transaction", json=data)
            
            # so far, all the failures with transactions have code 417 and BOLT4003
            if (res.status_code != 200):
                print("failure")
                stringtoprint = self.username + " to " + other_username
                print(stringtoprint)
                # print(res.status_code)
                # print(res.text)
                # print(res.headers)
                # print(res._content)
                print("\n")
            else:
                print("success")
                stringtoprint = self.username + " to " + other_username
                print(stringtoprint)
                print("\n")


    # called last and only once
    def on_stop(self):
        
        # do i even need to logout?
        if (self.logged_in):
            self.client.post("/api/logout", json={})

        return super().on_stop()



class CreateAccountUser(TaskSet):
    username = "NOT_FOUND"
    password = "Infotask" # only requirements: > 4 chars, one uppercase
    email = ""
    token = ""
    id = "" # not sure how useful this is

    # called first and only once
    def on_start(self):

        # create new account
        self.client.headers["referer"] = "https://boltplace.com/register"

        # get avaliable username
        url = ""
        for i in range(10): 
            url = "/api/user/check-username/infotest" + str(i)
            res = self.client.get(url)

            # res.text if username avaliable: {"status":"success","username":{"available":false}}
            if ((json.loads(res._content)['username'])['available']):
                self.username = "infotest" + str(i)
                break
        
        # create account

        # what do i do about privacy policy?
        # do i get authorizatino token from create account or do i need to login with new credentials?

        # url not right
        self.email = self.username + "@zuzlab.com"
        res = self.client.post("/api/user", json={'Content-Type': "application/json;charset=UTF-8", 'email': self.email, 'firstName':"Dummy", 'lastName': "Dummy", 'password': self.password, 'role': "customer", 'username': self.username})
        
        # right now: only recieving this
        # POST /api/user: HTTPError('417 Client Error: Expectation Failed for url: /api/user')

        if (res.status_code != "200") :
            self.on_stop()


    # tasks are called in random order  
    @task
    def test_connection(self):
        url = "/api/user/" + id
        res = self.client.get(url)
    @task
    def connect_to_my_bolts(self):
        res = self.client.get("/api/user/my-bolts")
    @task
    def connect_to_user_txns(self):
        res = self.client.get("/api/v2/transaction/user-txns")

     # called last and only once
    def on_stop(self):

        # logout of new account
        if (self.logged_in):
            self.client.post("/api/logout", json={})

        return super().on_stop()




class Users(HttpUser):

    # both different types of users are spawned if # users > 1
    tasks = [LoginUser]
    host = "https://boltplace.com"
