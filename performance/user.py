from locust import HttpUser, TaskSet, task
import logging, sys
from credentials import *
import json, time

# TO DO:
# create account user
# fill credentials.py with actual credentials



class LoginUser(TaskSet):
    username = "NOT_FOUND"
    password = "NOT_FOUND"
    token = ""
    id = "" # not sure how useful this is

    # called first and only once
    def on_start(self):

        # getting username and password from credentials.py
        if len(USER_CREDENTIALS) > 0:
            self.username, self.password = USER_CREDENTIALS.pop()
        
        # login
        res = self.client.post("/api/login", json={'username': self.username, 'password': self.password})
        self.token = json.loads(res._content)['token']
        self.id = json.loads(res._content)['id']
        self.client.headers["authorization"] = "Bearer " + self.token

    # tasks are called in random order     
    @task
    def test_connection(self):
        res = self.client.get("/api/user/99")

    @task
    def connect_to_my_bolts(self):
        res = self.client.get("/api/user/my-bolts")

    @task
    def connect_to_user_txns(self):
        res = self.client.get("/api/v2/transaction/user-txns")




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

        if (res.status_code != "202") :
            self.kill()


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

    # kill program if we get a bad request
    def kill(self):
        time.sleep(999999) # trying to find a better way to stop the current user




class Users(HttpUser):

    # both different types of users are spawned if # users > 1
    tasks = [LoginUser, CreateAccountUser]
    host = "https://boltplace.com"
