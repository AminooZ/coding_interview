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
    #       Time: O(N) (N is the length of the shortest string
    #       Memory: O(N)
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


def another_one_away(word_a, word_b):
    # Complexity
    #   Time: O(N)
    #   Memory: O(N)
    # Case 1: Length difference > 1 then more than one away
    if abs(len(word_a) - len(word_b)) > 1:
        return False
    # Case 2: Same length
    elif abs(len(word_a) - len(word_b)) == 0:
        nb_edits = 0
        for (a, b) in zip(word_a, word_b):
            if a != b:
                nb_edits += 1
        return nb_edits == 1
    # Case 3: Length difference of 1
    else:
        if len(word_a) > len(word_b):
            long_word, short_word = word_a, word_b
        else:
            long_word, short_word = word_b, word_a
        nb_edits = 0
        l, s = 0, 0
        while s < len(short_word) and l < len(long_word) and nb_edits < 2:
            if long_word[l] != short_word[s]:
                nb_edits += 1
                l += 1
            else:
                l += 1
                s += 1
        if nb_edits < 2:
            return True
        else:
            return False
