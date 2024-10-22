class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #assume the first string is the prefix
        prefix = strs[0]
        #for each subsequent string, reduce the prefix length until it matches the beginning of the string
        for string in strs[1:]:
            while prefix != string[:len(prefix)]:
                prefix = prefix[:-1]
                #if the prefix is reduced to an empty string at any point, return an empty string
                if prefix == "":
                    return prefix
        #once all strings have been compared, the remaining prefix is the longest common prefix
        return prefix

def run_tests():
    #create an instance of solution
    solution = Solution()

    #Define your test cases
    test_cases = [
    # Case 1: Typical case with common prefix
    (["flower", "flow", "flight"], "fl"),
    
    # Case 2: No common prefix
    (["dog", "racecar", "car"], ""),
    
    # Case 3: Single string in the array
    (["single"], "single"),
    
    # Case 4: All strings are identical
    (["repeat", "repeat", "repeat"], "repeat"),
    
    # Case 5: Empty string included in the array
    (["", "empty", "example"], ""),
    
    # Case 6: Strings of varying lengths but common prefix
    (["interview", "interact", "internet", "internal"], "inter"),
    
    # Case 7: All strings are empty
    (["", "", ""], ""),
    
    # Case 8: Single character strings with common prefix
    (["a", "a", "a"], "a"),
    
    # Case 9: Single character strings with no common prefix
    (["a", "b", "c"], ""),
    
    # Case 10: Large input with a very long common prefix
    (["longprefix" * 20, "longprefix" * 15 + "xyz", "longprefix" * 18 + "abc"], "longprefix" * 15)
    ]

    for i, (strs, expected) in enumerate(test_cases):
        #call the method
        output = solution.longestCommonPrefix(strs)

        #compare the result with the expected output
        if output == expected:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed")
            print(f" Expected: {expected}")
            print(f" Got: {output}")

#run the tests
run_tests()