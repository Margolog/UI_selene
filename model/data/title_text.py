from dataclasses import dataclass


@dataclass
class Title:
    expected_text: str


payment = Title(expected_text='Payment')
faqs = Title(expected_text='FAQS')
policy = Title(expected_text='Privacy policy')
limitation = Title(expected_text='Terms of service')
