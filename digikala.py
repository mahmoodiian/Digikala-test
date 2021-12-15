from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

"""
Test Website Digikala
"""

# open browser (by chrome driver) and open digikala.com
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('https://www.digikala.com/')
sleep(2)

# find the login link and click on it
driver.find_element(By.XPATH, '/html/body/header/div/div/div[2]/div[1]/div/a').click()
sleep(2)

# find the username input and add data on it
username = input('Username: ')
driver.find_element(By.NAME, 'login[email_phone]').send_keys(username)
sleep(2)

# click on login button for continue
driver.find_element(By.XPATH ,'//*[@id="loginForm"]/button').click()
sleep(2)

# find the password input and add data on it
password = input('Password: ')
driver.find_element(By.NAME, 'login[password]').send_keys(password)
sleep(2)

# click on continue button for login
driver.find_element(By.XPATH, '//*[@id="authForm"]/button').click()
sleep(2)

# click on account button for check the username
driver.find_element(By.XPATH, '/html/body/header/div/div/div[2]/div[1]/div').click()
sleep(10)

# close the browser
driver.quit()
