__author__ = 'Nazar Ner'

import time

class Farm:

    def __init__(self, app):
        self.app = app

    def launch(self, containerid, farmid):
        driver = self.app.driver
        driver.get(
            'http://' + containerid + self.app.farmsquery + farmid)
        time.sleep(3)
        driver.find_element_by_css_selector(
            ".x-grid-icon-launch").click()
        driver.find_element_by_css_selector(
            "a.x-btn-default-small-focus").click()
        time.sleep(3)

    def add_role(self):
        driver = self.app.driver
        driver.find_element_by_xpath(
            "//a[.='Add to farm']").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//a[.='Save farm']").click()
        time.sleep(1)
    
    def search_by_field(self, farmrole, scope):
        driver = self.app.driver
        driver.find_element_by_xpath(
            "//a[.='Add farm role']").click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "//*[.='Base']").click()
        driver.find_element_by_css_selector(
            "div.x-form-text-wrap-focus> input").clear()
        driver.find_element_by_css_selector(
            "div.x-form-text-wrap-focus> input").send_keys(farmrole)
        time.sleep(2)
        driver.find_element_by_css_selector(
            scope).click()
        time.sleep(2)
        
    def search_quick_start(self):
        driver = self.app.driver
        driver.find_element_by_xpath(
            "//a[.='Add farm role']").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[.='Quick start']").click()
        driver.find_element_by_xpath(
            "//*[.='MySQL']").click()
        time.sleep(3)       

    def search(self, containerid, farmid):
        driver = self.app.driver
        driver.get(
            'http://' + containerid + self.app.farmsquery + farmid)
        driver.find_element_by_css_selector(
            ".x-grid-icon-configure").click()
        time.sleep(3)

    def login_user_accaunt(self, login, passw):
        driver = self.app.driver
        driver.find_element_by_name(
            "scalrLogin").send_keys(login)
        driver.find_element_by_name(
            "scalrPass").send_keys(passw)
        time.sleep(1)
        driver.find_element_by_id(
            "button-1030").click()
        time.sleep(2)

    def go_to_container(self, containerid):
        driver = self.app.driver
        driver.get(
            'http://' + containerid + self.app.base_url)

