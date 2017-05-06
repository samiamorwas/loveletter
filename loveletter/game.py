from random import shuffle
from collections import deque

from .deck import Deck
from .player import Player


class Game:
    """A representation of a single game.

    A game consists of a number of players and a deck. Each player takes
    a turn until one player wins, either by being the only player left,
    or by having the highest rank card when the deck is empty.
    """

    def __init__(self, player_names):
        self.deck = Deck()
        self.players = deque([Player(name, self.deck) for name in player_names])
        self.is_over = False

    def __str__(self):
        """Print the players and the deck."""
        players = [str(player) for player in self.players]
        return 'Players: {0}\nDeck: {1}'.format(players, self.deck)

    def _get_winner(self):
        if len(self.players) == 1:
            return self.players.pop()

        return sorted(self.players, key=lambda player: player.get_hand_rank()).pop()

    def _check_is_over(self):
        return self.deck.is_empty() or len(self.players) == 1

    def play(self):
        """Take turns until the game is over."""
        shuffle(self.players)
        while not self.is_over:
            current_player = self.players.popleft()
            played_card = current_player.take_turn(self)

            print('{0} played {1}'.format(current_player.name, played_card))

            self.players.append(current_player)
            eliminated_players = list(filter(lambda player: player.is_out, self.players))

            for player in eliminated_players:
                print(player.name + ' is out!')
                self.players.remove(player)

            self.is_over = self._check_is_over()

        print(self)
        print(self._get_winner().name + ' won!')
