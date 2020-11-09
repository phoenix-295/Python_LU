import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Navigate to a site
driver = webdriver.Chrome()
driver.get("https://web.simple-mmo.com/")

#sleep For 3 sec
time.sleep(3)

# Login to Site using ID and Pass
email1 = driver.find_element_by_xpath('//*[@id="kt_login_form"]/div[1]/input')
email1.send_keys('nikhil295@gmail.com')
pass1 = driver.find_element_by_xpath('//*[@id="kt_login_form"]/div[2]/input')
pass1.send_keys('nikhil1905')
submit1 = driver.find_element_by_xpath('//*[@id="kt_login_signin_submit"]')
submit1.click()

#sleep for 3 sec
time.sleep(3)

#Navigate to 
driver.get("https://web.simple-mmo.com/travel")

#Infinite While to Travel
count = 0
while (count < 30):
    
    try :
        travel = driver.find_element_by_xpath('//*[@id="travel"]/div[5]/button[1]')
        travel.click()
        
        x = random.randint(5,7)
        time.sleep(x)
        
        #count = count + 1
    except :
        pass