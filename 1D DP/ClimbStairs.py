class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev1, prev2 = 1, 2
        for _ in range (3, n + 1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current

        return prev2
    
def test_climbStairs():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        (1, 1),  # Smallest input, minimal staircase
        (2, 2),  # Base case with two steps
        (3, 3),  # Transition point from base case to recursion
        (4, 5),  # First non-trivial calculation
        (10, 89),  # Mid-range test
        (20, 10946),  # Larger input, testing performance
        (30, 1346269),  # Near upper limit
        (40, 165580141),  # High input value
        (45, 1836311903),  # Maximum allowed input
        (15, 987)  # Medium value to test consistency
    ]

    # Run test cases
    for i, (n, expected) in enumerate(test_cases):
        result = solution.climbStairs(n)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_climbStairs()