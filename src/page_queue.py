"""Page Queue"""
from queue import Queue


class PageQueue(Queue):
    """
    Page Queue class with low level shuffling methods.
    """

    def __init__(self, maxsize: int = None):
        super().__init__(maxsize=maxsize)

    def shift(self, index: int):
        """
        Shift values from the right of a given index
        over the hole at the given index
        :param index: item that is being "removed"
        :return:
        """
        if index < 0:
            raise ValueError('index must be greater than 0: {}'.format(index))

        for idx in range(index, len(self.queue)):
            self.queue[idx] = self.queue[idx + 1]


