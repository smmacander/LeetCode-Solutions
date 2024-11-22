# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        #base case: if both nodes are None, they are the same
        if not p and not q:
            return True

        #if one of them is None or their values differ, they are not the same
        if not p or not q or p.val != q.val:
            return False
        
        #recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
def test_sameTree():
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
        ([1,2,3],[1,2,3], True),
        ([1,2], [1,None,2], False),
        ([1,2,1], [1,1,2], False),
        ([1],[1],True),
        ([],[1],False),
        ([],[],True),
        ([1,2,3],[1,2,4],False),
        ([1,2,None],[1,None,2],False),
        ([1, 2, 3, None, None, 4, 5], [1, 2, 3, None, None, 4, 5], True),
        ([1, 2, 3, None, 4], [1, 2, 3, 4], False),
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], True),
        ([1, 2, None, 4, None], [1, None, 3, None, 5], False),
        ([-1, -2, -3], [-1, -2, -3], True)
    ]

    # Run test cases
    for i, (p, q, expected) in enumerate(test_cases):
        root_p = build_tree_from_list(p)
        root_q = build_tree_from_list(q)
        result = solution.isSameTree(root_p,root_q)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_sameTree()