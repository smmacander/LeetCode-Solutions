class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #use one pointer to track the position of unique elements
        i = 0
        #use another pointer to iterate through the array and compare each element with the original one
        j = 1

        for j in range(1, len(nums)):
            #whenever you encounter a new unique element, increment i and replaces nums[i] with the new unique element
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        #return i+1 as the number of unique elements (k)
        return i + 1
    
def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (nums, val, expected_result)
        ([1,1,2], [1,2]),
        ([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4]),
        ([1], [1]),
        ([2, 2, 2, 2, 2], [2]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 1, 2, 2, 3, 3], [1, 2, 3]),
        ([-100, -50, 0, 50, 100], [-100, -50, 0, 50, 100]),
        ([-3, -2, -2, -1], [-3, -2, -1]),
        ([1, 2, 3, 4, 4], [1, 2, 3, 4]),
        ([0, 0, 1, 2, 2, 3, 4, 4, 5], [0, 1, 2, 3, 4, 5]),
        ([-100, -100, -100], [-100]),
        ([i//2 for i in range(2, 30002)], list(range(1, 15001)))
    ]

    for i, (nums, expected) in enumerate(test_cases):
        #make a copy of nums1 to modify
        nums_copy = nums[:]
        #call the merge method
        k = solution.removeDuplicates(nums_copy)

        if k == len(expected) and nums_copy[:k] == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {nums_copy[:k]}")

#run the tests
run_tests()