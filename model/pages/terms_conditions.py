import allure
from selene import command, have
from selene.support.shared import browser


class TermsConditionsPage:
    def switch(self):
        with allure.step('Open terms conditions page'):
            browser.element('.Linklist__Item > a[href="/policies/terms-of-service"]').perform(
                command.js.scroll_into_view)
            browser.element('.Linklist__Item > a[href="/policies/terms-of-service"]').click()
        return self

    def should_have(self, expected_text: str):
        browser.element('.shopify-policy__title').should(have.text(expected_text))
        return self
