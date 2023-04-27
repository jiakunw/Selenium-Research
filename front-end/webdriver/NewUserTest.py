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

parser = argparse.ArgumentParser(description='New User Test')

parser.add_argument('-u', '--username', default=None, help='Username of new account')
parser.add_argument('-p', '--password', default=None, help='Password of new account')
parser.add_argument('-e', '--email', default=None, help='Email of new account')
parser.add_argument('-f', '--firstname', default=None, help='First name of new account')
parser.add_argument('-l', '--lastname', default=None, help='Last name of new account')
parser.add_argument('-n', '--number', default=None, help='Phone number of new account')
parser.add_argument('-w', '--website', default='https://boltplace.com', help='URL of Website')

args = parser.parse_args()

if(args.username == None):
    print("No username given")
    quit()
if(args.password == None):
    print("No password given")
    quit()
if(args.email == None):
    print("No email given")
    quit()
if(args.firstname == None):
    print("No first name given")
    quit()


email = args.email
username = args.username
password = args.password
firstName = args.firstname
lastName = args.lastname
phoneNumber = args.number
    
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
    email_field = driver.find_element(By.ID, "email")
except:
    terminate("Could not find email field")

email_field.send_keys(email)

try:
    username_field = driver.find_element(By.ID, "username")
except:
    terminate("Could not find username field")

try:
    password_field = driver.find_element(By.ID, "password")
except:
    terminate("Could not find password field")

try:
    confirm_password_field = driver.find_element(By.ID, "passwordCopy")
except:
    terminate("Could not find confirm password field")

username_field.send_keys(username)
password_field.send_keys(password)
confirm_password_field.send_keys(password)
sleep(2)

try:
    firstName_field = driver.find_element(By.ID, "firstname")
except:
    terminate("Could not find first name field")

firstName_field.send_keys(firstName)

try:
    lastName_field = driver.find_element(By.ID, "lastname")
except:
    terminate("Could not find last name field")

lastName_field.send_keys(lastName)

try:
    phoneNumber_field = driver.find_element(By.ID, "phone")
except:
    terminate("Could not find phone number field")

phoneNumber_field.send_keys(phoneNumber)

sleep(3)

try:
    sign_up_button = driver.find_element(By.XPATH, '//button[normalize-space()="Sign Up"]')
except:
    terminate("Could not find sign up button")

# sign_up_button.click()

driver.close()