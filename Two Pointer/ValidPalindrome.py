class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert to lowercase and filter out non-alphanumeric characters
        filtered_s = ''.join(char.lower() for char in s if char.isalnum())
        # Check if the filtered string is the same forward and backward
        return filtered_s == filtered_s[::-1]

def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (s, expected_result)
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True),
        ("a", True),
        ("No 'x' in Nixon", True),
        ("12321", True),
        ("123456", False),
        ("Was it a car or a cat I saw?", True),
        ("Able was I ere I saw Elba", True),
        ("This is not a palindrome", False)
    ]

    for i, (s, expected) in enumerate(test_cases):
        #call the method
        output = solution.isPalindrome(s)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()