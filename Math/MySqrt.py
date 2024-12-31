class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x # The square root of 0 or 1 is the number itself.

        left, right = 0, x
        while left <= right: 
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
            
        return right # 'right' will be the largest number such that right^2 <= x

def test_mySqrt():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        (0, 0),        # Smallest input, square root of 0
        (1, 1),        # Square root of 1, smallest non-zero input
        (2, 1),        # Non-perfect square, rounding down
        (3, 1),        # Another non-perfect square
        (4, 2),        # Perfect square
        (8, 2),        # Non-perfect square, close to a perfect square
        (9, 3),        # Perfect square
        (15, 3),       # Non-perfect square, slightly below a perfect square
        (231 - 1, 15), # Non-perfect square near the upper limit (adjust for real root calculations)
        (2**31 - 1, 46340) # Largest possible value for x, maximum edge case
    ]


    # Run test cases
    for i, (x, expected) in enumerate(test_cases):
        result = solution.mySqrt(x)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_mySqrt()