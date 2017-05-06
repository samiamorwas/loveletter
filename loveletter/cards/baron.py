from .base_card import BaseCard
from .. import utils


class Baron(BaseCard):
    """The Baron card."""

    @property
    def rank(self):
        """The rank of the card."""
        return 3

    @property
    def name(self):
        """The name of the card."""
        return 'baron'

    def play(self, player, game):
        """The action to take when the card is played."""
        target = utils.get_random_target(player, game.players)
        target_rank = target.get_hand_rank()
        player_rank = player.get_hand_rank()

        if target_rank < player_rank:
            target.is_out = True
        elif player_rank < target_rank:
            player.is_out = True
