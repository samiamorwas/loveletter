from .base_card import BaseCard


class Guard(BaseCard):
    """The Guard card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 1

    @property
    def name(self):
        """The name of the card."""
        return 'guard'

    def play(self, player, game):
        """The action to take when the card is played."""
        return
