"""
Problem Description:
You are given:
- words: an array of lowercase English words
- weights: an array of length 26 where weights[i]
  is the weight of the ith lowercase letter

For each word:
1. Compute the sum of the weights of its characters.
2. Take the sum modulo 26.
3. Convert the result using reverse alphabetical mapping:

       0 -> 'z'
       1 -> 'y'
       ...
      25 -> 'a'

Return the concatenation of the mapped characters
for all words.

Approach:
- For each word:
    - Compute its weight by summing character weights.
    - Compute weight % 26.
    - Map the result to a character using:

          chr(122 - remainder)

      since:
          ord('z') = 122

- Append the mapped character to the result.

Time Complexity:
O(nm)
n: no of words in the words array
m: average length of each word in words

Space Complexity:
O(n)
n being length of the output string
"""

class Solution(object):

    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """

        result = ""

        for word in words:

            s = 0

            for ch in word:
                s += weights[ord(ch) - 97]

            result += chr(122 - s % 26)

        return result
