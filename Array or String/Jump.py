from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0 # Already at the last index

        # Initialize variables
        jumps = 0 # Count of jumps made
        current_end = 0 # End of the range covered by the current jump
        farthest = 0 # The farthest we can reach at any point

        for i in range(n - 1): # No need to check the last index
            farthest = max(farthest, i + nums[i]) # Update the farthest we can reach
            if i == current_end: # Time to make a jump
                jumps += 1
                current_end = farthest # Update the range covered by the jump
                if current_end >= n - 1: # If we can reach the end, break early
                    break
        
        return jumps
    
def test_jump():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        ([2,3,1,1,4], 2),
        ([2,3,0,1,4], 2),
        # Single element array
        ([0], 0),  # Already at the destination

        # Array where every jump is 1
        ([1, 1, 1, 1, 1], 4),  # Must jump 4 times to reach the end

        # Array with large jumps possible
        ([5, 4, 3, 2, 1, 0, 0], 2),

        # Long array with increasing jump range
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4),  # Optimal jumps increase coverage

        # Array with zero values in between
        ([3, 0, 0, 0, 1], 2),

        # Long array where jumps alternate between 1 and a large number
        ([1, 1000, 1, 1000, 1, 1000, 1], 2),  # Jump to every second large jump

        # Array with max jump range (1000)
        ([1000] + [0] * 999, 1),  # Single jump to the end

        # Array with a decreasing sequence
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 1),  # Start covers the whole array

        # Large array with alternating small and large jumps
        ([1, 100, 1, 100, 1, 100, 1, 100, 1], 2)  # Use large jumps to minimize steps
    ]

    # Run test cases
    for i, (nums, expected) in enumerate(test_cases):
        # Call the jump function
        result = solution.jump(nums)
        
        # Validate the elements
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        
        # If no assertion fails
        print(f"Test case {i+1} passed.")

# Run tests
test_jump()