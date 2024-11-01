from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)

def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        # Basic positive case, straightforward anagram
        ("anagram", "nagaram", True),
    
        # Basic negative case, different letters
        ("hello", "world", False),
    
        # Edge case: both strings are empty
        ("", "", True),
    
        # Edge case: one empty string, one non-empty string
        ("a", "", False),
    
        # Edge case: single character, same character
        ("a", "a", True),
    
        # Edge case: single character, different character
        ("a", "b", False),
    
        # Long anagram case
        ("a" * 50000 + "b" * 50000, "b" * 50000 + "a" * 50000, True),

        # Long non-anagram case, slightly different counts
        ("a" * 50000 + "b" * 49999, "b" * 50000 + "a" * 50000, False),

        # Anagram with repeated characters
        ("listen", "silent", True),

        # Non-anagram with same character counts but different characters
        ("abcd", "abce", False)
    ]

    for i, (s, t, expected) in enumerate(test_cases):
        #call the method
        output = solution.isAnagram(s, t)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()