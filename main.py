from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

start = datetime.now()

ffb = FirefoxBinary(r'/home/bora/programs/firefox/firefox')



driver = webdriver.Firefox( firefox_binary=ffb) #executable_path=r'/home/bora/programs/firefox/firefox',
driver.get("http://192.168.0.1")
sleep(1)

def login():
    global driver
    try:
        adminnameinput = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'txtUsr')))
        #adminnameinput=driver.find_element(By.ID, 'txtUsr')
        adminnameinput.send_keys("admin")
        adminpassinput = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'txtPwd')))
        adminpassinput.send_keys("admin")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'btnLogin')) ).click()
    except:
        print('some error happen !!')

try:
    loginlink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'loginlink') ))
    #loginlink = driver.find_element(By.ID, 'loginlink')
    #if loginlink.text!='':
    loginlink.click()
    login()
except:
    print('login is alredy')



try:
    switch_key = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'h_connect_btn')))
    switch_key.click()
except:
    print('some error happen !!')
"""
while (driver.find_element(By.ID, 'result-overlay').get_attribute('style') == 'display: none;'):
    sleep(.1)
driver.refresh()
"""
try:
    
    temp = WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.ID, 'overlay-success')))
    driver.refresh()
except:
    print('some error happen !! refresh')


try:
    switch_key = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'h_connect_btn')))
    switch_key.click()
except:
    print('some error happen !!')


try:
    
    temp = WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.ID, 'overlay-success')))
    driver.close()
except:
    print('some error happen !! refresh')
t = (datetime.now() - start)
print('\n' + str(t.seconds) + '.' + str(t.microseconds) )