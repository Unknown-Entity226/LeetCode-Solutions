'''
Problem Description:
The count-and-say sequence is defined as:
  countAndSay(1) = "1"
  countAndSay(n) = run-length encoding (RLE) of countAndSay(n - 1)

Run-length encoding replaces consecutive identical characters
with the count followed by the character.

Given a positive integer n, return the nth term of the count-and-say sequence.

Approach:
- Use recursion to build the sequence from 1 up to n.
- Define a helper function that performs run-length encoding (RLE)
  on a given string.
- For each term:
  - Traverse the previous string.
  - Count consecutive identical characters.
  - Append the count and the character to the result string.
- Base case: when n == 1, return "1".

Time Complexity:
O(L), where L is the length of the resulting string at step n.
(Each character is processed once per term.)'''

class Solution(object):
    def countAndSay(self, n):

        def rle(s):
            result = ""
            prev = s[0]
            count = 1

            for i in range(1, len(s)):
                if s[i] == prev:
                    count += 1
                else:
                    result += str(count) + prev
                    prev = s[i]
                    count = 1

            result += str(count) + prev
            return result

        if n == 1:
            return "1"

        return rle(self.countAndSay(n - 1))
