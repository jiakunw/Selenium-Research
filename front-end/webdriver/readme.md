# Installation
To install the webdriver for Python you can use Pip or download it manually
    Pip

        pip install selenium
    Download
        Downlaod the PyPI source archive from https://pypi.org/project/selenium/#files and then run
        
        python setup.py install
    
For other languages look at https://www.selenium.dev/documentation/webdriver/getting_started/install_library/

# Creating a Test
Make a python file and import the webdriver with 
    
    from selenium import webdriver

You can use different browsers such as Chrome, Firefox, Edge, etc. If you want to use Chrome then you will want to do

    driver = webdriver.Chrome()
Note: You must have the browswer installed otherwise the webdriver will return an error.

To find elements on a webpage look at https://www.geeksforgeeks.org/python-selenium-find-button-by-text/

For examples of tests look at
https://www.browserstack.com/guide/login-automation-using-selenium-webdriver
https://selenium-python.readthedocs.io/getting-started.html

# test1.py
The python program takes in 3 arguments login_username, password, and payee_username
-login_username is the username that will be used to login into the ZUZ website
-password is the password associated with the login_username account
-payee_username is the username of the account that you want to test sending money to

