class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 #the last element of the original part of nums1
        j = n - 1 #the last element of nums2
        k = m + n - 1 #the last position in nums1, which is where the merged element will go

        #compare the elements of nums1[i] and nums2[j]
        #place the larger one at nums1[k] and move the respective pointer (i or j) and k backwards
        while i>= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k -= 1

        #if there are remaining elements in nums2 (i.e., j >= 0), copy them into nums1 (because nums1 already contains its sorted path)
        while j >= 0:
            nums1[k] = nums2[j]
            k-=1
            j-=1

def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (nums1, m, nums2, n, expected_result)
        ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
        ([1],1,[],0,[1]),
        ([0],0,[1],1,[1]),
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1, 2, 3], 3, [], 0, [1, 2, 3]),
        ([0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3]),
        ([1, 0], 1, [2], 1, [1, 2]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3, [1, 2, 3, 4, 5, 6]),
        ([2, 2, 3, 0, 0, 0], 3, [2, 2, 4], 3, [2, 2, 2, 2, 3, 4]),
        ([0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3]),
        ([2, 2, 2, 0, 0, 0], 3, [2, 2, 2], 3, [2, 2, 2, 2, 2, 2]),
        ([0], 0, [], 0, [0])
    ]

    for i, (nums1, m, nums2, n, expected) in enumerate(test_cases):
        #make a copy of nums1 to modify
        nums1_copy = nums1[:]
        #call the merge method
        solution.merge(nums1_copy, m, nums2, n)

        #compare the result with the expected output
        if nums1_copy == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {nums1_copy}")

#run the tests
run_tests()