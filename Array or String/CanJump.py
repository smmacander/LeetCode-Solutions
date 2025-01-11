from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0 # Tracks the farthest index we can reach
        n = len(nums)

        for i in range(n):
            if i > max_reachable:
                return False # If we can't reach index i, return False
            max_reachable = max(max_reachable, i + nums[i]) # Update the farthest reachable index
            if max_reachable >= n - 1:
                return True # If we can reach of exceed the last index, return True

        return max_reachable >= n - 1 # Final check if the last index is reachable
    
def test_canJump():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        # Basic case: can jump to the end
        ([2, 3, 1, 1, 4], True),
    
        # Basic case: cannot jump to the end due to a zero
        ([3, 2, 1, 0, 4], False),
    
        # Single element (trivially true)
        ([0], True),
    
        # Large array of all zeros (cannot progress)
        ([0] * 10000, False),
    
        # Large array, all maximum values (can always reach the end)
        ([10**5] * 10000, True),
    
        # All 1s, should always be able to reach the end
        ([1] * 10000, True),
    
        # Zeros at the end make it impossible to reach the last index
        ([4, 2, 0, 0, 0, 1], False),
    
        # Jump exactly to the last index
        ([1, 2, 3, 4, 0, 0, 0, 1], True),
    
        # Case with alternating large and small values
        ([5, 0, 4, 0, 3, 0, 2, 0, 1, 0], True),
    
        # Case with the first jump insufficient to proceed
        ([1, 0, 2, 3], False),
    ]

    # Run test cases
    for i, (nums, expected) in enumerate(test_cases):
        # Call the canJump function
        result = solution.canJump(nums)
        
        # Validate the elements
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        
        # If no assertion fails
        print(f"Test case {i+1} passed.")

# Run tests
test_canJump()