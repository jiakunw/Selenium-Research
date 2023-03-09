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
driver.get("https://zuzweb.com/login")

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

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(username)
password_field.send_keys(password)
sleep(2)

login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/main/div/form/button')
login_button.click()
sleep(3)

marketplace = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/header/div/div/div[2]/div/a[2]')
# marketplace.click()

sleep(3)

seth_bakery = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/main/div/div/div[2]/ul/div/div')
seth_bakery.click()
sleep(1)

spend_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[6]/button/span[1]')
spend_button.click()
sleep(3)

# receive_user_field = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/div[1]/div/div")
receive_user_field = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/div[1]/div')
# receive_user_field.send_keys(payee_username)

sleep(2)

amount_field = driver.find_element(By.ID, 'outlined-adornment-amount')
amount_field.send_keys('10')

sleep(1)
driver.close()