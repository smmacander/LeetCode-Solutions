# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        #helper function to compare two subtrees
        def isMirror(t1, t2):
            if not t1 and not t2: #both nodes are null
                return True
            if not t1 or not t2:
                return False
            return (
                t1.val == t2.val and #values are equal
                isMirror(t1.left, t2.right) and #left of t1 matches right of t2
                isMirror(t1.right, t2.left) #right of t1 matches left of t2
            )

        #an empty tree is symmetric
        if not root:
            return True

        #compare left and right subtrees of the root
        return isMirror(root.left, root.right)

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

    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        # Test 1: Simple symmetric tree
        ([1, 2, 2, 3, 4, 4, 3], True),
    
        # Test 2: Simple asymmetric tree
        ([1, 2, 2, None, 3, None, 3], False),
    
        # Test 3: Single node tree (trivial symmetric case)
        ([1], True),
    
        # Test 4: Tree with all nodes null (trivial symmetric case)
        ([None], True),
    
        # Test 5: Larger symmetric tree
        ([1, 2, 2, 3, 4, 4, 3, 5, 6, 6, 5, None, None, None, None], False),
    
        # Test 6: Larger asymmetric tree with missing node
        ([1, 2, 2, 3, 4, None, 3], False),
    
        # Test 7: Tree with negative values, symmetric
        ([1, -2, -2, -3, -4, -4, -3], True),
    
        # Test 8: Tree with one subtree being larger
        ([1, 2, 2, 3, None, None, 3, None, 4], False),
    
        # Test 9: Tree with all nodes having the same value, symmetric
        ([1, 1, 1, 1, 1, 1, 1], True),
    
        # Test 10: Tree with multiple levels and asymmetric
        ([1, 2, 2, 3, 4, 4, 3, 5, None, None, 5, None, None, 6, 6], False),
    ]


    # Run test cases
    for i, (root, expected) in enumerate(test_cases):
        tree = build_tree_from_list(root)
        result = solution.isSymmetric(tree)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_invertBinaryTree()