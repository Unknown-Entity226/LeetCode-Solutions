'''
Problem Description:
You are given two permutations A and B of length n.

Define the prefix common array C such that:
    C[i] = count of numbers present in both:
        A[0..i] and B[0..i]

Return the array C.

Approach:
- Maintain a frequency map to track occurrences
  of numbers from both arrays.

- For each index i:
    1. Increment frequency of A[i]
    2. Increment frequency of B[i]

- When a number's frequency becomes 2,
  it means the number has now appeared in BOTH arrays'
  prefixes → increment common count.

- Special case:
    If A[i] == B[i],
    the same number gets incremented twice in the same iteration,
    causing double counting.
    So subtract 1.

Time Complexity:
O(n)

Space Complexity:
O(n)
'''
class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        freq = {}
        for i in range(1, len(A)+1):
            freq[i] = 0
        output = []
        count = 0
        for i in range(len(A)):
            freq[A[i]] +=1
            freq[B[i]] +=1
            if freq[A[i]] == 2:
                count+=1
            if freq[B[i]] == 2:
                count+=1  
            if A[i] == B[i]:
                count-=1
            output.append(count)
        return output


