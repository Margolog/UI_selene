from this import s

from selene import command
from selene.support.shared import browser


class FAQS:
    def open_page(self):
        browser.open('https://shop.spacex.com/')
        return self

    def scroll_to_bottom(self):
        s('.ProductItem__Wrapper > a[href^="/pages/faqs"]').perform(command.js.scroll_into_view)
        return self

    def open_faqs(self):
        browser.element('.ProductItem__Wrapper > a[href^="/pages/faqs"]')
        return self
