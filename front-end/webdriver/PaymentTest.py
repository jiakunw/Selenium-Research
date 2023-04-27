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

parser.add_argument('-u', '--username', default=None, help='Username of account to make payment')
parser.add_argument('-p', '--password', default=None, help='Password of account to make payment')
parser.add_argument('-u2', '--payee', default=None, help='Username of account to receive payment')
parser.add_argument('-w', '--website', default='https://boltplace.com', help='URL of Website')

args = parser.parse_args()
    
if(args.username == None):
    print("No username given")
    quit()
if(args.password == None):
    print("No password given")
    quit()
if(args.payee == None):
    print("No payee username given")
    quit()


username = args.username
password = args.password
payee_username = args.payee

driver = webdriver.Chrome()
driver.get(args.website)

sleep(2)

try:
    username_field = driver.find_element(By.ID, "username")
except:
    terminate("Could not find username field")

username_field.send_keys(username)

try:
    password_field = driver.find_element(By.ID, "password")
except:
    terminate("Could not find password field")
    

password_field.send_keys(password)
sleep(2)

try:
    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/main/div/form/button')
except:
    terminate("Could not find login button")

login_button.click()
sleep(3)

try:
    seth_bakery = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div[2]/div/button')
except:
    terminate("Could not find seth bakery")

seth_bakery.click()
sleep(1)

try:
    spend_button = driver.find_element(By.XPATH, '//button[normalize-space()="Spend"]')
except:
    terminate("Could not find spend button")

spend_button.click()
sleep(3)

try:
    payee_field = driver.find_element(By.XPATH, "//input[normalize-space()='']")
except:
    terminate("Could not find payee field")

payee_field.send_keys(payee_username)

sleep(2)
try:
    amount_field = driver.find_element(By.NAME, 'amount')
except:
    terminate("Could not find amount field")

amount_field.send_keys('10')

sleep(1)

try:
    spend_button = driver.find_element(By.XPATH, '//button[normalize-space()="Submit"]')
except:
    terminate("Could not find spend button")

# driver.click()
sleep(1)

terminate