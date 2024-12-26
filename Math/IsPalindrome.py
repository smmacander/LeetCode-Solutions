class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (but not 0 itself) are not palindromes
        if x < 0 or (x%10 == 0 and x != 0):
            return False

        # Reverse the scond half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Check if the original number is a palindrome
        # The number is a palindrome if the first half matches the reversed second half
        # For odd-length numbers, reversed_half // 10 removes the middle digit
        return x == reversed_half or x == reversed_half // 10
    
def test_isPalindrome():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        (121, True),       # Basic palindrome
        (-121, False),     # Negative number, not a palindrome
        (10, False),       # Ends in zero, not a palindrome
        (0, True),         # Single digit, always a palindrome
        (12321, True),     # Odd-length palindrome
        (123321, True),    # Even-length palindrome
        (1000021, False),  # Non-palindrome with a large number
        (2147447412, True),# Large positive palindrome
        (-2147447412, False), # Large negative number, not a palindrome
        (1234567899, False) # Large non-palindrome
    ]

    # Run test cases
    for i, (x, expected) in enumerate(test_cases):
        result = solution.isPalindrome(x)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_isPalindrome()