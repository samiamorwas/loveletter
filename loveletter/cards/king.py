from .base_card import BaseCard


class King(BaseCard):
    """The King card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 6

    @property
    def name(self):
        """The name of the card."""
        return 'king'

    def play(self, player, game):
        """The action to take when the card is played."""
        return
