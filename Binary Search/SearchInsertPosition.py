from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

def test_searchInsert():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        ([1,3,5,6],5,2),
        ([1,3,5,6],2,1),
        ([1,3,5,6],7,4),
        ([1, 3, 5, 6], 0, 0),
        ([2], 2, 0),
        ([2], 1, 0),
        ([2], 3, 1),
        ([-104], -105, 0),
        ([i for i in range(1, 10001)], 5001.5, 5001),
        ([-104, 0, 104], 0, 1)
    ]

    # Run test cases
    for i, (nums, target, expected) in enumerate(test_cases):
        result = solution.searchInsert(nums, target)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_searchInsert()