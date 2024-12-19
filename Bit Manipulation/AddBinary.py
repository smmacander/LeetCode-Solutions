class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integerts, add them, then conver the result back to binary
        return bin(int(a, 2) + int(b, 2))[2:]

def test_addBinary():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        ("1010","1011","10101"),
        # Simple cases
        ("1", "1", "10"),              # Smallest binary strings
        ("11", "1", "100"),            # Carry over

        # Different lengths
        ("101", "10", "111"),          # Different lengths, no carry
        ("1001", "11", "1100"),        # Different lengths, carry over

        # Edge cases
        ("0", "0", "0"),               # Both are zero
        ("1", "0", "1"),               # One is zero
        ("0", "1", "1"),               # Other is zero

        # Long strings
        ("1" * 104, "1", "1" + "0" * 104), # Maximum length, small addition
        ("1" * 104, "1" * 104, "1" * 104 + "0"), # Maximum length, full addition

        # Uneven large inputs
        ("1" * 100, "1" * 50, "1" + "0" * 50 + "1" * 49 + "0") # Uneven lengths with large inputs
    ]

    # Run test cases
    for i, (a, b, expected) in enumerate(test_cases):
        result = solution.addBinary(a, b)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_addBinary()