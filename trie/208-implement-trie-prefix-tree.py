"""
Problem Description:
Implement a Trie supporting insertion, exact word searching,
and prefix searching.

Approach:
- Represent each trie node using a nested dictionary.
- Traverse characters while inserting a word, creating missing
  nodes whenever necessary.
- Use '#' as an end-of-word marker in the final node.
- For search, traverse the word and check whether the final node
  contains the termination marker.
- For startsWith, check whether all prefix characters exist
  in the trie.

Time Complexity:
O(L) per operation, where L is the length of the input string.

Reason:
- Each character is processed exactly once.
- Dictionary lookups and insertions take O(1) average time.
- Therefore, insert, search, and startsWith each take O(L).

Space Complexity:
O(N * L) in the worst case.

Reason:
- N inserted words with maximum length L can create up to
  O(N * L) trie nodes.
- Each node is represented by a dictionary.
"""
class Trie:

    def __init__(self):
        self.root = {}
        self.terminate = "#"

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]

        node[self.terminate] = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node:
                return False

            node = node[ch]

        return self.terminate in node


    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            if ch not in node:
                return False

            node = node[ch]

        return True
