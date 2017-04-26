from cards.base_card import BaseCard


class Princess(BaseCard):
    """The Princess card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 8
