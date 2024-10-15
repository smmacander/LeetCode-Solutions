class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #use a variable k to count how many elements are not equal to k
        k = 0

        #iterate through the array
        for i in range(len(nums)):
            #for each element that is not equal to val
            if nums[i] != val:
                #move it to the front of the array at index k
                nums[k] = nums[i]
                #increment k
                k += 1
        
        #return k at the end, which will represent the number of elements in nums that are not equal to val.
        return k
    
def sort_first_k_elements(arr, k):
    # Sort the first k elements
    sorted_part = sorted(arr[:k])
    
    # Combine the sorted part with the remaining unsorted part of the array
    return sorted_part + arr[k:]
    
def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (nums, val, expected_result)
        ([3, 2, 2, 3], 3, [2,2]),
        ([0,1,2,2,3,0,4,2], 2, [0,1,4,0,3]),
        ([10, 20, 10, 30], 10, [20, 30]),
        ([], 5, []),
        ([12, 25, 37, 49], 100, [12, 25, 37, 49]),
        ([15, 15, 15, 15], 15, []),
        ([3, 5, 3, 7, 3], 3, [5, 7]),
        ([10, 20, 30, 40, 50], 50, [10, 20, 30, 40]),
        ([8], 8, []),
        ([7], 5, [7]),
        ([0, 1, 0, 2, 0], 0, [1, 2]),
        ([50, 50, 25, 50, 10], 50, [25, 10])
    ]

    for i, (nums, val, expected) in enumerate(test_cases):
        #make a copy of nums1 to modify
        nums_copy = nums[:]
        #call the merge method
        k = solution.removeElement(nums_copy, val)

        #compare the result with the expected output
        nums_copy = sort_first_k_elements(nums_copy, k)
        expected = sort_first_k_elements(expected, len(expected))

        if k == len(expected) and nums_copy[:k] == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {nums_copy[:k]}")

#run the tests
run_tests()