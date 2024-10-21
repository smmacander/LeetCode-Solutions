class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #initialize min_price to a large value (e.g., 10^5)
        min_price = 100000
        #initialize max_profit to 0
        max_profit = 0
        #iterate through the prices array
        for price in prices:
            #update min_price to the minimum of the current min_price and the current price
            min_price = min(min_price, price)
            #calculate the profit if you sell at the current price
            current_profit = price - min_price
            #update max_profit to the maximum of the current max_profit and the calculated profit
            max_profit = max(current_profit, max_profit)

        #at the end, return max_profit
        return max_profit
    
def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        #Each test case is a tuple of (prices, expected_result)
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([7, 1, 5, 3, 6, 4], 5),
        ([9, 8, 7, 6, 5, 4], 0),
        ([1, 2, 3, 4, 5, 6], 5),
        ([4, 4, 4, 4, 4], 0),
        ([10], 0),
        ([0, 0, 0, 0], 0),
        ([10, 2, 11, 3, 9, 15], 13),
        ([5, 3, 8, 2, 10, 1, 12], 11),
        ([3, 7, 2, 8, 1], 6),
        ([100, 104, 102, 103], 4)
    ]

    for i, (nums, expected) in enumerate(test_cases):
        #call the method
        output = solution.maxProfit(nums)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()