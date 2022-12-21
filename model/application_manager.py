from model.pages.faqs import FAQS
from model.pages.payment import Payment
from model.pages.privacy_policy import PrivacyPolicy
from model.pages.terms_conditions import TermsConditions


class ApplicationManager:
    def __init__(self):
        self.payment = Payment()
        self.faqs = FAQS()
        self.privacy_policy = PrivacyPolicy()
        self.terms_conditions = TermsConditions()
