class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Boyer–Moore majority vote algorithm
        #the current candidate for majority element
        candidate = 0
        #how many times the current candidate has been encountered
        count = 0

        #iterate through the array
        for i in range(0, len(nums)):
            #if the count is zero, update the candidate to the current element
            if count == 0:
                candidate = nums[i]
            #if the current element is the same as the candidate, increase count
            if nums[i] == candidate:
                count += 1
            #if it's different, decrease count
            else:
                count -= 1
        #at the end of the loop, the candidate will be the majority element
        return candidate

def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (nums1, m, nums2, n, expected_result)
        ([3,2,3], 3),
        ([2,2,1,1,1,2,2], 2),
        ([3, 2, 3], 3),
        ([1, 1, 1, 1, 1], 1),
        ([-1, -1, -1, 2, 2], -1),
        ([7, -2, 7, 7, -2, 7, 7], 7),
        ([10], 10),
        ([4, 5, 6, 6, 6], 6),
        ([8, 8, 9, 8, 8], 8),
        ([5, 5, 6, 6, 5, 6, 5], 5),
        ([109, 109, 109, 109, -109, -109, 109], 109),
        ([-109, -109, -109, 100, 100, -109], -109)
    ]

    for i, (nums, expected) in enumerate(test_cases):
        #call the merge method
        output = solution.majorityElement(nums)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()