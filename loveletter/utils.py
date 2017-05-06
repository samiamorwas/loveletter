from random import shuffle

"""Common utility methods for running the game."""


def get_readable_list(obj_list):
    """Return a readable string describing a list of game objects."""
    return ', '.join(str(obj) for obj in obj_list)


def get_random_target(current_player, players):
    """Return a random player that isn't the current player."""
    other_players = list(filter(lambda player: player is not current_player, players))
    shuffle(other_players)
    return other_players.pop()
