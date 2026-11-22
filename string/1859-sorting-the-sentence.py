"""
Problem Description:
Given a shuffled sentence where each word has its original 1-indexed
position appended to its end, reconstruct and return the original sentence.

Approach:
Use an array to restore the original word order.

1. Split the shuffled sentence into individual words.
2. Create a result array of the same length as the number of words.
3. Iterate through each word:
   - Extract the last character to obtain its original position.
   - Convert the position to a zero-based index by subtracting 1.
   - Remove the last character to obtain the original word.
   - Place the word at its corresponding index in the result array.
4. Join the result array using spaces and return the reconstructed sentence.

Time Complexity: O(n + k)
Reason: Splitting and joining take O(n), while processing all characters
of the words takes O(k), where k is the total number of characters.

Space Complexity: O(n + k)
Reason: The split list and result array store the words, requiring space
proportional to the input size.
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        
        s = s.split()

        result = [0]*len(s)


        for i in s:

            result[int(i[-1])-1] = i[:-1]


        return " ".join(result)
