from random import random


def select(lst):
    """Select a random value from a given list.

    Arguments:
        lst: list; the list from which a value will be selected.

    Returns:
        One item selected randomly from the list.
    """
    return lst[int(random() * len(lst))]


def roll(count, value):
    """Return a total value from rolled dice.

    Arguments:
        count: int; the number of dice to roll.

        value: int; the value of each die.

    Returns:
        total: int; the sum total of all rolls.
    """

    total = 0
    for _ in range(count):
        total += int(random() * value) + 1
    return total
