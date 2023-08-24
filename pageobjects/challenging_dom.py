from pip._internal.models import index
from selenium.webdriver.common.by import By
from toolium.pageelements import Button
from toolium.pageobjects.page_object import PageObject


class ChallengingDomPageObject(PageObject):

    def init_page_elements(self):
        self.btn = Button(By.XPATH, '//a[@class="button"]')
        self.btn_alert = Button(By.XPATH, '//a[@class="button alert"]')
        self.btn_success = Button(By.XPATH, '//a[@class="button success"]')
        self.btn_edit = Button(By.XPATH, '//tr[td[text()="Phaedrum0"]]//a[@href="#edit"]')
        self.btn_delete = Button(By.XPATH, '//tr[td[text()="Phaedrum0"]]//a[@href="#delete"]')
    
    def get_element(self, element_name):
        switcher = {

                "btn" : self.btn,
                "btn_alert" : self.btn_alert,
                "btn_success" : self.btn_success,
                "btn_alert" : self.btn_alert,
                "btn_edit" : self.btn_edit,
                "btn_delete" : self.btn_delete
         }

        el = switcher.get(element_name, None)

        if el is None:
            self.logger.error('Element "{}" is undefined'.format(element_name))
        else:
            return el