from .base_card import BaseCard


class King(BaseCard):
    """The King card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 6
