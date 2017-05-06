from .base_card import BaseCard


class Handmaid(BaseCard):
    """The Handmaid card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 4

    @property
    def name(self):
        """The name of the card."""
        return 'handmaid'

    def play(self, player, game):
        """Prevent the player from being targeted."""
        player.is_targetable = False
