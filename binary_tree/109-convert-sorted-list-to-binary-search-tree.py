"""
Problem Description:
Convert a sorted singly linked list into a height-balanced Binary Search Tree.

Approach:
- Find the middle node of the linked list using slow and fast pointers.
- Use the middle node as the root of the current BST.
- Disconnect the list before the middle node to form the left sublist.
- Recursively construct the left subtree from the left sublist.
- Recursively construct the right subtree from the nodes after the middle node.
- Continue until the list contains zero or one node.

Time Complexity:
O(n log n)

Reason:
- Finding the middle takes O(n) for each recursive level.
- The list is divided approximately in half at every level.
- Therefore, the total complexity is O(n log n).

Space Complexity:
O(log n)

Reason:
- The recursion depth is O(log n) because the resulting BST is height-balanced.
- No additional data structure proportional to n is used.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def find_mid(self, head):

        slow = head
        prev = None
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return slow, prev

    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        

        def treemake(head):

            if not head:
                return None
            if not head.next:
                return TreeNode(head.val)
                
            mid , prev= self.find_mid(head)
            
            if prev:
                prev.next = None

            root = TreeNode(mid.val)

            root.left = treemake(head)
            root.right = treemake(mid.next)
            return root

        return treemake(head)

    

        
