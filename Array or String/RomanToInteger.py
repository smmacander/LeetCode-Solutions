class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dictionary to map Roman symbols to their corresponding values
        roman_values = {
            'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000
        }
        total = 0
        prev_value = 0
        #traverse the string from the end to the beginning
        for char in reversed(s):
            current_value = roman_values[char]
            #subtract when necessary: if a smaller value appears before a larger one (like I before V or X), subtract the smaller value from the total instead of adding it
            if current_value < prev_value:
                total -= current_value
            #add all other values: if a symbol is greater than or equal to the one after it, simply add its value to the total 
            else:
                total += current_value
            prev_value = current_value
        return total

def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        ("MCMXCIV", 1994),
        ("I", 1),        # Smallest number possible
        ("III", 3),      # Simple addition of the same symbol
        ("IV", 4),       # Smallest subtraction case (I before V)
        ("IX", 9),       # Subtraction case (I before X)
        ("LVIII", 58),   # Mixed addition and subtraction
        ("XC", 90),      # Subtraction case (X before C)
        ("CXLIV", 144),  # Multiple subtraction cases
        ("DCCCXC", 890), # Complex case, mix of addition and subtraction
        ("MMMCMXCIX", 3999), # Largest number possible
        ("MMMDCCCLXXXVIII", 3888) # Largest addition-based number
    ]

    for i, (nums, expected) in enumerate(test_cases):
        #call the merge method
        output = solution.romanToInt(nums)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()