from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://account.proton.me/login")

input=driver.find_element_by_xpath('//*[@id="username"]')
input.send_keys('virat1a1') #enter proton mail mail id

input=driver.find_element_by_xpath('//*[@id="password"]')
input.send_keys('dhoni123') #enter proton mail valid password

input=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/button').click()

time.sleep(40)

input=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[2]/button').click()

input=driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/div/div[2]/div/div')
input.send_keys('Yashwanth6678@gmail.com') #add receiver mail id

input=driver.find_element_by_xpath('//*[@id="subject-composer-505"]')
input.send_keys('be good do good') #change text to your required line

input=driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/footer/div/div[1]/button/span').click()

time.sleep(10)

