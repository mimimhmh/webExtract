from enum import Enum, unique


@unique
class Classification(Enum):
    G = 'General Audience'
    PG = 'Parental Guidance Recommended'
    M = 'Mature Audience'
    R13 = 'Restricted 13'
    R16 = 'Restricted 16'
    R18 = 'Restricted 18'
    TBC = 'Pending Classification'
    UNDEFINED = 'Undefined'


class Game(object):

    def __init__(self, game_id, name, price, classification, release_date,
                 in_stock=True):
        self.game_id = game_id
        self.name = name
        self.price = price
        self.classification = classification
        self.release_date = release_date
        self.in_stock = in_stock
