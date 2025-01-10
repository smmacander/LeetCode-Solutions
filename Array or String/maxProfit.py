from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            # If the price is higher than the previous day's price, add the difference
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
    
def test_maxProfit():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        # Simple case with one profitable transaction
        ([7, 1, 5, 3, 6, 4], 7),
    
        # Case with monotonically increasing prices
        ([1, 2, 3, 4, 5], 4),

        ([7, 6, 4, 3, 1], 0),
    
        # Case with monotonically decreasing prices
        ([5, 4, 3, 2, 1], 0),
    
        # Case with all prices the same
        ([3, 3, 3, 3, 3], 0),
    
        # Case with alternating ups and downs
        ([1, 2, 1, 2, 1, 2, 1], 3),
    
        # Single-day prices
        ([7], 0),
    
        # Two-day prices with profit
        ([1, 5], 4),
    
        # Two-day prices with no profit
        ([5, 1], 0),
    
        # Large input with alternating ups and downs
        ([i % 2 * 1000 for i in range(3 * 10**4)], 3 * 10**4 // 2 * 1000),
    
        # Large input with monotonically increasing prices
        (list(range(3 * 10**4)), 3 * 10**4 - 1)
    ]

    # Run test cases
    for i, (prices, expected) in enumerate(test_cases):
        # Call the maxProfit function
        result = solution.maxProfit(prices)
        
        # Validate the elements
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        
        # If no assertion fails
        print(f"Test case {i+1} passed.")

# Run tests
test_maxProfit()