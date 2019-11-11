# You have a basketball hoop and someone says that you can play one of two games.
# Game 1: You get one shot to make the hoop.
# Game 2: You get n shots and have to make k of n shots.
# If p is the probability of making a particular shot, for which values of p should
# you pick one game or the other ?
# NB: This is a generalisation of the Basketball question where n = 3 and k = 2.

from math import factorial


def combination(n, k):
    assert k <= n
    return factorial(n) // factorial(k) // factorial(n - k)


def basketball(n, k, p):
    p_game_2 = 0
    for i in range(k, n + 1):
        p_game_2 += combination(n, i) * p ** i * (1 - p) ** (n - i)
    if p_game_2 == p:
        return 0
    return (p < p_game_2) + 1
