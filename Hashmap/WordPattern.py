class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        #check if the lengths of pattern and words match
        if len(pattern) != len(words):
            return False

        #dictionaries to store the mappings
        char_to_word = {}
        word_to_char = {}

        for char, word, in zip(pattern, words):
            #check if char already maps to a differnt word
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word

            #check if word already maps to a differnt char
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        return True
    
def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
        # Simple match, should return True
        ("abba", "dog cat cat dog", True),

        # Different word count than pattern, should return False
        ("abba", "dog cat cat", False),
    
        # Pattern is bijective but words are not, should return False
        ("abba", "dog dog dog dog", False),

        # Pattern repeats and bijection holds, should return True
        ("aaaa", "dog dog dog dog", True),
    
        # Pattern has a bijective mapping with distinct words, should return True
        ("abcd", "dog cat fish bird", True),
    
        # Pattern with repeated characters, but no matching repeated words, should return False
        ("aabb", "dog dog cat fish", False),
    
        # Very long pattern and string, bijective mapping holds, should return True
        ("a" * 150 + "b" * 150, "cat " * 150 + "dog " * 150, True),
    
        # Long pattern and string with single repeating word, should return False
        ("abcabcabcabc", "dog dog dog dog dog dog dog dog dog dog dog dog", False),
    
        # Single character pattern and single word, should return True
        ("a", "dog", True),
    
        # Pattern and words do not align in mapping due to extra character, should return False
        ("ab", "dog cat cat", False)
    ]

    for i, (pattern, s, expected) in enumerate(test_cases):
        #call the method
        output = solution.wordPattern(pattern, s)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()