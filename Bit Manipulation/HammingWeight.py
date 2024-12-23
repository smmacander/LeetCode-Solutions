class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Calculate the number of set bits in the binary representation of n.

        :param n: A positive integer
        :return: The Hamming weight of n
        """
        count = 0
        while n > 0:
            count += n & 1 # Increment count if the last bit is 1
            n >>= 1        # Shift bits of n to the right
        return count

def test_hammingWeight():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        (11, 3),
        (128, 1),
        (2147483645, 30),
        (1, 1),
        (2, 1),
        (3, 2),
        (255, 8),
        (1024, 1),
        (2147483647, 31),
        (0b101010101010101010101010101010, 15),
        (0b111000111000111000111000111000, 15),
        (0b1000000000000000000000000000001, 2),
        (0,0)
    ]

    # Run test cases
    for i, (n, expected) in enumerate(test_cases):
        result = solution.hammingWeight(n)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_hammingWeight()