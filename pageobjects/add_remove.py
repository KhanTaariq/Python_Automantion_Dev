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
