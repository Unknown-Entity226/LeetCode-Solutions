"""
Problem Description:
Given a string s, return the maximum length of a substring
such that every character appears at most twice.

Approach:
- Maintain a sliding window using left and right pointers.
- Store the frequency of each character in the current
  window.
- Expand the window using right while the current character
  occurs fewer than two times.
- If the current character already occurs twice, move left
  forward and decrease the frequency of the character being
  removed.
- Track the maximum valid window length.

Time Complexity:
O(n)

Reason:
- The right pointer moves forward at most n times.
- The left pointer also moves forward at most n times.
- When right does not move, left moves instead.
- Therefore, the total number of pointer movements is O(n).

Space Complexity:
O(min(n, k))

Reason:
- The frequency map stores the distinct characters present
  in the current window.
- k is the number of possible distinct characters.
- For lowercase English letters, k is at most 26, making
  the space complexity O(1).
"""

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        freq = {}

        maxString = 0

        while right<len(s):

            if s[right] not in freq:
                freq[s[right]] = 1
                right+=1
            elif freq[s[right]] <2:
                freq[s[right]]+=1
                right+=1
            
            elif freq[s[right]] == 2:
                freq[s[left]]-=1
                left+=1

            maxString = max(maxString, right-left)
            
        return maxString
