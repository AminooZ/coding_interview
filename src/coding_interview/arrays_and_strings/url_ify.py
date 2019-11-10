# Write a method to replace all spaces in a string with '%20'. You may assume that the
# string has sufficient space at the end to hold the additional characters, and that
# you are given the "True" length of the string. (Note: if implementing in Java, please
# use a character array so that you can preform this operation inplace.)
# Example:
#       Input: "Mr John Smith       ", 13
#       Output: "Mr%20John%20Smith"


def count_spaces(sentence, length):
    space_count = 0
    for index in range(length):
        if sentence[index] == ' ':
            space_count += 1
    return space_count


def url_ify(sentence, length):
    sentence = list(sentence)
    final_length = length + count_spaces(sentence=sentence, length=length) * 2
    for index in range(length - 1, -1, -1):
        if sentence[index] == ' ':
            sentence[final_length - 3] = '%'
            sentence[final_length - 2] = '2'
            sentence[final_length - 1] = '0'
            final_length -= 3
        else:
            sentence[final_length - 1] = sentence[index]
            final_length -= 1
    return ''.join(sentence)
