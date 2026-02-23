'''
Problem Description:
Given a binary string s and an integer k, return True if every possible
binary code of length k appears as a substring of s.
Otherwise, return False.

There are exactly 2^k possible binary strings of length k.
We must verify that all of them exist as substrings in s.

Approach:
- The total number of distinct binary codes of length k is 2^k.
- Use a dictionary (or set) to store unique substrings of length k.
- Slide a window of size k across the string:
    - Extract substring s[i:i+k]
    - If it is new, store it and decrement the remaining expected count.
- Stop early if all 2^k codes are found.
- Return True if expected becomes 0; otherwise False.

Time Complexity:
O(n * k), where:
  n = length of string s
  k = substring length
(Substring slicing costs O(k))

Space Complexity:
O(2^k), for storing distinct substrings.
'''
class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        expected = 1 << k  
        d = {}
        i = 0

        while expected != 0 and i < (len(s) - k + 1):
            substring = s[i:i + k]
            if substring not in d:
                d[substring] = 1
                expected -= 1
            i += 1

        return expected == 0
