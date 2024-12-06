from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root:
            return []

        result = []
        queue = deque([root]) # Use deque for BFS

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range (level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate the average for the current level
            result.append(level_sum / level_size)

        return result
    
def test_averageOfLevels():
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
        ([3, 9, 20, None, None, 15, 7], [3.00000,14.50000,11.00000]),
        ([3, 9, 20, 15, 7], [3.00000,14.50000,11.00000]),
        
        # Test 3: Single-node tree (smallest tree possible)
        ([1], [1.00000]),

        # Test 4: Completely balanced binary tree
        ([1, 2, 3, 4, 5, 6, 7], [1.00000, 2.50000, 5.50000]),

        # Test 5: Tree with None as children (sparse tree)
        ([1, 2, 3, None, 5, None, 7], [1.00000, 2.50000, 6.00000]),

        # Test 6: Deep tree (linked list structure, unbalanced)
        ([1, 2, None, 3, None, 4, None], [1.00000, 2.00000, 3.00000, 4.00000]),

        # Test 7: Tree with very large and small values
        ([2**31 - 1, -2**31, 2**31 - 1], [(2**31 - 1) * 1.00000, -0.50000]),

        # Test 8: Tree with all negative values
        ([-10, -20, -30, -40, -50], [-10.00000, -25.00000, -45.00000]),

        # Test 9: Tree with mix of positive and negative values
        ([0, -3, 9, -10, None, 5, None], [0.00000, 3.00000, -2.50000]),

        # Test 10: Maximum possible nodes for a complete binary tree (e.g., height 3)
        ([i for i in range(1, 16)], [1.00000, 2.50000, 5.50000, 11.50000]),

        # Test 11: Tree with zero as all node values
        ([0, 0, 0, 0, 0, 0, 0], [0.00000, 0.00000, 0.00000]),

        # Test 12: Tree with two levels, with some missing children
        ([1, 2, 3, None, 4], [1.00000, 2.50000, 4.00000])

    ]


    # Run test cases
    for i, (root, expected) in enumerate(test_cases):
        tree = build_tree_from_list(root)
        result = solution.averageOfLevels(tree)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_averageOfLevels()