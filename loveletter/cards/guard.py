from cards.base_card import BaseCard


class Guard(BaseCard):
    """The Guard card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 1
