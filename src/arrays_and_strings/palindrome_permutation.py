# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be
# limited to just dictionary words.
# Example:
#       Input: Tact Coa
#       Output: True (permutations: "taco cat", "atco cta", etc.)


from string import ascii_lowercase

from bitarray import bitarray


def palindrome_permutation_first_attempt(sentence):
    # Complexity
    #   Memory: O(N)
    #   Time: O(N)
    letters = set(ascii_lowercase)
    letters_dict = dict()
    for letter in letters:
        letters_dict[letter] = 0
    odds = 0
    for raw_letter in sentence:
        letter = raw_letter.lower()
        if letter.lower() in letters:
            if letters_dict[letter] % 2 == 1:
                odds -= 1
            else:
                odds += 1
            letters_dict[letter] += 1
    return odds <= 1


def palindrome_permutation_second_attempt(sentence):
    # Complexity
    #   Memory: O(1)
    #   Time: O(N)
    letters_array = bitarray(26)
    letters_array.setall(0)
    for letter in sentence:
        letter_index = ord(letter.lower()) - 97
        if 0 <= letter_index < 26:
            letters_array[letter_index] = not letters_array[letter_index]
    return sum(letters_array) <= 1
