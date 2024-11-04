class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #dictionary to store the number and its index
        num_to_index = {}

        #iterate over the list
        for i, num in enumerate(nums):
            #calculate the complement
            complement = target - num

            #check if the complement is in the dictionary
            if complement in num_to_index:
                #if found, return the indices
                return [num_to_index[complement], i]

            #otherwise, add the number to the dictionary
            num_to_index[num] = i

        #in case there's no solution (per problem statement, there shoulda lways be one)
        return None
    
def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (nums, target, expected_result)
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3,2,4], 6, [1,2]),
        ([3,3], 6, [0,1]),
        ([-1, 2, 3, 4], 5, [1, 2]),
        ([-3, 4, 3, 90], 0, [0, 2]),
        ([1, 2], 3, [0, 1]),
        ([109, -109, 5, 7], 0, [0, 1]),
        ([3, 3, 4, 5], 6, [0, 1]),
        ([2, 5, 11, 15], 7, [0, 1]),
        ([1, 2, 5, 9], 3, [0, 1]),
        ([-10, -60, -30, -40, -50], -70, [0, 1]),
        ([-109, 0, 109], 0, [0, 2])
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        #call the method
        output = solution.twoSum(nums, target)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()