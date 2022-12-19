from modal.apps import app
from modal.data.user import User1


def test_xxx():
       (app.search_things.open_page('https://shop.spacex.com/')
        .search()
        .choose(User1.things)
        .choose_things()
        .add_things()
        .go_checkout()
        .fill_email(User1.email)
        .fill_name(User1.name)
        .fill_last_name(User1.last_name)
        .fill_country(User1.country)
        .fill_city(User1.city)
        .fill_phone(User1.phone)
        .clik_continue()
        .should_have_text(User1.text)
        )




