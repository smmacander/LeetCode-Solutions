# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)

def test_maxDepth():
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
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1,None,2], 2),
        ([], 0),                               # Empty tree
        ([1], 1),                              # Single node
        ([1, 2, 3, 4, 5, 6, 7], 3),            # Complete binary tree
        ([1, 2, None, 3, None, 4, None], 4),   # Skewed tree (left-heavy)
        ([1, None, 2, None, 3, None, 4], 4),   # Skewed tree (right-heavy)
        ([1, 2, 3, 4, None, None, 5, 6], 4),   # Tree with varying depths
        ([i for i in range(1, 10001)], 14),    # Large tree (e.g., depth ~14 for 10^4 nodes)
        ([0, -10, 10, -20, None, None, 20], 3) # Tree with negative and zero node values
    ]

    # Run test cases
    for i, (values, expected) in enumerate(test_cases):
        root = build_tree_from_list(values)
        result = solution.maxDepth(root)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_maxDepth()