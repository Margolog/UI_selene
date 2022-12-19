from selene.support.shared import browser


class Main:
    def __int__(self):
        super.__init__()
    def open(self):
        browser.open('https://shop.spacex.com/')

    def search_click(self):
        browser.element('[data-action="toggle-search"]').click()

