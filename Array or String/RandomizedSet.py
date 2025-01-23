import random

class RandomizedSet:

    def __init__(self):
        # Initialize an empty list to store elements and a dictionary for index mapping

        self.data = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False # Value already exists
        # Add the value to the list and record its index in the dictionary
        self.index_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False # Value does not exist
        # Swap the element to remove with the last element in the list
        idx = self.index_map[val]
        last_element = self.data[-1]
        self.data[idx] = last_element
        self.index_map[last_element] = idx
        # Remove the last element and update the dictionary
        self.data.pop()
        del self.index_map[val]
        return True
 
    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.data)
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def test_randomized_set():
    # Initialize the RandomizedSet
    rs = RandomizedSet()
    
    # Test case 1: Insert minimum and maximum values
    assert rs.insert(-2**31) == True, "Test Case 1 Failed: Insert minimum value"
    assert rs.insert(2**31 - 1) == True, "Test Case 1 Failed: Insert maximum value"
    
    # Test case 2: Attempt to re-insert the same values
    assert rs.insert(-2**31) == False, "Test Case 2 Failed: Re-insert minimum value"
    assert rs.insert(2**31 - 1) == False, "Test Case 2 Failed: Re-insert maximum value"
    
    # Test case 3: Remove a value and try removing it again
    assert rs.remove(-2**31) == True, "Test Case 3 Failed: Remove existing minimum value"
    assert rs.remove(-2**31) == False, "Test Case 3 Failed: Remove non-existing value"
    
    # Test case 4: Randomly get elements with one element in the set
    assert rs.getRandom() == 2**31 - 1, "Test Case 4 Failed: Random with one element"
    
    # Test case 5: Add multiple elements and test random access
    rs.insert(1)
    rs.insert(2)
    rs.insert(3)
    random_set = {rs.getRandom() for _ in range(100)}
    assert random_set.issubset({1, 2, 3, 2**31 - 1}), "Test Case 5 Failed: Random subset mismatch"
    
    # Test case 6: Remove all elements and ensure no random calls are made
    rs.remove(1)
    rs.remove(2)
    rs.remove(3)
    rs.remove(2**31 - 1)
    rs.insert(0)
    assert rs.getRandom() == 0, "Test Case 6 Failed: Random with one element after removals"
    
    # Test case 7: Stress test with large numbers of insertions
    for i in range(1, 100001):
        rs.insert(i)
    assert len(rs.data) == 100001, "Test Case 7 Failed: Incorrect size after bulk insertions"
    
    # Test case 8: Remove a large range of values
    for i in range(1, 50001):
        rs.remove(i)
    assert len(rs.data) == 50001, "Test Case 8 Failed: Incorrect size after bulk removals"
    
    # Test case 9: Ensure random access with many elements remaining
    random_set_large = {rs.getRandom() for _ in range(1000)}
    assert random_set_large.issubset(set(range(50001, 100001)) | {0}), "Test Case 9 Failed: Random subset mismatch after bulk operations"
    
    # Test case 10: Edge case with alternating inserts and removes
    rs = RandomizedSet()
    for i in range(1, 1001):
        rs.insert(i)
    for i in range(1, 1001):
        rs.remove(i)
    assert len(rs.data) == 0, "Test Case 10 Failed: Incorrect size after alternating insert/remove"
    
    print("All test cases passed successfully!")

# Run the test function
test_randomized_set()