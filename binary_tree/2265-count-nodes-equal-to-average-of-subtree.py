"""
Problem Description:
Given the root of a binary tree, count the nodes whose value is equal
to the floor of the average of all values in their subtree.

Approach:
- Perform a postorder DFS traversal so that the sum and number of nodes
  in both child subtrees are known before processing the current node.
- For each node, calculate:
    subtree_sum = left_sum + right_sum + node_value
    subtree_count = left_count + right_count + 1
- Compute the floor average using integer division.
- If the average equals the current node's value, increment the answer.
- Return the subtree sum and subtree node count to the parent.

Time Complexity:
O(n)

Reason:
- Every node is visited exactly once.
- All operations performed for each node take O(1) time.

Space Complexity:
O(h)

Reason:
- The recursion stack can contain at most h nodes, where h is the
  height of the tree.
"""

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        count =[0]

        def postOrder(root):

            if not root:
                return (0, 0)

            left = postOrder(root.left)
            right = postOrder(root.right)

            nodeSum = left[0]+right[0] + root.val
            nodeCount = left[1]+right[1] +1

            avg = nodeSum//nodeCount


            if avg == root.val:
                count[0]+=1

            return (nodeSum,nodeCount)

        postOrder(root)

        return count[0]
