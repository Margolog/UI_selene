import allure
from selene import command, have
from selene.support.shared import browser


class PrivacyPolicyPage:

    def switch(self):
        with allure.step('Open privacy policy'):
            browser.element('.Linklist__Item > a[href="/policies/privacy-policy"]').perform(command.js.scroll_into_view)
            browser.element('.Linklist__Item > a[href="/policies/privacy-policy"]').click()
        return self


    def should_have(self, expected_text: str):
        browser.element('.shopify-policy__title').should(have.text(expected_text))
        return self
