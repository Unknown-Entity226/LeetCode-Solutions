"""
Problem Description:
Given a string, remap the telephone keypad to minimize
the total number of key presses required to type the
word.

Approach:
- Count the frequency of each character.
- Sort the frequencies in descending order.
- Assign the highest frequencies to the lowest push
  counts.
- Every 8 characters, increase the required push count.
- Compute the total pushes.

Time Complexity:
O(n + k log k)

Reason:
- Counting frequencies takes O(n).
- Sorting k distinct characters takes O(k log k).
- Assigning push counts takes O(k).

Space Complexity:
O(1)

-Maximum space acquired is 26
O(26) = O(1)
"""

class Solution:
    def minimumPushes(self, word: str) -> int:
        
        freq  = {}

        for i in word:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse = True))

        counter = 1
        count = 2
        total = 0
        for i in freq:
            total += freq[i]*counter
            count+=1
            if count >9:
                count = 2
                counter+=1
        return total
