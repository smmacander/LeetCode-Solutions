class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #create a dictionary to store the counts of each character in magazine
        magazine_counts = {}

        #count each character in magazine
        for char in magazine:
            magazine_counts[char] = magazine_counts.get(char, 0) + 1

        #check each character in ransomNote
        for char in ransomNote:
            #if the character is not in magazine or not enough occurrences are left, return False
            if magazine_counts.get(char, 0) == 0:
                return False
            #otherwise, decrease the count of the character in magazine_counts
            magazine_counts[char] -= 1
        
        #if we pass all checks, return True
        return True
    
def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        ("a", "b", False),             # Single letter in `ransomNote` not in `magazine`
        ("aa", "ab", False),           # Not enough occurrences of 'a' in `magazine`
        ("aa", "aab", True),           # Enough occurrences of 'a' to satisfy `ransomNote`
        ("a" * 10**5, "a" * 10**5, True),    # Maximum length case with all matching characters
        ("a" * 10**5, "b" * 10**5, False),   # Maximum length case with no matching characters
        ("abc", "aabbcc", True),       # `magazine` has enough occurrences for each letter in `ransomNote`
        ("abc", "aabbc", True),        # Corrected to True, enough occurrences for each letter
        ("xyz", "xyyzz", True),        # `magazine` contains enough occurrences for `ransomNote`
        ("xyz", "xyy", False),         # Not enough 'z' in `magazine`
        ("xyz" * 10**4, "x" * 10**4 + "y" * 10**4 + "z" * 10**4, True)  # Large case with exact letter counts
    ]

    for i, (ransomNote, magazine, expected) in enumerate(test_cases):
        #call the method
        output = solution.canConstruct(ransomNote, magazine)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()