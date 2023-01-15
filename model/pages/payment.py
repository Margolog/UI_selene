import allure
from selene import have
from selene.support.shared import browser



class PaymentPage:

    def search_and_choose_things(self, things):
        with allure.step('Choose various'):
            browser.element('[data-action="toggle-search"]').click()
            browser.element('#search-input').type(things)
            browser.element('.ProductItem__Wrapper > a[href^="/products/spacex-back-pack"]').click()
        return self


    def add_goods(self):
        with allure.step('Add goods'):
            browser.element('[data-hcid="pdp-ac"]').click()
        return self

    def go_checkout(self):
        browser.element('[type="submit"]').click()
        return self

    def fill_form(self, email, name, last_name, country, code, city, phone):
        with allure.step('Fill form'):
            browser.element('[name="checkout[email]"]').type(email)
            browser.element('.field__input--select').click()
            browser.element('[data-code="TR"]').click()
            browser.element('#checkout_shipping_address_first_name').type(name)
            browser.element('#checkout_shipping_address_last_name').type(last_name)
            browser.element('#checkout_shipping_address_address1').type(country)
            browser.element('#checkout_shipping_address_zip').type(code)
            browser.element('#checkout_shipping_address_city').type(city)
            browser.element('#checkout_shipping_address_phone').type(phone)
        return self

    def go_next_page(self):
        with allure.step('Switch on payment'):
            browser.element('#continue_button').click()
        return self

    def should_have(self, expected_text: str):
        browser.config.timeout = 30
        browser.element('.breadcrumb__item.breadcrumb__item--blank').should(have.text(expected_text))
        return self
