# Valid Anagram
# Easy
# Topics
# Company Tags
# Hints
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.

s = "racecar"
t = "carrace"

from collections import Counter

print(Counter(s) == Counter(t))

# solution 2

char_count_s = {}
char_count_t = {}

def count_characters(char_count, text):
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

print(count_characters(char_count_s, s) == count_characters(char_count_t, t))
