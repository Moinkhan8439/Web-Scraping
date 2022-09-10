
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "C:\Program Files (x86)/chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get('https://www.dextools.io/app/')

close_model=driver.find_element(By.CLASS_NAME,"modal-content").find_element(By.CLASS_NAME,'close')
close_model.send_keys(Keys.RETURN)

search=driver.find_element(By.CLASS_NAME,'search-container').find_element(By.TAG_NAME,'input')
search.send_keys('WDOGE')
try:
    results=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'results-container')))
    # results=driver.find_element(By.CLASS_NAME,'results-container')
    print('after resuts')
    list_results=driver.find_element(By.CLASS_NAME,'results-container').find_element(By.TAG_NAME,'li').find_element(By.TAG_NAME,'a')
    print('after searching')
    list_results.click()
    print('after clicking')
    social_links_load=WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.CLASS_NAME,'social-links')))
    for i in range(3):
        print('social links loaded')
        telegram=driver.find_element(By.CLASS_NAME,'social-links').find_element(By.CLASS_NAME,'fa-telegram')
        print('telegram found')
        telegram.click()
except:
    print('social links not available')
    driver.quit()
    


