import pytest

from Pages.RoshenCorporation import RoshenCorporation
from Utilities.readProperties import ReadDataConfiguraton
from Pages.AboutProducts.BoxedSweets import BoxedSweets


class Test_BoxedSweets:

    base_login_url = ReadDataConfiguraton.get_application_url()
    boxed_sweets_h1_xpath = "//h1[@class='fade-in-animation block-animated']"

    @pytest.mark.petiokasmetio
    def test_boxed_sweets_header1(self, setup):
        self.driver = setup
        self.driver.get(self.base_login_url)
        self.roshencorporation = RoshenCorporation(self.driver)
        self.roshencorporation.click_about_procucts()
        self.boxedsweets = BoxedSweets(self.driver)
        self.boxedsweets.click_slider_arrow()
        self.boxedsweets.click_boxed_sweets()
        #TO DO ASSERTION FOR H1 TEXT
        # self.texth1 = self.driver.find_element_by_xpath(self.boxed_sweets_h1_xpath).text
        # if 'Boxed sweets' in self.texth1:
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.close()
        #     assert False

