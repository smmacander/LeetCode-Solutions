from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Step 1: Sort citations in descending order
        citations.sort(reverse=True)

        # Step 2: Calculate the h-index
        h = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h = i + 1
            else:
                break

        return h
    
def test_hIndex():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        ([3, 0, 6, 1, 5], 3),
        ([1,3,1], 1),
        ([0, 0, 0, 0, 0], 0),
        ([1000, 1000, 1000, 1000, 1000], 5),
        ([1, 1, 1, 1, 1], 1),
        ([10, 8, 5, 4, 3], 4),
        ([25, 8, 5, 3, 3, 3, 1], 3),
        ([0, 1, 2, 3, 4], 2),
        ([0], 0),
        ([1], 1),
        ([0, 5000] + [0] * 4998, 1)
    ]

    # Run test cases
    for i, (citations, expected) in enumerate(test_cases):
        # Call the hIndex function
        result = solution.hIndex(citations)
        
        # Validate the elements
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        
        # If no assertion fails
        print(f"Test case {i+1} passed.")

# Run tests
test_hIndex()