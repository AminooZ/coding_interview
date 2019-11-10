# Assume you have a method isSubstring which checks if one word is a substring of
# another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1
# using only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").


def is_substring(sub_string, string):
    return sub_string in string


def string_rotation(string1, string2):
    return is_substring(
        sub_string=string1,
        string=string2 + string2[:-1]
    ) and len(string1) == len(string2)
