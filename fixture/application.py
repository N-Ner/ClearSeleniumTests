__author__ = 'Nazar Ner'

from selenium import webdriver
from farm.farm import Farm


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = ".test-env.scalr.com/"
        self.farmsquery = ".test-env.scalr.com/#/farms?query="
        self.farm = Farm(self)
        self.driver.maximize_window()

    def destroy(self):
        self.driver.quit()

