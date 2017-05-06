from .base_card import BaseCard


class Priest(BaseCard):
    """The Priest card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 2

    @property
    def name(self):
        """The name of the card."""
        return 'priest'

    def play(self, player, game):
        """The action to take when the card is played."""
        return
