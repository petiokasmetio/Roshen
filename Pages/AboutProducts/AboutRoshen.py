from selenium.webdriver import ActionChains
from TestCases import conftest

class AboutRoshen:

    slider_arrow_xpath = "//div[@class='slider-arr-dwn js-arr-down-all']"
    boxed_sweets_link_xpath = "//a[@href='en/en/about-roshen/about-products/boxed-sweets']//div[@class='border-animate-content']"
    h1_categories_xpath = "//h1[@class='fade-in-animation block-animated']"
    boxed_sweets_downarrow_xpah = "//div[@class='slider-arr-dwn js-arr-down-all']"
    boxed_sweets_info_xpath = "//p[contains(text(),'They say that life is like a box of chocolates: yo')]"
    category_chocolates_xpath = "//a[@href='en/en/about-roshen/about-products/chocolates-and-chocolate-bars']//div[@class='border-animate-content']"

    def __init__(self, driver):
        self.driver = driver

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

