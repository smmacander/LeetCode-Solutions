class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (haystack, needle, expected_result)
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("aaaaaa", "a", 0),
        ("aaaaaa", "b", -1),
        ("abc", "abcd", -1),
        ("abcdef", "abcdef", 0),
        ("abcdefgh", "xyz", -1),
        ("abcdabc", "dab", 3),
        ("abc", "", 0),
        ("abababab", "abab", 0)
    ]

    for i, (haystack, needle, expected) in enumerate(test_cases):
        #call the method
        output = solution.strStr(haystack, needle)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()