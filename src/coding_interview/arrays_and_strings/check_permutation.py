# Exercise 1.2:
# Given two strings, write a method to decide if one is a permutation of the other.

from coding_interview.utils import SuperDict


def check_permutation_first_attempt(left, right):
    # Time complexity = O(n+m)
    # Memory complexity = O(n+m)
    if len(left) != len(right):
        return False
    letter_dict = SuperDict()
    for letter in left:
        letter_dict.add(letter, 1)
    for letter in right:
        letter_dict.subtract(letter, 1)
    if set(letter_dict.values()) == {0}:
        return True
    return False


def check_permutation_second_attempt(left, right):
    # Time complexity = O(n.log(n)+m.log(m))
    # Memory complexity = O(1)
    return sorted(left) == sorted(right)
