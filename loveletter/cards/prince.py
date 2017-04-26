from .base_card import BaseCard


class Prince(BaseCard):
    """The Prince card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 5
