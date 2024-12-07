from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def in_order_traversal(node):
            nonlocal prev, min_diff
            if not node:
                return
            # Traverse the left subtree
            in_order_traversal(node.left)
            # Update min_diff using the current and previous node values
            if prev is not None:
                min_diff = abs(min(min_diff, node.val - prev))
            prev = node.val
            in_order_traversal(node.right)
        
        prev = None
        min_diff = float('inf')
        in_order_traversal(root)
        return min_diff
    
def test_getMinimumDifference():
    def build_tree_from_list(values):
        """Helper function to build a binary tree from a level-order list."""
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        # Basic case: small BST with minimum difference = 1
        (([4, 2, 6, 1, 3], 1)),  
    
        # Edge case: minimum difference between very close values
        (([1, 0, 48, None, None, 12, 49], 1)),  
    
        # Large BST with large gaps between some values
        (([1000, 500, 1500, 250, 750, 1250, 1750], 250)),  
    
        # Two nodes only: difference equals the absolute difference of the two values
        (([10, 20], 10)),  
    
        # BST with duplicate values (though duplicates are rare in BSTs)
        (([2, 2, 2], 0)),  
    
        # Dense BST with values spaced closely
        (([15, 10, 20, 8, 12, 17, 25], 2)),  
    
        # Linear BST (effectively a linked list): small differences between consecutive nodes
        (([1, None, 2, None, 3, None, 4], 1)),  
    
        # BST with maximum constraints (node values near the upper limit)
        (([105000, 104999, None], 1)),  
    
        # BST with minimum constraints (small node values)
        (([0, 0, None], 0)),  
    
        # BST with larger number of nodes (represents a balanced tree)
        (([50, 30, 70, 20, 40, 60, 80], 10))
    ]

    # Run test cases
    for i, (root, expected) in enumerate(test_cases):
        tree = build_tree_from_list(root)
        result = solution.getMinimumDifference(tree)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_getMinimumDifference()