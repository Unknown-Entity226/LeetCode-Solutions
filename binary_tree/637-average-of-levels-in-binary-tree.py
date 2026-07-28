"""
Problem Description:
Given the root of a binary tree, return the average
value of the nodes on each level.

Approach:
- Perform a level order traversal using BFS.
- Use a NULL marker to separate levels.
- Maintain the sum and count of nodes for each level.
- Compute the average when a level ends and store it.
- Repeat until all levels are processed.

Time Complexity:
O(n)

Reason:
- Every node is visited exactly once.
- Each node is added to and removed from the queue once.

Space Complexity:
O(n)

Reason:
- The queue may store an entire level of the tree.
- The answer stores one average per level.
"""
