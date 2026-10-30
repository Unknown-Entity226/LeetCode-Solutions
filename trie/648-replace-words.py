"""
Problem Description:
Given a dictionary of root words and a sentence, replace every
derivative in the sentence with the shortest root that forms it.
If no root matches a word, leave the word unchanged.

Approach:
- Implement a Trie using nested dictionaries.
- Insert every dictionary root into the Trie.
- Mark the end of each root using a termination character '#'.
- Traverse each sentence word character by character.
- Stop as soon as a termination marker is encountered, ensuring
  the shortest matching root is returned.
- If no root is found, retain the original word.
- Join the processed words with spaces and return the sentence.

Time Complexity:
O(D + S)

Reason:
- D represents the total number of characters across all dictionary
  roots. Insertion takes O(D).
- S represents the total number of characters across all sentence
  words. Searching takes O(S).
- Joining the resulting words takes O(S) time.
- Therefore, total complexity is O(D + S).

Space Complexity:
O(D + S)

Reason:
- The Trie requires O(D) space in the worst case.
- The words list and resulting sentence list require O(S) space.
"""
class Solution:

    def __init__(self):
        self.root = {}
        self.terminate = "#"


    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node:
                node[ch] ={}

            node = node[ch]

        node[self.terminate] = True


    def search(self, word):
        node = self.root
        prefix = []

        for ch in word:
            if self.terminate in node:
                return "".join(prefix)

            if ch not in node:
                return ""

            prefix.append(ch)
            node = node[ch]

        if self.terminate in node:
            return "".join(prefix)

        return ""

    def replaceWords(self, dictionary: list[str], sentence: str) -> str:

        for word in dictionary:
            self.insert(word)

        words = sentence.split()

        new_sen = []

        for word in words:
            prefix = self.search(word)
            if prefix == "":
                new_sen.append(word)

            else:
                new_sen.append(prefix)

            new_sen.append(" ")

        return "".join(new_sen).strip()
