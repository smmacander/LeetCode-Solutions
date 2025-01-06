from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n # Normalize k to be within the array length

        # Helper function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
        
        # Reverse the entire array
        reverse(0, n - 1)
        # Reverse the first k elements
        reverse(0, k - 1)
        # Reverse the rest
        reverse(k, n - 1)

def test_rotate():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        # Basic case
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1,-100,3,99], 2, [3,99,-1,-100]),
        
        # Single element array
        ([1], 0, [1]),  # k = 0
        ([1], 5, [1]),  # k > length

        # Two elements
        ([1, 2], 1, [2, 1]),  # k = 1
        ([1, 2], 2, [1, 2]),  # k = length
        ([1, 2], 3, [2, 1]),  # k > length

        # Array with duplicates
        ([1, 1, 1, 1], 2, [1, 1, 1, 1]),  # k = any value

        # Large array with small k
        (list(range(1, 11)), 1, [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]),

        # Large array with k = length
        (list(range(1, 101)), 100, list(range(1, 101))),  # Full rotation

        # Large array with k > length
        (list(range(1, 101)), 105, [96, 97, 98, 99, 100, 1, 2, 3, 4, 5]),

        # Edge case: k = 0
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),

        # Edge case: k = nums.length - 1
        ([1, 2, 3, 4, 5], 4, [2, 3, 4, 5, 1]),
    ]



    # Run test cases
    for i, (nums, k, expected) in enumerate(test_cases):
        # Call the removeDuplicates function
        solution.rotate(nums, k)
        
        # Validate the elements
        for j in range(len(expected)):
            assert nums[j] == expected[j], f"Test case {i+1} failed at index {j}: expected {expected[j]}, got {nums[j]}"
        
        # If no assertion fails
        print(f"Test case {i+1} passed.")

# Run tests
test_rotate()