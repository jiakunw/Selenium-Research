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

create_account_button = driver.find_element(By.PARTIAL_LINK_TEXT, "New to ZUZ?")
create_account_button.click()
sleep(2)


username_field = driver.find_element(By.ID, "username")
username_field.send_keys(username)
sleep(2)

#TODO: Assert that not valid username text appears

try:
    t = driver.find_element(By.XPATH, '//*[contains(text(), "Usernames must be unique, contain a mix of letters, numbers, or dashes, and be at least 4 characters long.")]')
    print("Passed")
except:
    print("Fail! Text did not appear")                    

driver.close()