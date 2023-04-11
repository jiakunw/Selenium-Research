from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

length = len(sys.argv)

if(length < 2):
    print("Please give all required arguments")
    quit()
else:
    username = sys.argv[1]
    
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
    username_field = driver.find_element(By.ID, "username")
except:
    print("Could not find username field")
    driver.close()
    quit()

username_field.send_keys(username)
sleep(2)

try:
    t = driver.find_element(By.XPATH, '//*[contains(text(), "Usernames must be unique, contain a mix of letters, numbers, or dashes, and be at least 4 characters long.")]')
    print("Passed")
except:
    print("Fail! Text did not appear")                    

driver.close()