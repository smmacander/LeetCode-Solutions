class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #use two dictionaries to track mappings from s to t and from t to s
        map_s_to_t = {}
        map_t_to_s = {}

        for char_s, char_t in zip(s, t):
            #check if there is a consistent mapping from s to t
            if (char_s in map_s_to_t and map_s_to_t[char_s] != char_t) or \
               (char_t in map_t_to_s and map_t_to_s[char_t] != char_s):
               return False
            
            #record the mapping in both dictionaries
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s

        return True 
    
def run_tests():
    #create an instance of solution
    solution = Solution()

    # Test cases for isomorphic strings function
    test_cases = [
        ("egg", "add", True),                   # Simple isomorphic case
        ("foo", "bar", False),                  # Non-isomorphic, repeated characters map differently
        ("paper", "title", True),               # Isomorphic with non-repeating and repeating characters
        ("", "", True),                         # Edge case with empty strings
        ("a", "b", True),                       # Single character strings
        ("ab", "aa", False),                    # Non-isomorphic, two characters mapping to the same character
        ("123@!", "!@321", True),               # Isomorphic with special characters and numbers
        ("abcd", "mnop", True),                 # Isomorphic without any repeating characters
        ("abcdabcd", "mnopmnop", True),         # Isomorphic with a repeating pattern
        ("abcdabcd", "mnopmnpx", False)         # Non-isomorphic, similar pattern but one character differs
    ]

    for i, (s, t, expected) in enumerate(test_cases):
        #call the method
        output = solution.isIsomorphic(s, t)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()