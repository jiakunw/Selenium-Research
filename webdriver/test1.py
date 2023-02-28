from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

length = len(sys.argv)

if(length < 3):
    username = "Username"
    password = "Password"
else:
    username = sys.argv[1]
    password = sys.argv[2]

driver = webdriver.Chrome()
driver.get("https://www.getzuz.com/login")

print("Current URL is " + driver.current_url)
sleep(1)
print("Web page title is " + driver.title)


about = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/header/div/div/div[2]/div/a[1]')

if about:
    print(about.text)
else:
    print("Couldn't find about")

about.click()

sleep(3)

login = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/header/div/div/div[2]/div/a[4]')
login.click()

sleep(3)

username_field = driver.find_element(By.XPATH, '//*[@id="username"]')
password_field = driver.find_element(By.XPATH, '//*[@id="password"]')

username_field.send_keys(username)
password_field.send_keys(password)
sleep(2)

login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/main/div/form/button')
login_button.click()
sleep(3)

marketplace = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/header/div/div/div[2]/div/a[2]')
marketplace.click()

sleep(3)
driver.close()