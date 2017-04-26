from random import shuffle

import utils


class Player:
    """A representation of a Love Letter player.

    A player has a hand consisting of a single card, and a reference
    to a deck shared by all players in the game.
    """

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = [self.deck.draw()]

    def __str__(self):
        """Print the player's name and current hand."""
        readable_hand = utils.get_readable_cards(self.hand)
        return '{0}: {1}'.format(self.name, readable_hand)

    def take_turn(self):
        """Take a turn by drawing a card from the deck and playing it."""
        self.hand.append(self.deck.draw())
        shuffle(self.hand)
        return self.hand.pop()
