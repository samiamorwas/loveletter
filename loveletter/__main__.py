"""
Run a fun game of Love Letter in the command line!
"""

if __name__ == '__main__':
    from .game import Game

    game = Game(['max', 'jon'])
    game.play()
