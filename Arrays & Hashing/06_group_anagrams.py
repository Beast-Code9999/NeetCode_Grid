# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

from collections import defaultdict

strs = ["act","pots","tops","cat","stop","hat"]

def group_anagrams( array ):
    anagrams = defaultdict(list) # a default dictionary for keys that does not yet existsg
    
    for item in array:
        # sort word in alphabeical order
        sorted_word = "".join(sorted(item))
        # append to dictionary
        anagrams[sorted_word].append(item)

    return list(anagrams.values())

print(group_anagrams(strs))