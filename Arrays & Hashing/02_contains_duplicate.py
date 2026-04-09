# Contains Duplicate
# Easy
# Topics
# Company Tags
# Hints
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false


# Topics

# Recommended Time & Space Complexity

# Hint 1

# Hint 2

# Hint 3

# Company Tags
# Seen this question in a real interview?
# Yes
# No
# Acceptance Rate
# 72.4%

# Solution 1
# +

# NeetBot
# |

# Hint
# |
# |
# Ln 1, Col 1
# 123

nums = [1,2,3,3]

def check_duplicate():
    """
    Checks if any array has a duplicate number
    return true if exist
    else return false
    """
    new_set = set()
    for num in nums:
        if num in new_set:
            return True
        new_set.add(num)

    return False
        
print(check_duplicate())
        


        