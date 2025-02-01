class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV",
            1: "I"
        }

        result = []
        for value, symbol in roman_numerals.items():
            while num >= value:
                result.append(symbol)
                num -= value

        return "".join(result)
    
def test_intToRoman():
    # Create an instance of Solution
    solution = Solution()

    # Define test cases
    test_cases = [
        (3749, "MMMDCCXLIX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (1, "I"),          # Smallest number  
        (4, "IV"),         # Subtractive form (4)  
        (9, "IX"),         # Subtractive form (9)  
        (40, "XL"),        # Subtractive form (40)  
        (90, "XC"),        # Subtractive form (90)  
        (400, "CD"),       # Subtractive form (400)  
        (900, "CM"),       # Subtractive form (900)  
        (3999, "MMMCMXCIX"), # Largest number in range  
        (2888, "MMDCCCLXXXVIII") # Mixed symbols with max consecutive repetitions
    ]

    # Run test cases
    for i, (num, expected) in enumerate(test_cases):
        # Call the intToRoman function
        result = solution.intToRoman(num)
        
        # Validate the elements
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        
        # If no assertion fails
        print(f"Test case {i+1} passed.")

# Run tests
test_intToRoman()