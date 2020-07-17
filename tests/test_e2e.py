from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
from utilities.BaseClass import BaseClass



class TestOne(BaseClass):
    def test_e2e(self):

        self.driver.find_element_by_css_selector("a[href*='shop']").click()

        # check for all the products
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        # check for the title and select desired one
        # //div[@class='card h-100']/div/h4/a
        # to reach add to cart button /div[@class='card h-100']/div[2]/button
        for product in products:
            print(product.find_element_by_xpath("div/h4/a").text)
            product_name = product.find_element_by_xpath("div/h4/a").text
            # add item into cart
            if product_name == "Blackberry":
                product.find_element_by_xpath("div[2]/button").click()

        # click on checkout button

        self.driver.find_element_by_css_selector("a.btn-primary").click()
        self.driver.find_element_by_css_selector("button.btn-success").click()
        self.driver.find_element_by_id("country").send_keys("ind")

        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_elements_by_xpath("//div[@class='checkbox-primary']")
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        # driver.find_element_by_id("checkbox2")
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        alert = self.driver.find_element_by_css_selector("div.alert-success").text
        print(self.driver.find_element_by_css_selector("div.alert-success").text)
        assert "Success! Thank you!" in alert

        self.driver.get_screenshot_as_file("screen.png")








