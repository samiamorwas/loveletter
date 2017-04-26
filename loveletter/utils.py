"""Common utility methods for running the game."""


def get_readable_cards(cards):
    """Return a readable string describing a list of cards."""
    return ', '.join(str(card) for card in cards)
