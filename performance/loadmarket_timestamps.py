from locust import FastHttpUser, TaskSet, task, events
import logging
from market_load_urls import *
import json, time
from credentials import *
import bs4

# This file loads the market place for a user that's not logged in. 
# Uses timestamps for estimating the performance of loading the marketplace frontend. 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('LoadMarketTimestamps.csv')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s,%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)

logger.addHandler(handler)


class LoadMarketPlaceNoLogin(TaskSet):

    @task
    def load_market(self):
        start_time = time.time() 
        
        # get HTML page -> load .js and .css files from it
        res = self.client.get("/") # returns the HTML page
        soup = bs4.BeautifulSoup(res.text, features='html.parser')
        scripts = soup.find_all('script')
        srcs = [link['src'] for link in scripts if 'src' in link.attrs]
        js_link = srcs[0]
        links = soup.find_all('link')
        l_srcs = [link['href'] for link in links if 'stylesheet' in link['rel']]
        stylesheet = l_srcs[0]

        res = self.client.get(js_link)
        res = self.client.get(stylesheet)
        # self.client.get("/images/zuz_logotype_white.svg") 
        # self.client.get("/favicon.ico") 

        # load logo images from issuers
        res = self.client.get("/api/v2/user/list/issuers") # go through issuers for logos
        issuers_info = json.loads(res.text)["result"]
        for i in range(len(issuers_info)):
            logo = issuers_info[i]["logo"]
            self.client.get("/" + logo)

        end_time = time.time()
        logger.info('%s', end_time - start_time) # TODO attach user number
        self.on_stop()
        
    def on_stop(self): 
        return super().on_stop()

class Users(FastHttpUser):

    # both different types of users are spawned if # users > 1
    tasks = [LoadMarketPlaceNoLogin]
    host = "https://boltplace.com"

    def on_stop(self):
        handler.close()
        return super().on_stop()



