class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<=1 # Shift result left by 1 to make space for the next bit
            result |= n & 1 # Add the least significant bit of 'n' to result
            n >>= 1 # Shift 'n' right by 1 to process the next bit
        return result

def test_reverseBits():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        (0b11111111111111111111111111111101, 0b10111111111111111111111111111111),
        (0b00000000000000000000000000000000, 0b00000000000000000000000000000000),  # All zeros
        (0b11111111111111111111111111111111, 0b11111111111111111111111111111111),  # All ones
        (0b00000000000000000000000000000001, 0b10000000000000000000000000000000),  # Single 1 at LSB
        (0b10000000000000000000000000000000, 0b00000000000000000000000000000001),  # Single 1 at MSB
        (0b11110000111100001111000011110000, 0b00001111000011110000111100001111),  # Alternating blocks
        (0b00001111000011110000111100001111, 0b11110000111100001111000011110000),  # Reverse of above
        (0b10101010101010101010101010101010, 0b01010101010101010101010101010101),  # Alternating bits
        (0b01010101010101010101010101010101, 0b10101010101010101010101010101010),  # Reverse of above
        (0b00000010100101000001111010011100, 0b00111001011110000010100101000000),  # Random pattern
        (0b10000000000000000000000000000001, 0b10000000000000000000000000000001),  # Palindrome binary
    ]

    # Run test cases
    for i, (n, expected) in enumerate(test_cases):
        result = solution.reverseBits(n)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_reverseBits()