import abc


class BaseCard(metaclass=abc.ABCMeta):
    """The abstract card API"""

    @abc.abstractproperty
    def rank(self):
        """The rank of the card."""
        return

    @abc.abstractproperty
    def name(self):
        """The name of the card."""
        return ''

    @abc.abstractmethod
    def play(self, player, game):
        """The action to take when the card is played."""
        return

    def __str__(self):
        """Use the class name as the name of the card."""
        return '{0}({1})'.format(type(self).__name__, self.rank)
