from selenium import webdriver
from selenium.webdriver.common.by import By

class Enter():
    def write_text(self, driver, type_locator ,locator, text):
            if type_locator=='ID':
                driver.find_element(By.ID, locator).send_keys(text)
            else:
                pass
           
       
