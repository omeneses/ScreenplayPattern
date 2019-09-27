from selenium import webdriver
from selenium.webdriver.common.by import By

class Click():
    def click_on(self, driver, type_locator ,locator):
            if type_locator=='ID':
                driver.find_element(By.ID, locator).click()
            else:
                pass
           
       
