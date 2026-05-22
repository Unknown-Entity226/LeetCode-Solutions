'''
Problem Description:
Given two strings ransomNote and magazine,
return True if ransomNote can be constructed
using the letters from magazine.

Each letter in magazine can only be used once.

Approach:
- Since the strings contain only lowercase English letters,
  use a fixed-size frequency array of size 26.

- Count occurrences of each character in magazine.

- Traverse ransomNote:
    - If the required character is available,
      decrement its frequency.
    - Otherwise, return False immediately.

- If all characters are successfully matched,
  return True.

Time Complexity:
O(m + n)

where:
  m = length of magazine
  n = length of ransomNote

Space Complexity:
O(1)

Because the frequency array size is fixed at 26.'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        storage = [0] * 26

        # Count magazine characters
        for ch in magazine:
            storage[ord(ch) - ord("a")] += 1

        # Try constructing ransomNote
        for ch in ransomNote:

            idx = ord(ch) - ord("a")

            if storage[idx] > 0:
                storage[idx] -= 1
            else:
                return False

        return True
