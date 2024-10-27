class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #initialize two pointers, one for each string
        i, j = 0, 0

        #loop while there are characters left in both strings
        while i < len (s) and j < len(t):
            #if characters match, move the pointer in s
            if s[i] == t[j]:
                i += 1
            #move the pointer in t
            j += 1
        
        #if i has reached the end of s, all characters in s are found in t in order
        return i == len(s)

def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (s, t, expected_result)
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("", "", True),
        ("a", "", False),
        ("", "ahbgdc", True),
        ("abc", "abc", True),
        ("ace", "abcdef", True),
        ("aec", "abcdef", False),
        ("longsubstringtest", "loontgrbsuscttingstest", False),
        ("abcdefghij", "a" * 10000, False)
    ]

    for i, (s, t, expected) in enumerate(test_cases):
        #call the method
        output = solution.isSubsequence(s, t)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()