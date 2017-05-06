from .base_card import BaseCard


class Countess(BaseCard):
    """The Countess card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 7

    @property
    def name(self):
        """The name of the card."""
        return 'countess'

    def play(self, player, game):
        """The countess does nothing when played. Special rules are found in Player."""
        return
