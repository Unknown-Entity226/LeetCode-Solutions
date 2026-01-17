'''
Problem Description:
A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward.
Given a string s, return True if it is a palindrome, or False otherwise.
Alphanumeric characters include letters and digits.
Approach:
- Use two pointers: one starting from the beginning (i) and one from the end (j).
- Move the pointers inward:
  - Skip characters that are not alphanumeric.
  - Compare characters in a case-insensitive manner.
- If at any point the characters do not match, return False.
- If all valid characters match, return True.
Time Complexity: O(n), where n is the length of the string.'''
class Solution(object):
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False

        return True
