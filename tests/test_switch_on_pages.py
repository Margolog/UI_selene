import allure
from allure_commons.types import Severity
from modal.application_manager import ApplicationManager
from modal.data.user import Margo


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.feature("Page payment")
@allure.title('Switch on Payment Page')
def test_payment_page(app: ApplicationManager):
    app.payment.open_main()
    app.payment.search_click()
    app.payment.search(Margo.things)
    app.payment.choose_things()
    app.payment.add()
    app.payment.go_checkout()
    app.payment.fill_email(Margo.email)
    app.payment.fill_region()
    app.payment.fill_name(Margo.name)
    app.payment.fill_last_name(Margo.last_name)
    app.payment.fill_country(Margo.country)
    app.payment.fill_code(Margo.code)
    app.payment.fill_city(Margo.city)
    app.payment.fill_phone(Margo.phone)
    app.payment.switch()
    app.payment.should_have_text(Margo.text)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Page faqs")
@allure.title('Switch on Faqs Page')
def test_faqs(app: ApplicationManager):
    app.faqs.open_main()
    app.faqs.scroll()
    app.faqs.switch()
    app.faqs.should_have_text()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Page Privacy Policy")
@allure.title('Switch on Privacy Policy page')
def test_privacy_policy(app: ApplicationManager):
    app.privacy_policy.open_main()
    app.privacy_policy.scroll()
    app.privacy_policy.switch()
    app.privacy_policy.should_have_text()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Page Terms Conditions")
@allure.title('Switch on Terms Conditions page')
def test_terms_conditions(app: ApplicationManager):
    app.terms_conditions.open_main()
    app.terms_conditions.scroll()
    app.terms_conditions.switch()
    app.terms_conditions.should_have_text()
