from cards.base_card import BaseCard


class Baron(BaseCard):
    """The Baron card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 3
