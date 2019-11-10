# Implement a method to perform basic string compression using the counts of repeated
# characters. For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string. You can assume the string has only
# uppercase and lowercase letters (a-z).


def string_compression(word):
    # Complexity:
    #       Memory: O(1)
    #       Time: O(N)
    length = len(word)
    compressed_word = ['.' for _ in range(52)]
    compressed_word[0] = word[0]
    compressed_index = 0
    letter_count = 1
    for index in range(1, length):
        if word[index] == word[index - 1]:
            letter_count += 1
        else:
            compressed_word[compressed_index + 1] = str(letter_count)
            letter_count = 1
            compressed_word[compressed_index + 2] = word[index]
            compressed_index += 2
    compressed_word[compressed_index + 1] = str(letter_count)
    compressed_index += 2

    if length < compressed_index:
        return word
    return ''.join(compressed_word[:compressed_index])
