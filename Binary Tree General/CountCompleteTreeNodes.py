# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Helper function to compute tree height
        def compute_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        if not root:
            return 0

        left_height = compute_height(root.left)
        right_height = compute_height(root.right)

        if left_height == right_height:
            # Left subtree is full
            return (1 << left_height) + self.countNodes(root.right) # 2^left_height + right subtree count
        else:
            # Right subtree is full
            return (1 << right_height) + self.countNodes(root.left) # 2^right_height + left subtree count
        
def test_countCompleteTreeNodes():
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
        ([1, 2, 3, 4, 5, 6], 6),
        ([], 0),
        ([1], 1),
        ([1, 2, 3, 4, 5, 6, 7], 7),
        ([0, 0, 0, 0, 0, 0, 0], 7),
        ([50000, 50000, 50000, 50000, 50000, 50000, 50000], 7),
        (list(range(1, 50001)), 50000),
        ([1, 2, 3, 4, 5], 5),
        ([1, 2, 3, None, None, 6, 7], 5),
        ([1, 2, 3, 4], 4)
    ]


    # Run test cases
    for i, (root, expected) in enumerate(test_cases):
        tree = build_tree_from_list(root)
        result = solution.countNodes(tree)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_countCompleteTreeNodes()