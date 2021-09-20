from selenium import webdriver
from time import sleep
from Pass import username,password

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(PATH)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_class_name("f0n8F")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        
InstaBot(username,password)