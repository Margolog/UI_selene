from modal.apps import app
from modal.data.user import Margo


def test_xxx():
    (app.search_things.open_page('https://shop.spacex.com/')
     .search(Margo.things)
     .choose_things()
     .add_things()
     .go_checkout()
     .fill_email(Margo.email)
     .fill_name(Margo.name)
     .fill_last_name(Margo.last_name)
     .fill_country(Margo.country)
     .fill_city(Margo.city)
     .fill_phone(Margo.phone)
     .clik_continue()
     .should_have_text(Margo.text)
     )
