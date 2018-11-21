from collections import deque
from queue import PriorityQueue


def opt(page_table: deque, ref_string: deque):
    """
    Optimal scheduling
    :param page_table: page table object
    :param ref_string: reference string to look through
    :return:
    """
    results = PriorityQueue()
    for value in list(page_table):
        try:
            # TODO: deque index does not work in 3.4
            index = ref_string.index(value)
        except ValueError:
            # This page will never be used again, so it is a good victim
            page_table.remove(value)
            return
        else:
            # This serves to reverse the queue, so that the highest index
            # is the lowest number and thus top of the priority queue
            results.put((index * -1, value))

    victim = results.get()[1]
    page_table.remove(victim)
