from .base_card import BaseCard


class Prince(BaseCard):
    """The Prince card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 5

    @property
    def name(self):
        """The name of the card."""
        return 'prince'

    def play(self, player, game):
        """The action to take when the card is played."""
        return
