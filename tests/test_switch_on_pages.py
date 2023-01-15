import allure
from allure_commons.types import Severity
from model.application_manager import ApplicationManager
from model.data.title_text import *
from model.data.user import margo
from utils.allure_labels import allure_labels


@allure.severity(Severity.CRITICAL)
def test_payment_page(app: ApplicationManager):
    allure_labels(feature='Page payment',
                  title='Switch on Payment Page')

    app.main.open()
    (
        app.payment.search_and_choose_things(margo.things)
        .add_goods()
        .go_checkout()
        .fill_form(margo.email, margo.name, margo.last_name, margo.country, margo.code, margo.city,
                   margo.phone)
        .go_next_page()
    )

    app.payment.should_have(payment.expected_text)


@allure.severity(Severity.NORMAL)
def test_faqs(app: ApplicationManager):
    allure_labels(feature='Page faqs',
                  title='Switch on Faqs Page')

    app.main.open()
    (app.faqs.switch())

    app.faqs.should_have(faqs.expected_text)


@allure.severity(Severity.NORMAL)
def test_privacy_policy(app: ApplicationManager):
    allure_labels(feature='Page Privacy Policy',
                  title='Switch on Privacy Policy page')

    app.main.open()
    (app.privacy_policy.switch())

    app.privacy_policy.should_have(policy.expected_text)



@allure.severity(Severity.NORMAL)
def test_terms_conditions(app: ApplicationManager):
    allure_labels(feature='Page Terms Conditions',
                  title='Switch on Terms Conditions page')

    app.main.open()
    (app.terms_conditions.switch())

    app.terms_conditions.should_have(limitation.expected_text)
