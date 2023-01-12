from model.pages.faqs import FAQSPage
from model.pages.main import MainPage
from model.pages.payment import PaymentPage
from model.pages.privacy_policy import PrivacyPolicyPage
from model.pages.terms_conditions import TermsConditionsPage


class ApplicationManager:
    def __init__(self):
        self.payment = PaymentPage()
        self.faqs = FAQSPage()
        self.privacy_policy = PrivacyPolicyPage()
        self.terms_conditions = TermsConditionsPage()
        self.main = MainPage()
