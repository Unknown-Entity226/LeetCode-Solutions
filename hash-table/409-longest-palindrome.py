'''
Problem Description:
Given a string s consisting of uppercase and lowercase letters,
return the length of the longest palindrome that can be built
using those letters.

Letters are case-sensitive (e.g., 'A' and 'a' are different).

A palindrome reads the same forward and backward.

Approach:
- Count the frequency of each character.
- For each character:
    - If its count is even → use all occurrences.
    - If its count is odd → use (count - 1) occurrences (to keep symmetry).
- At most one character with an odd count can be placed in the center.
- Track whether we have used a center character.

Time Complexity:
O(n), where n is the length of the string.

Space Complexity:
O(1), since character set is fixed to 52 letters.
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = Counter(s)
        count = 0
        used_center = False

        for i in hashmap:
            if hashmap[i] % 2 == 0:
                count += hashmap[i]
            else:
                count += hashmap[i] - 1
                if not used_center:
                    count += 1
                    used_center = True

        return count
