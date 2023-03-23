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

create_account_button = driver.find_element(By.PARTIAL_LINK_TEXT, "New to ZUZ?")
create_account_button.click()
sleep(2)

email_field = driver.find_element(By.ID, "email")
email_field.send_keys(email)


username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
confirm_password_field = driver.find_element(By.ID, "passwordCopy")

username_field.send_keys(username)
password_field.send_keys(password)
confirm_password_field.send_keys(password)
sleep(2)

firstName_field = driver.find_element(By.ID, "firstname")
firstName_field.send_keys(firstName)


lastName_field = driver.find_element(By.ID, "lastname")
lastName_field.send_keys(lastName)

phoneNumber_field = driver.find_element(By.ID, "phone")
phoneNumber_field.send_keys(phoneNumber)

sleep(3)

sign_up_button = driver.find_element(By.XPATH, '//button[normalize-space()="Sign Up"]')
# sign_up_button.click()


driver.get("")

driver.close()