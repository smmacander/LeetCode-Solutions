from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            # If the current digit is less than 9, increment and return the result
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Otherwise, set the current digit to 0 and move to the next
            digits[i] = 0

        # If we finish the loop, it means all digits were 9
        return [1] + digits
    
def test_plusOne():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        # Single-digit number increment
        ([1], [2]),  # Incrementing 1
        ([9], [1, 0]),  # Incrementing 9 (carry-over)

        # Multi-digit number with no carry-over
        ([1, 2, 3], [1, 2, 4]),  # Incrementing the last digit
        ([4, 3, 2, 1], [4, 3, 2, 2]),

        # Multi-digit number with carry-over
        ([1, 2, 9], [1, 3, 0]),  # Carry-over from the last digit
        ([9, 9, 9], [1, 0, 0, 0]),  # All digits carry over

        # Edge case: Maximum length array with no carry-over
        ([1] * 100, [1] * 99 + [2]),  # Increment the last digit of 100 ones

        # Edge case: Maximum length array with carry-over
        ([9] * 100, [1] + [0] * 100),  # All digits are nines

        # Incrementing a number with leading non-zero digits and trailing nines
        ([4, 5, 6, 9, 9], [4, 5, 7, 0, 0]),  # Carry-over affects only part of the number

        # Large number with scattered nines
        ([8, 9, 9, 9, 8, 9], [8, 9, 9, 9, 9, 0]),  # Carry-over skips some digits

        # Single-digit edge cases
        ([5], [6]),  # Incrementing a middle-range single digit
    ]



    # Run test cases
    for i, (digits, expected) in enumerate(test_cases):
        result = solution.plusOne(digits)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_plusOne()