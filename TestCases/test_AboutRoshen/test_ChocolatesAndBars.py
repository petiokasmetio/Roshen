from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from Pages.RoshenCorporation import RoshenCorporation
from Utilities.readProperties import ReadDataConfiguraton
from Pages.AboutProducts.AboutRoshen import AboutRoshen


class Test_ChocolatesAndBars:


    base_login_url = ReadDataConfiguraton.get_application_url()
    chocolates_info_xpath = "//p[contains(text(),'ROSHEN chocolate is a combination of excellent rec')]"

    def test_chocolates_and_bars_h1(self, setup):
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.base_login_url)
        self.roshencorporation = RoshenCorporation(self.driver)
        self.roshencorporation.click_about_procucts()
        self.chocolates = AboutRoshen(self.driver)
        self.chocolates.click_slider_arrow()
        self.chocolates.click_chocolates_and_bars()
        try:
            self.chocolates.check_h1_exists()
        except NoSuchElementException:
            return False
        self.driver.close()
        return True


    def test_chocolates_info(self, setup):
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.base_login_url)
        self.roshencorporation = RoshenCorporation(self.driver)
        self.roshencorporation.accept_cookie()
        self.roshencorporation.click_about_procucts()
        self.chocolates = AboutRoshen(self.driver)
        self.chocolates.click_slider_arrow()
        self.chocolates.click_chocolates_and_bars()
        self.chocolates.click_sub_category_downarrow()
        chocolates_text = self.wait.until(EC.presence_of_element_located((By.XPATH, self.chocolates_info_xpath)))
        if "ROSHEN chocolate is a combination of excellent recipes and mastery of confectioners, which ensures a high quality product that brings true satisfaction. And that is what we all expect from the chocolate." in chocolates_text.text:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False