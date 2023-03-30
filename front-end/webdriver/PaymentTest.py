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
sleep(3)

try:
    seth_bakery = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div[2]/div/button')
except:
    print("Could not find seth bakery")
    driver.close()
    quit()

seth_bakery.click()
sleep(1)

try:
    spend_button = driver.find_element(By.XPATH, '//button[normalize-space()="Spend"]')
except:
    print("Could not find spend button")
    driver.close()
    quit()

spend_button.click()
sleep(3)

try:
    payee_field = driver.find_element(By.XPATH, "//input[normalize-space()='']")
except:
    print("Could not find payee field")
    driver.close()
    quit()

payee_field.send_keys(payee_username)

sleep(2)
try:
    amount_field = driver.find_element(By.NAME, 'amount')
except:
    print("Could not find amount field")
    driver.close()
    quit()

amount_field.send_keys('10')

sleep(1)

try:
    spend_button = driver.find_element(By.XPATH, '//button[normalize-space()="Submit"]')
except:
    print("Could not find spend button")
    driver.close()
    quit()

# driver.click()
sleep(1)

driver.close()