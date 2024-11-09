class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        #mapping of closing to opening brackets
        bracket_map = {')':'(', '}':'{',']':'['}

        for char in s:
            if char in bracket_map:
                #pop the top element if stack is not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                #check if the mapping for the closing bracket matches the top element
                if bracket_map[char] != top_element:
                    return False
            else:
                #push the opening bracket onto the stack
                stack.append(char)

        #if the stack is empty, all brackets were matched
        return not stack
    
def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (s, expected_result)
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),                   # Correct types but incorrect nesting
        ("{[]}", True),                    # Nested brackets of different types
        ("", True),                        # Edge case: empty string (no brackets to match)
        ("(((((((((((((((((((())))))))))))))))))))", True),  # Edge case with maximum nesting depth
        ("(((())))([]){[]}", True),        # Mixed nesting with multiple valid patterns
        ("({[({[({[({[]})]})]})]})", True), # Deep nesting with different bracket types
        ("((({{{[[[}}}]]])))", False),     # Invalid sequence with incorrect ordering
    ]

    for i, (s, expected) in enumerate(test_cases):
        #call the method
        output = solution.isValid(s)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()