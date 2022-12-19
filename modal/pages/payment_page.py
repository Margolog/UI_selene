from selene import have
from selene.support.shared import browser


class SearchThings:
    def open_page(self):
        browser.open('https://shop.spacex.com/')
        browser.element('[data-action="toggle-search"]').click()
        return self

    def search(self, things):
        browser.element('#search-input').type(things)
        return self

    def choose_things(self):
        browser.element('.ProductItem__Wrapper > a[href^="/products/spacex-back-pack"]').click()
        return self

    def add_things(self):
        browser.element('[data-hcid="pdp-ac"]').click()
        return self

    def go_checkout(self):
        browser.element('[type="submit"]').click()
        return self

    def fill_email(self, email):
        browser.element('[name="checkout[email]"]').type(email)
        return self

    def fill_name(self, name):
        browser.element('#checkout_shipping_address_first_name').type(name)
        return self

    def fill_last_name(self, last_name):
        browser.element('#checkout_shipping_address_first_name').type(last_name)
        return self


    def fill_country(self, country):
        browser.element('#checkout_shipping_address_address1').type(country)
        #[data-code="TR"]
        return self

    def fill_city(self, city):
        browser.element('#checkout_shipping_address_city').type(city)
        return self

    def fill_phone(self, phone):
        browser.element('#checkout_shipping_address_phone').type(phone)
        return self

    def clik_continue(self):
        browser.element('#continue_button').click()
        return self

    def should_have_text(self,text: str):
        browser.element('.notice__text').should(have.text(text))
        return self


