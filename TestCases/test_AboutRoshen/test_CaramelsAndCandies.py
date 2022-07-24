import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from Pages.RoshenCorporation import RoshenCorporation
from Utilities.readProperties import ReadDataConfiguraton
from Pages.AboutProducts.AboutRoshen import AboutRoshen


class Test_CaramelAndCandies:


    base_url = ReadDataConfiguraton.get_application_url()

    def test_caramels_and_candies_title(self, setup):
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.base_url)
        self.roshencorporation = RoshenCorporation(self.driver)
        self.roshencorporation.accept_cookie()
        self.roshencorporation.click_about_procucts()
        self.roshencorporation.about_products_downarrow()
        self.candies = AboutRoshen(self.driver)
        self.candies.click_caramels_and_candies()
        actual_title = self.driver.title
        if actual_title == 'Caramel and candies':
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_caramels_text(self, setup):
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.base_url)
        self.roshencorporation = RoshenCorporation(self.driver)
        self.roshencorporation.accept_cookie()
        self.roshencorporation.click_about_procucts()
        self.roshencorporation.about_products_downarrow()
        self.candies = AboutRoshen(self.driver)
        self.candies.click_caramels_and_candies()
        self.candies.click_sub_category_downarrow()
        time.sleep(5)
        try:
            self.candies.paragraph_candies()
        except NoSuchElementException:
            return False
        self.driver.close()
        return True

    @pytest.mark.petiokasmetio
    def test_caramels_p_text(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.roshencorporation = RoshenCorporation(self.driver)
        self.roshencorporation.accept_cookie()
        self.roshencorporation.click_about_procucts()
        self.roshencorporation.about_products_downarrow()
        self.candies = AboutRoshen(self.driver)
        self.candies.click_caramels_and_candies()
        self.candies.click_sub_category_downarrow()
        self.candies.paragraph_candies_text()

