import allure
from selene import command, have
from selene.support.shared import browser


class FAQS:
    def open_main(self):
        with allure.step('Open main'):
            browser.open('https://shop.spacex.com/')
        return self

    def scroll(self):
        browser.element('.Linklist__Item > a[href="/pages/faqs"]').perform(command.js.scroll_into_view)
        return self

    def switch(self):
        with allure.step('Open faqs'):
            browser.element('.Linklist__Item > a[href="/pages/faqs"]').click()
        return self


    def should_have_text(self):
        browser.element('.u-h1').should(have.text('FAQS'))
        return self
