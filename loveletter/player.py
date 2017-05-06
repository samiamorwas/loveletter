from random import shuffle

from . import utils


class Player:
    """A representation of a Love Letter player.

    A player has a hand consisting of a single card, and a reference
    to a deck shared by all players in the game.
    """

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = [self.deck.draw()]
        self.is_out = False
        self.is_targetable = True

    def __str__(self):
        """Print the player's name and current hand."""
        readable_hand = utils.get_readable_list(self.hand)
        return '{0}: {1}'.format(self.name, readable_hand)

    def take_turn(self, game):
        """Take a turn by drawing a card from the deck and playing it."""
        self.hand.append(self.deck.draw())
        # Reset the targetable state at the beginning of each turn.
        self.is_targetable = True
        card = self._get_card_to_play()
        card.play(self, game)
        return card

    def get_hand_rank(self):
        """Get the rank of the card in hand."""
        return self.hand[0].rank

    def _get_card_to_play(self):
        """Get the card to play.

        If the hand contains the countess and the prince or king,
        the countess must be played. Otherwise, pick a card at random.
        """
        card_names = [card.name for card in self.hand]

        if 'countess' in card_names and ('prince' in card_names or 'king' in card_names):
            # Force the countess to be played by sorting by rank, since it has a higher rank
            # than the prince and the king.
            self.hand = sorted(self.hand, key=lambda card: card.rank)
            print(self.name + " forced to play countess!")

        return self.hand.pop()
