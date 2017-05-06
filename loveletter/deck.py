from importlib import import_module
from random import shuffle

from . import utils


class Deck:
    """A representation of a deck of cards.

    Construct the full deck based on the count of each card type.
    """

    _counts = {
        'guard': 5,
        'priest': 2,
        'baron': 2,
        'handmaid': 2,
        'prince': 2,
        'king': 1,
        'countess': 1,
        'princess': 1
    }

    def __init__(self):
        classes = {}
        self.cards = []

        # Get the classes for all card types.
        for card_type in self._counts.keys():
            module = import_module('.cards.' + card_type, __package__)
            classes[card_type] = getattr(module, card_type.capitalize())

        for card_type, count in self._counts.items():
            for _ in range(count):
                card_instance = classes[card_type]()
                self.cards.append(card_instance)

        shuffle(self.cards)

    def __str__(self):
        """Print each card in the deck."""
        return '<{0}>'.format(utils.get_readable_list(self.cards))

    def draw(self):
        """Draw the top card of the deck."""
        return self.cards.pop()

    def is_empty(self):
        """Check if the deck is empty."""
        return not bool(self.cards)
