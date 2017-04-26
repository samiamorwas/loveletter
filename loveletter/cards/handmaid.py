from .base_card import BaseCard


class Handmaid(BaseCard):
    """The Handmaid card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 4
