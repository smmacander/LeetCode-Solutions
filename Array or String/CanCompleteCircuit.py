from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)

        # If the total gas is less than total cost, there's no valid start
        if total_gas < total_cost:
            return -1

        start, tank = 0, 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            # If tank goes negative, reset start position
            if tank < 0:
                start = i + 1
                tank = 0

        return start
    
def test_canCompleteCircuit():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        ([1,2,3,4,5], [3,4,5,1,2], 3),
        ([2,3,4], [3,4,3], -1),

        # Minimum input size, start possible
        ([1], [1], 0),  

        # Minimum input size, start not possible
        ([0], [1], -1),  

        # Large values, exactly enough gas to complete circuit
        ([10000, 10000, 10000], [9999, 9999, 10002], 0),  

        # Large values, total gas < total cost (impossible case)
        ([10000, 10000, 10000], [10001, 10000, 10000], -1),  

        # Cycle with alternating gain and loss
        ([3, 1, 4, 5, 2], [2, 2, 3, 6, 1], 0),  

        # All gas stations have 0 gas
        ([0, 0, 0, 0, 0], [1, 2, 3, 4, 5], -1),  

        # All gas stations have excess gas
        ([5, 5, 5, 5, 5], [1, 1, 1, 1, 1], 0),  

        # Only one station has enough gas to start
        ([1, 2, 3, 50, 1], [10, 2, 3, 10, 1], 1),  

        # Large n case with a feasible start
        ([1] * 100000, [1] * 99999 + [0], 0)
    ]

    # Run test cases
    for i, (gas, cost, expected) in enumerate(test_cases):
        # Call the productExceptSelf function
        result = solution.canCompleteCircuit(gas, cost)
        
        # Validate the elements
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        
        # If no assertion fails
        print(f"Test case {i+1} passed.")

# Run tests
test_canCompleteCircuit()