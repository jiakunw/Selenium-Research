from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

length = len(sys.argv)

if(length < 4):
    print("Please give all required arguments")
    quit()
else:
    username = sys.argv[1]
    password = sys.argv[2]
    payee_username = sys.argv[3]

driver = webdriver.Chrome()
driver.get("https://boltplace.com")

print("Current URL is " + driver.current_url)
print("Web page title is " + driver.title)

sleep(2)

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(username)
password_field.send_keys(password)
sleep(2)

login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/main/div/form/button')
login_button.click()
sleep(3)

seth_bakery = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div[2]/div/button')
seth_bakery.click()
sleep(1)



spend_button = driver.find_element(By.XPATH, '//button[normalize-space()="Spend"]')
spend_button.click()
sleep(3)

payee_field = driver.find_element(By.XPATH, "//input[normalize-space()='']")
payee_field.send_keys(payee_username)

sleep(2)
amount_field = driver.find_element(By.NAME, 'amount')
amount_field.send_keys('10')

sleep(1)

spend_button = driver.find_element(By.XPATH, '//button[normalize-space()="Submit"]')

driver.close()