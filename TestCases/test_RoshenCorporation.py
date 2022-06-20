import pytest
import unittest
import HtmlTestRunner
from selenium import webdriver
from Pages.RoshenCorporation import RoshenCorporation
from Utilities.readProperties import ReadDataConfiguraton


class Test_RoshenCorporation:

    base_login_url = ReadDataConfiguraton.get_application_url()

    def test_accept_cookit(self, setup):
        self.driver = setup
        self.driver.get(self.base_login_url)
        self.roshencorporation = RoshenCorporation(self.driver)
        self.roshencorporation.accept_cookie()
        self.driver.close()

    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_login_url)
        actual_title = self.driver.title
        if actual_title == 'ROSHEN Corporation':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:\\Users\\Elitebook\\PycharmProjects\\pythonProject\\Roshen\\Screenshots\\test_homepage_title.png")
            self.driver.close()
            assert False

    def test_about_products_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_login_url)
        self.roshencorporation = RoshenCorporation(self.driver)
        self.roshencorporation.click_about_procucts()
        actual_title = self.driver.title
        if actual_title == 'About products':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:\\Users\\Elitebook\\PycharmProjects\\pythonProject\\Roshen\\Screenshots\\test_About products_title.png")
            self.driver.close()
            assert False





