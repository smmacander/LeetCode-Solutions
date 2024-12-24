from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
    
def test_singleNumber():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        ([2, 2, 1], 1),
        ([4,1,2,1,2], 4),
        ([1], 1),
        ([-1, 2, 2], -1),
        ([30000, -30000, -30000], 30000),
        ([-30000, 5, 5], -30000),
        ([0, 7, 7], 0),
        ([3, 1, 3, 3, 3], 1),
        ([i for i in range(1, 15001) for _ in range(2)] + [15001], 15001),
        ([-4, 2, -4, -4, -4], 2),
        ([4, 5, 6, 4, 5, 6, 7], 7),
        ([8, 8, 8, 8, 9], 9),
    ]

    # Run test cases
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.singleNumber(nums)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_singleNumber()