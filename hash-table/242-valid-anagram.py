"""
Problem Description:
Given two strings s and t, determine whether t is an anagram of s.
Two strings are anagrams if they contain exactly the same characters
with the same frequencies, regardless of their order.

Approach:
Use a hash map to maintain character frequencies.

1. Traverse s and store the frequency of every character in a dictionary.
2. Traverse t and decrement the corresponding frequency.
3. If a character in t does not exist in the dictionary, or its frequency
   is already zero, return False.
4. After processing t, verify that every character frequency is zero.
5. If all frequencies are zero, return True.

Time Complexity: O(n + m)
Reason: Building the frequency map takes O(n), processing t takes O(m),
and checking the remaining frequencies takes O(k), where k is the
number of distinct characters. Since k <= n, the overall complexity
is O(n + m).

Space Complexity: O(k)
Reason: The dictionary stores at most k distinct characters from s.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        mapping = {}

        for i in s:
            if i in mapping:
                mapping[i]+=1

            else:
                mapping[i]=1

        for i in t:
            if i not in mapping or mapping[i]-1<0:
                return False

            elif i in mapping:
                mapping[i]-=1

        for i in mapping:
            if mapping[i]!=0:
                return False
                
        return True
