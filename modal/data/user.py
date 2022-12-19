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
             text='Payment')
