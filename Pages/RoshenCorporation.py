from selenium import webdriver
from selenium.webdriver import ActionChains


class RoshenCorporation:

    cookie_xpath = '//button[@id="accept"]'
    dropdown_about_roshen_xpath = '//a[@class="menu-head has-submenu"][normalize-space()="About ROSHEN"]'
    dropdown_option_about_products_xpath = '//ul[@class="sub-menu"]//a[normalize-space()="About Products"]'

    def __init__(self, driver):
        self.driver = driver

    def accept_cookie(self):
        self.driver.find_element_by_xpath(self.cookie_xpath).click()

    def click_about_procucts(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_xpath(self.dropdown_about_roshen_xpath)).move_to_element(
            self.driver.find_element_by_xpath(self.dropdown_option_about_products_xpath)).click().perform()

