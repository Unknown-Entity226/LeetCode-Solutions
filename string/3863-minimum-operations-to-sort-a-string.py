"""
Problem Description:
Given a lowercase string s, find the minimum number of operations
required to sort it in non-descending order. Each operation sorts
a proper substring, meaning the substring cannot be the entire string.
Return -1 if sorting is impossible.

Approach:
- Sort s and return 0 if it is already sorted.
- Return -1 if the string has length 2 and is unsorted.
- Count character frequencies and identify the minimum and maximum
  characters.
- Use the first and last characters, along with the frequencies of
  the minimum and maximum characters, to determine the answer.

Time Complexity:
O(n log n)

Reason:
- Sorting s takes O(n log n).
- Computing character frequencies and minimum/maximum characters
  takes O(n).
- The remaining checks take O(1).
- Therefore, sorting dominates the total time complexity.

Space Complexity:
O(n)

Reason:
- sorted(s) creates a sorted list of characters, and join creates
  a new string.
- The frequency dictionary uses at most 26 entries because s
  contains only lowercase English letters.
"""
class Solution:
    def minOperations(self, s: str) -> int:
        
        sorted_s = "".join(sorted(s))
        if s == sorted_s:
            return 0


        if len(s)==2:
            return -1
    
        freq = {}

        min_char = "z"
        max_char = "a"

        for i in s:
            if i in freq:
                freq[i]+=1

            else:
                freq[i] = 1

            if i<min_char:
                min_char = i
            
            if i>max_char:
                max_char = i

        if s[0] == min_char or s[-1] == max_char:
            return 1
        
        elif s[0] == max_char and s[-1] == min_char:
            if freq[max_char]>1 or freq[min_char]>1:
                return 2
            else:
                return 3

        return 2
