"""
Problem Description:
Given an array of strings, group together all strings that are anagrams
of each other. Anagrams contain exactly the same characters with the
same frequencies, regardless of their order.

Approach:
Use a hash map with a sorted character tuple as the key.

1. Iterate through every string in strs.
2. Sort its characters and convert them into a tuple.
3. Use this tuple as the key in the dictionary.
4. If the key already exists, append the current string to its group.
5. Otherwise, create a new group containing the current string.
6. Return all dictionary values as the grouped anagrams.

Strings that are anagrams produce identical sorted tuples, so they
automatically belong to the same group.

Time Complexity: O(n * k log k)
Reason: For n strings of maximum length k, sorting each string takes
O(k log k), resulting in O(n * k log k) overall.

Space Complexity: O(n * k)
Reason: The dictionary stores all input strings in groups, and the
sorted tuple keys require additional storage proportional to the total
number of characters.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapped_dict = {}
        for i in strs:
            s = tuple(sorted(i))
            if mapped_dict.get(s) is not None:
                mapped_dict[s].append(i)
            else:
                mapped_dict[s] = [i]
        return mapped_dict.values()
