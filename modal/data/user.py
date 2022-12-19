from dataclasses import dataclass


@dataclass
class User:
    things: str
    email: str
    name: str
    last_name: str
    country: str
    city: str
    phone: str
    text: str


Margo = User(things='Bag', email='LogunovaR@mail.com', name='Margo', last_name='Logunova', country='Turkey',
             city='Antalya', phone='89111111111',
             text='Your cart has been updated and the items you added can’t be shipped to your address. Remove the '
                  'items to comple')
