# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        
        if not root: # base case: if the node is None
            return False

        # check if the current node is a leaf and its value equals the remaining targetSum
        if not root.left and not root.right and root.val == targetSum:
            return True

        #recursively checck left and right subtrees with the updated targetSum
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

def test_pathSum():
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
        ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22, True),
        ([1,2,3], 5, False),
        ([],0,False),
        ([5,4,8,11,None,13,4,7,2,None,None,None,1], 28, False),
        ([7], 7, True),
        ([7], 10, False),
        ([-2,None,-3], -5, True),
        ([-2,None,-3], -4, False),
        ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 1000, False),
        ([1,None,2,None,3,None,4,None,5], 15, True),
        ([0,0,0,0,0,0,0], 0, True)    
    ]


    # Run test cases
    for i, (root, targetSum, expected) in enumerate(test_cases):
        tree = build_tree_from_list(root)
        result = solution.hasPathSum(tree, targetSum)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_pathSum()