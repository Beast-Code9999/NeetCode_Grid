# You are given an array of strings strs. Return the longest common prefix of all the strings.

# If there is no longest common prefix, return an empty string "".

# Example 1:

# Input: strs = ["bat","bag","bank","band"]

# Output: "ba"
# Example 2:

# Input: strs = ["dance","dag","danger","damage"]

# Output: "da"
# Example 3:

# Input: strs = ["neet","feet"]

# Output: ""
# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] is made up of lowercase English letters if it is non-empty.

strs = ["dance","dag","danger","damage"]

def get_longest_common_prefix( array ):
    """
    return longest common prefix of strings in an array
    """

    output = ""

    for i in range(len(strs[0])):
        reference_caracters_of_first_item = strs[0][i]
        for item in strs:
            if i > len(item) or item[i] != reference_caracters_of_first_item:
                return output

        output += reference_caracters_of_first_item
            

print(get_longest_common_prefix(strs))

