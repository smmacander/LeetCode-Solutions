class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sum_of_squares(num):
            return sum(int(digit) ** 2 for digit in str(num))
        
        seen = set()

        while n!= 1 and n not in seen:
            seen.add(n)
            n = sum_of_squares(n)

        return n == 1

def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        (1, True),            # Smallest happy number
        (19, True),           # Known happy number
        (2, False),           # Small number, not happy
        (7, True),            # Another small happy number
        (4, False),     # Large number that quickly cycles
        (100, True),          # Number with trailing zeros (happy)
        (999, False),         # Large three-digit number, leads to a cycle
        (100000000, True),    # Large happy number with trailing zeros
        (116, False),         # Known non-happy number that leads to a cycle
        (2147483647, False)   # Largest 32-bit integer, likely not happy
    ]

    for i, (n, expected) in enumerate(test_cases):
        #call the method
        output = solution.isHappy(n)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()