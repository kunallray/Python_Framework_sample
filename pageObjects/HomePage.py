import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self,driver):
        self.driver=driver


    shop=(By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        return driver.find_element(*HomePage.shop)


