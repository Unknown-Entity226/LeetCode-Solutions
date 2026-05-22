"""
Problem Description:
Given a string s, return the index of the first non-repeating character.
If every character repeats, return -1.

Approach:
- Use a hashmap to track character occurrence status.
- First occurrence:
      store character -> index
- Repeated occurrence:
      mark character as repeated using "x"
- Traverse the string again:
      first character whose stored value is not "x"
      is the first unique character.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""
class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        store = {}

        # Store first occurrence index or mark repeated chars
        for i in range(len(s)):

            if s[i] not in store:
                store[s[i]] = i

            else:
                store[s[i]] = "x"

        # Find first non-repeating character
        for i in range(len(s)):

            if store[s[i]] != "x":
                return store[s[i]]

        return -1
