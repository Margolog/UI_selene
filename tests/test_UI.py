from modal.application_manager import ApplicationManager
from modal.data.user import Margo
from modal.pages.payment_page import SearchThings


def test_items_not_shipped(app: ApplicationManager):
    app.main.open()
    app.main.search_click(Margo.things)
    pass


    # .search(Margo.things)
    # .choose_things()
    # .add_things()
    # .go_checkout()
    # .fill_email(Margo.email)
    # .fill_name(Margo.name)
    # .fill_last_name(Margo.last_name)
    # .fill_country(Margo.country)
    # .fill_city(Margo.city)
    # .fill_phone(Margo.phone)
    # .clik_continue()
    # .should_have_text(Margo.text)
    # )


def test_faqs():
    (app.faqs.open_page('https://shop.spacex.com/')
     .scroll_to_bottom()
     .open_faqs()

     )
