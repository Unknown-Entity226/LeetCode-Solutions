"""
Problem Description:
Given a pattern string and a string s, determine whether s follows the
same pattern.

There must be a bijective mapping between each pattern character and
a non-empty word:
- Every character maps to exactly one word.
- Every word maps to exactly one character.
- No two characters can map to the same word.

Approach:
Use a hash map and a set to maintain a bidirectional mapping.

1. Split s into individual words.
2. If the number of words differs from the length of pattern, return False.
3. Maintain:
   - word_mapping: Maps each pattern character to its corresponding word.
   - visited: Tracks words that have already been assigned.
4. Iterate through pattern and words simultaneously:
   - If the character already exists in word_mapping, verify that it
     maps to the current word.
   - Otherwise, check whether the current word has already been assigned
     to another character.
   - If it has, return False.
   - Otherwise, establish the mapping and mark the word as visited.
5. If all positions satisfy the mapping constraints, return True.

Time Complexity: O(n + k)
Reason: Splitting s takes O(k), where k is the length of s. The subsequent
traversal performs n average O(1) dictionary and set operations, where
n is the length of pattern.

Space Complexity: O(k)
Reason: The split operation creates a list of words, while the dictionary
and set store up to n distinct mappings and words.
"""



class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        word_mapping = {}

        s = s.split()
        
        if len(s)!=len(pattern):
            return False
            
        visited = set()

        for i in range(len(s)):

            if pattern[i] in word_mapping:

                if s[i] != word_mapping[pattern[i]]:
                    return False

            else:
                if s[i] in visited:
                    return False
                word_mapping[pattern[i]] = s[i]
                visited.add(s[i])

        return True
