# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to
# check if they are one edit (or zero) away.
# Examples:
#   pale, ple   -> True
#   pales, pale -> True
#   pale, bale  -> True
#   pale, bake  -> False


def one_away(word_a, word_b):
    # Complexity:
    #       Time: O(N + M)
    #       Memory: O(1)
    if len(word_b) >= len(word_a):
        word_a, word_b = word_b, word_a
    len_diff = len(word_a) - len(word_b)
    if len_diff > 1:
        return False
    elif len_diff == 0:
        edits = 0
        for letter_a, letter_b in zip(word_a, word_b):
            if letter_a != letter_b:
                edits += 1
            if edits > 1:
                return False
    else:
        for index in range(len(word_b)):
            if word_b[index] not in word_a[index:index + 2]:
                return False
    return True
