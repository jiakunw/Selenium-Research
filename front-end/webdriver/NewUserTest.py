from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

length = len(sys.argv)

if(length < 7):
    print("Please give all required arguments")
    quit()
else:
    email = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    firstName = sys.argv[4]
    lastName = sys.argv[5]
    phoneNumber = sys.argv[6]
    
driver = webdriver.Chrome()
driver.get("https://boltplace.com")

sleep(1)

try:
    create_account_button = driver.find_element(By.PARTIAL_LINK_TEXT, "New to ZUZ?")
except:
    print("Could not find create account button")
    driver.close()
    quit()

create_account_button.click()
sleep(2)

try:
    email_field = driver.find_element(By.ID, "email")
except:
    print("Could not find email field")
    driver.close()
    quit()

email_field.send_keys(email)

try:
    username_field = driver.find_element(By.ID, "username")
except:
    print("Could not find username field")
    driver.close()
    quit()

try:
    password_field = driver.find_element(By.ID, "password")
except:
    print("Could not find password field")
    driver.close()
    quit()

try:
    confirm_password_field = driver.find_element(By.ID, "passwordCopy")
except:
    print("Could not find confirm password field")
    driver.close()
    quit()

username_field.send_keys(username)
password_field.send_keys(password)
confirm_password_field.send_keys(password)
sleep(2)

try:
    firstName_field = driver.find_element(By.ID, "firstname")
except:
    print("Could not find first name field")
    driver.close()
    quit()

firstName_field.send_keys(firstName)

try:
    lastName_field = driver.find_element(By.ID, "lastname")
except:
    print("Could not find last name field")
    driver.close()
    quit()

lastName_field.send_keys(lastName)

try:
    phoneNumber_field = driver.find_element(By.ID, "phone")
except:
    print("Could not find phone number field")
    driver.close()
    quit()

phoneNumber_field.send_keys(phoneNumber)

sleep(3)

try:
    sign_up_button = driver.find_element(By.XPATH, '//button[normalize-space()="Sign Up"]')
except:
    print("Could not find sign up button")
    driver.close()
    quit()

# sign_up_button.click()

driver.close()