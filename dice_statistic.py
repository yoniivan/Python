# Calculates the probability of getting X of sum of both dices.

import itertools
from fractions import Fraction


def odds_of_getting_sum_dice(n: "2 < n < 12"):
    if n < 2 or n > 12:
        raise ValueError("Please enter a number between 2 and 12.")

    dice = itertools.product(range(1, 7), range(1, 7))
    dup = itertools.tee(dice, 2)
    outcomes = filter(lambda x: x[0] + x[1] == n, dup[0])
    dice_len = len(list(dup[1]))
    odds = len(list(outcomes))
    return dice_len, odds, Fraction(dice_len) / Fraction(odds)


my_func = odds_of_getting_sum_dice(13)
print(f'dice = {my_func[0]}, odds = {my_func[1]}, {my_func[2]}')
