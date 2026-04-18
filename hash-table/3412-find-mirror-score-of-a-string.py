'''
Problem Description:
For each character s[i], find the closest unmarked index j < i such that
s[j] is the mirror of s[i] (a↔z, b↔y, ...).
When found, mark both i and j and add (i - j) to the score.
Process from left to right and return the total score.

Approach:
- Maintain a map from character → stack (list) of indices of UNMATCHED occurrences.
- For each index i:
    - Compute mirror character using: mirror = chr(ord('a') + ord('z') - ord(s[i]))
    - If there exists an unmatched mirror index (stack non-empty):
        - Pop the most recent index j (this ensures the *closest* j < i).
        - Add (i - j) to the score.
    - Otherwise:
        - Push i onto the stack of s[i] (it remains unmatched for now).

Rationale:
- Using a stack ensures we always match with the closest previous occurrence.
- Each index is pushed and popped at most once → linear time.

Time Complexity:
O(n), where n is the length of s.

Space Complexity:
O(n) in the worst case (all characters unmatched).
'''
class Solution(object):
    def calculateScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        total = 0
        for i in range(len(s)):
            mirror = chr(219-ord(s[i]))
            if mirror in d and d[mirror]:
                total+= i-d[mirror].pop()
            else:
                if s[i] not in d:
                    d[s[i]] = []
                d[s[i]].append(i)
        return total        
