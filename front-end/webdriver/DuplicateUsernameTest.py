from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import argparse

def terminate(str):
    if(str != None):
        print(str)
    driver.close()
    sleep(1)
    quit()

parser = argparse.ArgumentParser(description='Duplicate Username Test')

parser.add_argument('-u', '--username', default=None, help='Username that you to be tested if it is a duplicate')
parser.add_argument('-w', '--website', default='https://boltplace.com', help='URL of Website')

args = parser.parse_args()
    
if(args.username == None):
    print("No username given")
    quit()

username = args.username

driver = webdriver.Chrome()
driver.get(args.website)

sleep(1)

try:
    create_account_button = driver.find_element(By.PARTIAL_LINK_TEXT, "New to ZUZ?")
except:
    terminate("Could not find create account button")

create_account_button.click()
sleep(2)

try:
    username_field = driver.find_element(By.ID, "username")
except:
    terminate('Could not find username field')

username_field.send_keys(username)
sleep(2)

try:
    t = driver.find_element(By.XPATH, '//*[contains(text(), "Usernames must be unique, contain a mix of letters, numbers, or dashes, and be at least 4 characters long.")]')
    print("Passed")
except:
    print("Fail! Text did not appear")                    


terminate()