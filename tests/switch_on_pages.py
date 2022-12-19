from modal.application_manager import ApplicationManager
from modal.data.user import Margo


def test_payment_page(app: ApplicationManager):
    app.payment.open_main()
    app.payment.search_click()
    app.payment.search(Margo.things)
    app.payment.choose_things()
    app.payment.add()
    app.payment.go_checkout()
    app.payment.fill_email(Margo.email)
    app.payment.fill_name(Margo.name)
    app.payment.fill_last_name(Margo.last_name)
    app.payment.fill_country(Margo.country)
    app.payment.fill_city(Margo.city)
    app.payment.fill_phone(Margo.phone)
    app.payment.switch()
    app.payment.should_have_text(Margo.text)


def test_faqs(app: ApplicationManager):
    app.faqs.open_main()
    app.faqs.scroll()
    app.faqs.switch()
    app.faqs.should_have_text()


def test_privacy_policy(app: ApplicationManager):
    app.privacy_policy.open_main()
    app.privacy_policy.scroll()
    app.privacy_policy.switch()
    app.privacy_policy.should_have_text()


def test_privacy_policy(app: ApplicationManager):
    app.privacy_policy.open_main()
    app.privacy_policy.scroll()
    app.privacy_policy.switch()
    app.privacy_policy.should_have_text()
