class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #trimming any trailing spaces from the end, as these won't affect the length of the last word
        #splitting the string by spaces to isolate the words
        words = s.strip().split()
        #returning the length of the last word in the resulting list of words
        return len(words[-1])

def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (s, expected_result)
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("Fly to the moon", 4),
        ("This is Sparta! ", 7),
        ("Antidisestablishmentarianism", 28),
        (" word", 4),
        ("A", 1),
        ("I am a hero", 4),
        ("Endless spaces ", 6),
        ("Supercalifragilisticexpialidocious", 34),
        ("First Last", 4)
    ]

    for i, (s, expected) in enumerate(test_cases):
        #call the method
        output = solution.lengthOfLastWord(s)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()