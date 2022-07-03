import time
from telnetlib import EC
from TestCases import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from Pages.RoshenCorporation import RoshenCorporation
from Utilities.readProperties import ReadDataConfiguraton
from Pages.AboutProducts.AboutRoshen import AboutRoshen


class Test_BoxedSweets:


    base_login_url = ReadDataConfiguraton.get_application_url()
    boxed_sweets_info_xpath = "//p[contains(text(),'They say that life is like a box of chocolates: yo')]"

    def test_boxed_sweets_h1(self, setup):
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.base_login_url)
        self.roshencorporation = RoshenCorporation(self.driver)
        self.roshencorporation.accept_cookie()
        self.roshencorporation.click_about_procucts()
        self.boxedsweets = AboutRoshen(self.driver)
        self.boxedsweets.click_slider_arrow()
        self.boxedsweets.click_boxed_sweets()
        try:
            self.boxedsweets.check_h1_exists()
        except NoSuchElementException:
            return False
        self.driver.close()
        return True

    def test_boxed_sweets_info(self, setup):
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.base_login_url)
        self.roshencorporation = RoshenCorporation(self.driver)
        self.roshencorporation.click_about_procucts()
        self.boxedsweets = AboutRoshen(self.driver)
        self.boxedsweets.click_slider_arrow()
        self.boxedsweets.click_boxed_sweets()
        self.boxedsweets.click_sub_category_downarrow()
        boxedsweets_text = self.wait.until(EC.presence_of_element_located((By.XPATH, self.boxed_sweets_info_xpath)))
        if "They say that life is like a box of chocolates: you never know what is waiting for you inside. However, if the box is filled with chocolates by ROSHEN, then you can expect the best only." in boxedsweets_text.text:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False