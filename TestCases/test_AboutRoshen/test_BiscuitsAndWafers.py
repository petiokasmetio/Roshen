import pytest
from Utilities.readProperties import ReadDataConfiguraton
from Pages.RoshenCorporation import RoshenCorporation
from Pages.AboutProducts.AboutRoshen import AboutRoshen

class Test_BiscuitsAndWafers:


    base_url = ReadDataConfiguraton.get_application_url()

    @pytest.mark.petiokasmetio
    def test_biscuits_and_wafers_h1(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.roshencorporation = RoshenCorporation(self.driver)
        self.roshencorporation.click_about_procucts()
        self.aboutroshen = AboutRoshen(self.driver)
        self.aboutroshen.click_slider_arrow()
        self.aboutroshen.click_biscuits_wafers()
        self.aboutroshen.h1_biscuits_text()
