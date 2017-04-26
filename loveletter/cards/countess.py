from cards.base_card import BaseCard


class Countess(BaseCard):
    """The Countess card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 7
