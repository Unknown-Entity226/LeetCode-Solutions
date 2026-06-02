"""
Problem Description:
Given a string s, return True if all characters that appear
in the string occur the same number of times.

A string is considered good if every distinct character has
the same frequency.

Approach:
- Use a frequency array of size 26 since the string contains
  lowercase English letters.
- Count the frequency of each character.
- Simultaneously count the occurrences of the first character.
- Traverse the frequency array:
    - Ignore frequencies equal to 0.
    - Every non-zero frequency must equal the frequency of s[0].
- If any frequency differs, return False.
- Otherwise, return True.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution(object):

    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """

        arr = [0] * 26
        count = 0

        for i in range(len(s)):

            if s[i] == s[0]:
                count += 1

            arr[ord(s[i]) - ord('a')] += 1

        for i in range(26):

            if arr[i] != 0 and arr[i] != count:
                return False

        return True
