"""
Problem Description:
Merge two strings by taking characters alternately,
starting with word1. If one string is longer, append
its remaining characters at the end.

Approach:
- Use two pointers to traverse both strings.
- Append one character from each string alternately.
- Continue until one string is exhausted.
- Append the remaining characters of the longer string.
- Join the character list to form the final string.

Time Complexity:
O(n + m)

Reason:
- n = length of word1.
- m = length of word2.
- Each character from both strings is visited exactly once.
- Joining the character list also takes O(n + m).

Space Complexity:
O(n + m)

Reason:
- The merged list stores all characters of both strings.
- The output string also contains n + m characters.
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        i = 0
        j = 0
        while i<len(word1) and j<len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i+=1
            j+=1
        while  i<len(word1):
            merged.append(word1[i])
            i+=1
        while j<len(word2):
            merged.append(word2[j])
            j+=1
        return "".join(merged)
