# Exercise 1.1:
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures ?


def is_unique_first_attempt(string):
    # Time complexity: O(n)
    # Memory complexity: O(n)
    chars = set()
    for char in string:
        if char in chars:
            return False
        chars.add(char)
    return True


def is_unique_second_attempt(string):
    # Time complexity: O(n)
    # Memory complexity: O(alphabet)
    from string import printable
    alphabet = dict()
    for char in printable:
        alphabet[char] = 0

    for char in string:
        alphabet[char] += 1
        if alphabet[char] > 1:
            return False
    return True


def is_unique_third_attempt(string):
    # Time complexity: O(n.log(n))
    # Memory complexity: O(1)
    string = ''.join(sorted(string))
    for index in range(1, len(string)):
        if string[index - 1] == string[index]:
            return False
    return True
