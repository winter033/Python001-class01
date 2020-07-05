import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im')
#    browser.find_element_by_xpath("//button[contains(@class,'login-button btn_hover_style_8')]").click()
#    browser.find_element_by_xpath("//input[@name='mobileOrEmail']").send_keys("123456")
#    browser.find_element_by_xpath("//input[@name='password']").send_keys("123456")
#    browser.find_element_by_class_name("submit").click()
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, 'login-button.btn_hover_style_8').click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//input[@name='mobileOrEmail']").send_keys("123456")
    browser.find_element(By.XPATH, "//input[@name='password']").send_keys("123456")
    browser.find_element(By.CLASS_NAME, "submit").click()

except Exception as e:
    print(e)