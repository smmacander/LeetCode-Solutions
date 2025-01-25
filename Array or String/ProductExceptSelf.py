from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Calculate prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Calculate suffix products and combine
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
    
def test_productExceptSelf():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
        # Test case with zeros (product for the index with zero will be non-zero)
        ([0, 1, 2, 3], [6, 0, 0, 0]),

        # Test case with multiple zeros (all products will be zero)
        ([0, 1, 0, 3], [0, 0, 0, 0]),

        # Test case with negative numbers
        ([-1, 2, -3, 4], [-24, 12, -8, 6]),

        # Test case with all elements being the same
        ([5, 5, 5, 5], [125, 125, 125, 125]),

        # Test case with a mix of large positive and negative numbers
        ([10, -10, 5, -5], [250, -250, 500, -500]),

        # Test case with two elements
        ([3, 7], [7, 3]),

        # Test case with the smallest and largest values within the constraint
        ([-30, 30, -30, 30], [-27000, 27000, -27000, 27000]),

        # Test case with sequential numbers
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),

        # Test case with alternating signs
        ([1, -2, 3, -4, 5], [120, -60, 40, -30, 24])        
    ]

    # Run test cases
    for i, (nums, expected) in enumerate(test_cases):
        # Call the productExceptSelf function
        result = solution.productExceptSelf(nums)
        
        # Validate the elements
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        
        # If no assertion fails
        print(f"Test case {i+1} passed.")

# Run tests
test_productExceptSelf()