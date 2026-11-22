"""
Problem Description:
Given a sentence containing words and positive integers, determine
whether all numbers appear in strictly increasing order from left to right.

Approach:
Use a single traversal with a variable to track the previously encountered
number.

1. Split the sentence into individual tokens.
2. Initialize last = 0, since all numbers are positive.
3. Iterate through the tokens:
   - Check whether the current token contains a number using isdigit().
   - Convert it to an integer.
   - If it is less than or equal to the previous number, return False.
   - Otherwise, update last with the current number.
4. If the traversal completes without finding a violation, return True.

Time Complexity: O(n)
Reason: Splitting and traversing the sentence take linear time. Each
token is examined once, and integer conversion is proportional to
the number of digits in that token.

Space Complexity: O(n)
Reason: split() creates a list containing all tokens from the sentence.
Apart from this list, only constant auxiliary space is used.
"""


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        

        s = s.split()

        last = 0

        for i in s:
            if i.isdigit():

                if int(i)<=last:
                    return False

                last = int(i)

        return True
