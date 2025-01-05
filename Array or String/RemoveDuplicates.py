from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        write = 2 # Start from the third position
        for read in range(2, len(nums)):
            # If the current number is not equal to the number two positions back
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write
    
def test_removeDuplicates():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        # Test Case 1: Typical case with repeated elements
        ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3]),
    
        # Test Case 2: No duplicates
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    
        # Test Case 3: All elements are the same
        ([5, 5, 5, 5, 5], [5, 5]),
    
        # Test Case 4: Two unique elements, both repeated multiple times
        ([1, 1, 1, 1, 2, 2, 2, 2], [1, 1, 2, 2]),
    
        # Test Case 5: Array length is 1 (minimum length constraint)
        ([42], [42]),
    
        # Test Case 6: Array of length 2 with identical elements
        ([6, 6], [6, 6]),
    
        # Test Case 7: Alternating pattern of numbers
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]),
    
        # Test Case 8: Long array with multiple duplicates
        ([1] * 10000 + [2] * 10000 + [3] * 10000, [1, 1, 2, 2, 3, 3]),
    
        # Test Case 9: All elements are distinct and in ascending order
        (list(range(-10000, 10001)), list(range(-10000, 10001))),
    
        # Test Case 10: Large array where each number appears exactly twice
        ([-10000, -10000] + [-9999, -9999] + [-9998, -9998], [-10000, -10000, -9999, -9999, -9998, -9998]),
        ([0,0,1,1,1,1,2,3,3], [0,0,1,1,2,3,3])
    ]


    # Run test cases
    for i, (nums, expected) in enumerate(test_cases):
        # Call the removeDuplicates function
        k = solution.removeDuplicates(nums)
        
        # Validate the length
        assert k == len(expected), f"Test case {i+1} failed: expected length {len(expected)}, got {k}"
        
        # Validate the elements
        for j in range(k):
            assert nums[j] == expected[j], f"Test case {i+1} failed at index {j}: expected {expected[j]}, got {nums[j]}"
        
        # If no assertion fails
        print(f"Test case {i+1} passed.")

# Run tests
test_removeDuplicates()