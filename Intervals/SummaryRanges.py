class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        ranges = []
        start = 0 #track the start of the current range

        for i in range(len(nums)):
            #if we're at the last element or the current element is not consecutive with the next
            if i == len(nums) -1 or nums[i] + 1 != nums[i + 1]:
                #if start and current element are the same, it's a single element range
                if start == i:
                    ranges.append(str(nums[start]))
                else:
                    ranges.append("{}->{}".format(nums[start], nums[i]))
                #move start to the next element
                start = i + 1       
        
        return ranges

def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (nums, expected_result)
        ([0,1,2,4,5,7], ["0->2","4->5","7"]),
        ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"]),
        ([0, 1, 2, 3, 4], ["0->4"]),
        ([0, 2, 4, 6, 8], ["0", "2", "4", "6", "8"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
        ([-5, -4, -3, 2, 3, 4], ["-5->-3", "2->4"]),
        ([5], ["5"]),
        ([], []),
        ([2147483640, 2147483641, 2147483642, 2147483643, 2147483644], ["2147483640->2147483644"]),
        ([-10, -9, -8, -5, -3, -2, -1], ["-10->-8", "-5", "-3->-1"]),
        ([-2147483648, 2147483647], ["-2147483648", "2147483647"]),
        ([1, 3, 5, 7, 10, 11, 12, 15], ["1", "3", "5", "7", "10->12", "15"])
    ]

    for i, (nums, expected) in enumerate(test_cases):
        #call the method
        output = solution.summaryRanges(nums)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()