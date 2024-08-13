class Solution:
    def repeatedSubstringPattern(self, s:str)-> bool:
        n = len(s)
        for i in range(1, n//2+1):
            if n%i == 0:
                substring = s[:i]
                if substring*(n//i) == s:
                    return True
        return False

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]


# The key idea behind this solution is based on a property of strings that can be constructed by 
# repeating a substring:

# 1. If a string `s` can be constructed by repeating a substring, then 
#    concatenating `s` with itself (`s+s`) and removing the first and last 
#    characters will always contain the original string `s` as a substring.
# 2. Conversely, if `s` cannot be constructed by repeating a substring, then `s` 
#    will not be found in `(s+s)[1:-1]`.

# Let's break it down step by step:
# 1. `s+s`: This creates a new string by concatenating `s` with itself.
# 2. `(s+s)[1:-1]`: This slices the concatenated string, removing the first and last characters.
# 3. `s in (s+s)[1:-1]`: This checks if the original string `s` is a substring of the sliced string.

# Let's see how this works with the given examples:

# 1. For s = "abab":
#    - s+s = "abababab"
#    - (s+s)[1:-1] = "bababab"
#    - "abab" is in "bababab", so it returns True

# 2. For s = "aba":
#    - s+s = "abaaba"
#    - (s+s)[1:-1] = "baab"
#    - "aba" is not in "baab", so it returns False

# 3. For s = "abcabcabcabc":
#    - s+s = "abcabcabcabcabcabcabcabc"
#    - (s+s)[1:-1] = "bcabcabcabcabcabcabcab"
#    - "abcabcabcabc" is in "bcabcabcabcabcabcabcab", so it returns True