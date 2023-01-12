import allure
from selene.support.shared import browser


class MainPage:
    def open(self):
        with allure.step('Open main'):
            browser.open('https://shop.spacex.com/')
        return self