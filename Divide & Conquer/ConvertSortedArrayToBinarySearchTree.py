from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Helper function for recursion
        def helper (left, right):
            if left > right: # Base case: no elements to form a subtree
                return None
            
            # Choose the middle element as the root
            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            # Recursively build the left and right subtrees
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(nums) - 1)
    
def serialize(root):
    """Converts a binary tree to a list (level-order traversal)."""
    if not root:
        return []
    
    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values to match expected output format
    while result and result[-1] is None:
        result.pop()

    return result

def test_sortedArraytoBST():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        ([1,3], [1,None,3]),
        # Single element (minimum size)
        ([0], [0]),
    
        # Two elements (minimum to have imbalance)
        ([-10, -3], [-10, None, -3]),
    
        # Three elements (perfectly balanced)
        ([0, 1, 2], [1, 0, 2]),
    
        # Larger odd-sized array
        ([-10, -3, 0, 5, 9], [0, -10, 5, None, -3, None, 9]),
    
        # Larger even-sized array
        ([-10, -5, 0, 5, 10, 15], [0, -10, 10, None, -5, 5, 15]),
    
        # Negative numbers only
        ([-15, -10, -5, -3, -2], [-5, -15, -3, None, -10, None, -2]),
    
        # Positive numbers only
        ([1, 2, 3, 4, 5], [3, 1, 4, None, 2, None, 5]),
    
        # All numbers spaced far apart
        ([-10000, -5000, 0, 5000, 10000], [0, -10000, 5000, None, -5000, None, 10000]),
    
        # Large input (upper constraint boundary)
        (list(range(-50, 50)), [-1, -26, 24, -39, -14, 11, 37, -45, -33, -20, -8, 5, 17, 30, 43, -48, -42, -36, -30, -23, -17, -11, 
-5, 2, 8, 14, 20, 27, 33, 40, 46, -50, -47, -44, -41, -38, -35, -32, -28, -25, -22, -19, -16, -13, -10, -7, -3, 0, 3, 6, 9, 12, 15, 18, 22, 25, 28, 31, 35, 38, 41, 44, 48, None, -49, None, -46, None, -43, None, -40, None, -37, None, -34, None, -31, -29, -27, None, -24, None, -21, None, -18, None, -15, None, -12, None, -9, None, -6, -4, -2, None, 1, None, 4, None, 7, None, 10, None, 13, None, 16, None, 19, 21, 23, None, 
26, None, 29, None, 32, 34, 36, None, 39, None, 42, None, 45, 47, 49]),
    
        # Small input with far apart extremes
        ([-10000, 0, 10000], [0, -10000, 10000])
    ]

    # Run test cases
    for i, (nums, expected) in enumerate(test_cases):
        root = solution.sortedArrayToBST(nums)
        result = serialize(root)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_sortedArraytoBST()