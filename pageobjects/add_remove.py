from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class AddRemovePageObject(PageObject):

    def init_page_elements(self):
        self.element = Button(By.XPATH, "//*[@id='elements']")
        self.add_btn = Button(By.XPATH, "//button[@onclick='addElement()']")
        self.delete_btn = Button(By.XPATH, "//button[@class='added-manually']")

    def open(self):
        self.driver.get('{}/add_remove_elements/'.format(self.config.get('Test', 'url')))
        return self
    
    def add_elem(self):
        self.add_btn.wait_until_visible()
        self.add_btn.click()
        return self

    def delete_elem(self):
        self.delete_btn.wait_until_visible()
        self.delete_btn.click()
        return self