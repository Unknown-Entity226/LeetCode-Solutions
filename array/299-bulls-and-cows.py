"""
Problem Description:
Given two strings:
- secret
- guess

Return a hint in the format:

    xAyB

where:
- x = number of bulls (correct digit and correct position)
- y = number of cows (correct digit but wrong position)

Duplicate digits must be handled correctly.

Approach:
- Count the frequency of each digit in the secret.
- First pass:
    - Count bulls.
    - Decrease the corresponding frequency since those
      digits have already been matched.
- Second pass:
    - Ignore bull positions.
    - If a guessed digit still has remaining frequency,
      it contributes a cow.
    - Decrease the frequency after using it.
- Return the formatted answer.

Time Complexity:
O(n)

Space Complexity:
O(1)
- At most 10 different digits are stored.
"""

class Solution:

    def getHint(self, secret: str, guess: str) -> str:

        counter = {}

        for i in secret:

            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        cows = 0
        bulls = 0

        for i in range(len(guess)):

            if guess[i] == secret[i]:

                bulls += 1
                counter[guess[i]] -= 1

        for i in range(len(guess)):

            if (
                guess[i] in counter
                and guess[i] != secret[i]
                and counter[guess[i]] > 0
            ):

                cows += 1
                counter[guess[i]] -= 1

        ans = f"{bulls}A{cows}B"

        return ans
