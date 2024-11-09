# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next #move slow pointer by 1 step
            fast = fast.next.next #move fast pointer by 2 steps

            if slow == fast:
                return True

        return False
    
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_entry = head if pos == 0 else None  # Initialize cycle_entry to head if pos == 0

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        # Mark the node where the cycle should start
        if i == pos:
            cycle_entry = current
    
    # Create the cycle
    if pos != -1:
        current.next = cycle_entry

    return head

def test_hasCycle():
    #create an instance of solution
    solution = Solution()

    # Define test cases
    test_cases = [
        ([3, 2, 0, -4], 1, True),     # Cycle starting at index 1
        ([1, 2], 0, True),            # Small list with a cycle
        ([1], -1, False),             # Single node, no cycle
        ([], -1, False),              # Empty list, no cycle
        ([1, 2, 3, 4, 5], -1, False), # Multiple nodes, no cycle
        ([1, 2, 3, 4, 5], 4, True),   # Cycle at the last node pointing back to itself
        ([1, 2, 3], 2, True),         # Cycle at the end pointing back to a middle node
        ([1, 2, 3, 4], 1, True),      # Cycle starting at second node
        ([1, 2, 3, 4, 5, 6, 7, 8], 0, True), # Long list with cycle at the head
        ([10, 20, 30, 40], -1, False) # List without cycle
    ]
    
    # Run the test cases
    for i, (values, pos, expected) in enumerate(test_cases):
        head = create_linked_list_with_cycle(values, pos)
        result = solution.hasCycle(head)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

# Run tests
test_hasCycle()