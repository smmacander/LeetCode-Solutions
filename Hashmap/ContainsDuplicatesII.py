class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #dictionary to store the last seen index of each number
        num_indices = {}

        #iterate through the array
        for i, num in enumerate(nums):
            #check if the number is in the dictionary and within the distance k
            if num in num_indices and i - num_indices[num] <= k:
                return True
            #update the dictionary with the current index of the number
            num_indices[num] = i

        #no such pair found
        return False

def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (nums, k, expected_result)
        ([1,2,3,1], 3, True),
        ([1,0,1,1], 1, True),
        ([1,2,3,1,2,3], 2, False),
        # Case where duplicates exist but are out of range k
        ([1, 2, 3, 1], 2, False),

        # Edge case with minimum nums length and no duplicates
        ([1], 1, False),

        # Edge case with nums of length 2, duplicate within range
        ([1, 1], 1, True),

        # Large k value and no duplicates in the list
        ([1, 2, 3, 4, 5], 100000, False),

        # Large array with duplicate exactly k indices apart
        ([1] + [0] * 99998 + [1], 99999, True),

        # Large array with no duplicates, k is small
        (list(range(100000)), 1, False),

        # Case with all elements the same and k equals length - 1
        ([2] * 100000, 99999, True),

        # Negative numbers with duplicates within range k
        ([-1, -1, -2, -2], 1, True),

        # No duplicates, but mixed positive and negative numbers
        ([10, -10, 20, -20, 30], 3, False),
    ]

    for i, (nums, k, expected) in enumerate(test_cases):
        #call the method
        output = solution.containsNearbyDuplicate(nums, k)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()