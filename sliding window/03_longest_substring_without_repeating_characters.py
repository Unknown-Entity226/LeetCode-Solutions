'''
Problem Description:
Given a string s, find the length of the longest substring
without repeating characters.

Approach:
- Use the sliding window technique with two pointers.
- Maintain a dictionary to store the most recent index
  where each character was seen.
- Expand the window by moving the right pointer.
- If the current character has already been seen within the
  current window, move the left pointer just after the previous
  occurrence of that character.
- Update the maximum length of the substring after each step.

Time Complexity:
O(n), where n is the length of the string.
Each character is processed at most twice.

Space Complexity:
O(m), where m is the size of the character set.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1

            seen[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len
