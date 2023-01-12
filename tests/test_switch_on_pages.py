import allure
from allure_commons.types import Severity
from model.application_manager import ApplicationManager
from model.data.user import margo
from utils.allure_labels import allure_labels


@allure.severity(Severity.CRITICAL)
def test_payment_page(app: ApplicationManager):
    allure_labels(feature='Page payment',
                  title='Switch on Payment Page')

    (
        app.payment.search(margo.things)
        .choose_things()
        .add()
        .go_checkout()
        .fill_form(margo.email, margo.name, margo.last_name, margo.country, margo.code, margo.city,
                   margo.phone)
        .switch()
    )


    app.payment.should_have_text(margo.text)


@allure.severity(Severity.NORMAL)
def test_faqs(app: ApplicationManager):
    allure_labels(feature='Page faqs',
                  title='Switch on Faqs Page')

    (
        app.faqs.switch()
    )

    app.faqs.should_have_text()


@allure.severity(Severity.NORMAL)
def test_privacy_policy(app: ApplicationManager):
    allure_labels(feature='Page Privacy Policy',
                  title='Switch on Privacy Policy page')
    (
        app.privacy_policy.switch()
    )

    app.privacy_policy.should_have_text()



@allure.severity(Severity.NORMAL)
def test_terms_conditions(app: ApplicationManager):
    allure_labels(feature='Page Terms Conditions',
                  title='Switch on Terms Conditions page')
    (
        app.terms_conditions.switch()
    )

    app.terms_conditions.should_have_text()
