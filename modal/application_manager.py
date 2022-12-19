from modal.pages.faqs import FAQS
from modal.pages.payment import Payment
from modal.pages.privacy_policy import PrivacyPolicy
from modal.pages.terms_conditions import TermsConditions


class ApplicationManager:
    def __init__(self):
        self.payment = Payment()
        self.faqs = FAQS()
        self.privacy_policy = PrivacyPolicy()
        self.terms_conditions = TermsConditions
