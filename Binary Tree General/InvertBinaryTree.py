# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        
        #swap the left and right subtrees
        root.left, root.right = root.right, root.left

        #recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

def test_invertBinaryTree():
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
    
    def tree_to_list(root):
        """Helper function to convert a binary tree to a level-order list."""
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing None values for comparison
        while result and result[-1] is None:
            result.pop()
        return result

    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, None, 3, None], [1, None, 2, None, 3]),
        ([1, None, 2, None, 3], [1, 2, None, 3]),  # Updated expected output
        ([4, 2, None, 1, None, None, None], [4, None, 2, None, 1]),
        ([1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]),
        ([-10, -20, 0, None, -15, None, 5], [-10, 0, -20, 5, None, -15]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, 3, 2, 7, 6, 5, 4, 15, 14, 13, 12, 11, 10, 9, 8])
    ]

    # Run test cases
    for i, (root, expected) in enumerate(test_cases):
        tree = build_tree_from_list(root)
        result_tree = solution.invertTree(tree)
        result_list = tree_to_list(result_tree)
        assert result_list == expected, f"Test case {i+1} failed: expected {expected}, got {result_list}"
        print(f"Test case {i+1} passed.")

# Run tests
test_invertBinaryTree()