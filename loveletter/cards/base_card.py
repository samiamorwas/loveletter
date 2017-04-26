import abc


class BaseCard(metaclass=abc.ABCMeta):
    """The abstract card API"""

    @abc.abstractproperty
    def rank(self):
        """The rank of the card."""
        return

    def __str__(self):
        """Use the class name as the name of the card."""
        return '{0}({1})'.format(type(self).__name__, self.rank)
