import allure
from selene import command, have
from selene.support.shared import browser


class FAQSPage:


    def switch(self):
        with allure.step('Open faqs'):
            browser.element('.Linklist__Item > a[href="/pages/faqs"]').perform(command.js.scroll_into_view)
            browser.element('.Linklist__Item > a[href="/pages/faqs"]').click()
        return self


    def should_have(self, expected_text: str):
        browser.element('.u-h1').should(have.text(expected_text))
        return self
