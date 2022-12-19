from dataclasses import dataclass


@dataclass
class User1:
    things: str = 'Bag'
    email: str = 'LogunovaR@mail.com'
    name: str = 'Margo'
    last_name: str = 'Logunova'
    country: str = 'Turkey'
    city: str = 'Antalya'
    phone: str = '89111111111'
    text: str = 'Your cart has been updated and the items you added can’t be shipped to your address. Remove the items to complete your order.'
