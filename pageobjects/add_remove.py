from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class AddRemovePageObject(PageObject):

    add_btn = None
    delete_btn = None

    def init_page_elements(self):
        self.add_btn = Button(By.XPATH, "//button[@onclick='addElement()']", wait=True)
        self.delete_btn = Button(By.XPATH, "//button[@class='added-manually']", wait=True)

    def get_element(self, element_name):
        switcher = {

                "add_btn" : self.add_btn,
                "delete_btn" : self.delete_btn
         }

        el = switcher.get(element_name, None)

        if el is None:
            self.logger.error('Element "{}" is undefined'.format(element_name))
        else:
            return el

    # def open(self, element_name: str, el: PageElement):
    #     self.driver.get('{}/add_remove_elements/'.format(self.config.get('Test', 'url')))
    #     return self
    
    # def add_elem(self, element_name: str, el: PageElement):
    #     self.add_btn.wait_until_visible(el)
    #     self.add_btn.click()
    #     return self

    # def delete_elem(self, element_name: str, el: PageElement):
    #     self.delete_btn.wait_until_visible(el)
    #     self.delete_btn.click()
    #     return self