import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AboutRoshen:

    slider_arrow_xpath = "//div[@class='slider-arr-dwn js-arr-down-all']"
    boxed_sweets_link_xpath = "//a[@href='en/en/about-roshen/about-products/boxed-sweets']//div[@class='border-animate-content']"
    h1_categories_xpath = "//h1[@class='fade-in-animation block-animated']"
    boxed_sweets_downarrow_xpah = "//div[@class='slider-arr-dwn js-arr-down-all']"
    boxed_sweets_info_xpath = "//p[contains(text(),'They say that life is like a box of chocolates: yo')]"
    category_chocolates_xpath = "//a[@href='en/en/about-roshen/about-products/chocolates-and-chocolate-bars']//div[@class='border-animate-content']"
    category_caramels_and_candies_xpath = "//a[@href='en/en/about-roshen/about-products/caramel-and-candies']//div[@class='border-animate-content']"
    p_caramels_text_xpath = "//p[contains(text(),'ROSHEN Corporation is an absolute leader in carame')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def paragraph_candies_text(self):
        time.sleep(3)
        para_text = self.wait.until(EC.presence_of_element_located((By.XPATH, self.p_caramels_text_xpath)))
        if "ROSHEN Corporation is an absolute leader in caramel production in Ukraine. If we put it in numbers: around 40% of caramel products at the home market belong to ROSHEN factories in Kremenchuk and Vinnytsia." in para_text.text:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def paragraph_candies(self):
        self.driver.find_element("xpath", self.p_caramels_text_xpath)

    def click_caramels_and_candies(self):
        self.driver.find_element_by_xpath(self.category_caramels_and_candies_xpath).click()

    def click_chocolates_and_bars(self):
        self.driver.find_element_by_xpath(self.category_chocolates_xpath).click()

    def check_h1_exists(self):
        self.driver.find_element_by_xpath(self.h1_categories_xpath)

    def click_slider_arrow(self):
        self.driver.find_element_by_xpath(self.slider_arrow_xpath).click()

    def click_boxed_sweets(self):
        self.driver.find_element_by_xpath(self.boxed_sweets_link_xpath).click()

    def get_text_from_h1_boxedsweets(self):
        self.driver.find_element_by_xpath(self.boxed_sweets_h1_xpath)

    def click_sub_category_downarrow(self):
        self.driver.find_element_by_xpath(self.boxed_sweets_downarrow_xpah).click()

