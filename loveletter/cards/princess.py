from .base_card import BaseCard


class Princess(BaseCard):
    """The Princess card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 8

    @property
    def name(self):
        """The name of the card."""
        return 'princess'

    def play(self, player, game):
        """If the princess is played, the player is out."""
        player.is_out = True
