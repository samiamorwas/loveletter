from .base_card import BaseCard


class Priest(BaseCard):
    """The Priest card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 2
