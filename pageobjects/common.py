import time
import pageobjects
from pageobjects.add_remove import AddRemovePageObject
from pageobjects.challenging_dom import ChallengingDomPageObject
from pageobjects.login import LoginPageObject
from toolium.pageelements import *
from toolium.pageobjects.page_object import PageObject


class CommonPageObject(PageObject):
    
    def open(self, page_name: str):
        """ Open login url in browser

        :returns: this page object instance
        """

        switcher = {
            "login_page": self.config.get('LoginPage', 'url'),
            "add_remove_elements_page": self.config.get('AddRemovePage', 'url'),
            "challenging_dom": self.config.get('ChallengingDom', 'url')
        }
        url = switcher.get(page_name.strip().lower(), None)

        self.driver.get('{}'.format(url))
        self.logger.info("Openned the {} page".format(page_name))
        self.logger.info("Page title = {}".format(self.driver.title))
        return self.driver.title
    
    def get_page(self, page_name: str):

        """ Return Page Object

       :returns: this page object instance
       """

        switcher = {
            "login_page": LoginPageObject,
            "add_remove_elements_page": AddRemovePageObject,
            "challenging_dom": ChallengingDomPageObject 
        }
        page = switcher.get(page_name.strip().lower(), None)
        self.logger.info("title = {}".format(self.driver.title))
        return page
    
    def click_element(self, element_name: str, el: PageElement):
        self.logger.info("Attempting to click on the {}".format(element_name))
        self.utils.wait_until_element_clickable(el).click()        
        self.logger.info("clicked the {} element".format(element_name))
        time.sleep(3) #for demonstration purposes
        return self