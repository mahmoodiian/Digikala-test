from selenium import webdriver
from time import sleep

"""
Test Website Digikala
"""

#
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('https://www.digikala.com/')
sleep(2)

# find the login link and click on it
driver.find_element_by_xpath('/html/body/header/div/div/div[2]/div[1]/div/a').click()
sleep(2)

# find the username input and add data on it
driver.find_element_by_name('login[email_phone]').send_keys('09194731285')
sleep(2)

# click on login button for continue
driver.find_element_by_xpath('//*[@id="loginForm"]/button').click()
sleep(2)

# find the password input and add data on it
driver.find_element_by_name('login[password]').send_keys('M_019980_m')
sleep(2)

# click on continue button for login
driver.find_element_by_xpath('//*[@id="authForm"]/button').click()
sleep(2)

# click on account button for check the username
driver.find_element_by_xpath('/html/body/header/div/div/div[2]/div[1]/div').click()
sleep(60)

# close browser
driver.quit()
