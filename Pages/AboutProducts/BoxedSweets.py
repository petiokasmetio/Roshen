from selenium.webdriver import ActionChains


class BoxedSweets:

    slider_arrow_xpath = "//div[@class='slider-arr-dwn js-arr-down-all']"
    boxed_sweets_link_xpath = "//a[@href='en/en/about-roshen/about-products/boxed-sweets']//div[@class='border-animate-content']"
    boxed_sweets_h1_xpath = "//h1[@class='fade-in-animation block-animated']"

    def __init__(self, driver):
        self.driver = driver

    def click_slider_arrow(self):
        self.driver.find_element_by_xpath(self.slider_arrow_xpath).click()

    def click_boxed_sweets(self):
        self.driver.find_element_by_xpath(self.boxed_sweets_link_xpath).click()

    def get_text_from_h1_boxedsweets(self):
        self.driver.find_element_by_xpath(self.boxed_sweets_h1_xpath)
