#!/usr/bin/env python

"""
Run a fun game of Love Letter in the command line!
"""

from deck import Deck
from player import Player

deck = Deck()

player1 = Player('max', deck)
player2 = Player('jon', deck)

print(player1)
print(player2)

card1 = player1.take_turn()
print(card1)
card2 = player2.take_turn()
print(card2)

print(deck)
