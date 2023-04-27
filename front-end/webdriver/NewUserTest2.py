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

parser = argparse.ArgumentParser(description='Login Test')

parser.add_argument('-u', '--username', default=None, help='Username of account')
parser.add_argument('-p', '--password', default=None, help='Password of account')
parser.add_argument('-w', '--website', default='https://boltplace.com', help='URL of Website')

args = parser.parse_args()
    
if(args.username == None):
    print("No username given")
    quit()
if(args.password == None):
    print("No password given")
    quit()


username = args.username
password = args.password
    
driver = webdriver.Chrome()
driver.get(args.website)

sleep(2)

try:
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
except:
    print("Could not find username or password field")
    driver.close()
    quit()

username_field.send_keys(username)
password_field.send_keys(password)
sleep(2)

try:
    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/main/div/form/button')
except:
    print("Could not find login button")
    driver.close()
    quit()

login_button.click()
sleep(2)

driver.close()