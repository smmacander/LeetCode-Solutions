class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by spaces, remove any extra spaces, and reverse the list of words
        words = s.split()
        return ' '.join(reversed(words))
    
def test_reverseWords():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        ("single", "single"),  # Single word case
        ("  multiple    spaces    between   words  ", "words between spaces multiple"),  # Excessive spaces
        ("Hello123 world456", "world456 Hello123"),  # Words with digits
        ("UPPER lower MiXeD", "MiXeD lower UPPER"),  # Case sensitivity
        ("123 456 789", "789 456 123"),  # Numbers only
        ("  spaced    out   ", "out spaced"),  # Edge case with only spaces between two words
        ("The quick brown fox jumps over the lazy dog", "dog lazy the over jumps fox brown quick The")  # Longer sentence
    ]

    # Run test cases
    for i, (s, expected) in enumerate(test_cases):
        # Call the reverseWords function
        result = solution.reverseWords(s)
        
        # Validate the elements
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        
        # If no assertion fails
        print(f"Test case {i+1} passed.")

# Run tests
test_reverseWords()