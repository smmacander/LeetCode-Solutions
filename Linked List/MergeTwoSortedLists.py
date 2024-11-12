# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #initialize a dumy node to act as the head of the merged list
        dummy = ListNode()
        current = dummy

        #traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        #attach the remaining nodes
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        #the merged list is next to the dummy node
        return dummy.next

# Helper function to convert a Python list to a linked list
def list_to_linkedlist(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a Python list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test function for mergeTwoLists
def test_mergeTwoLists(list1_vals, list2_vals, expected_output):
    #create an instance of solution
    solution = Solution()

    list1 = list_to_linkedlist(list1_vals)
    list2 = list_to_linkedlist(list2_vals)
    merged_head = solution.mergeTwoLists(list1, list2)
    output = linkedlist_to_list(merged_head)
    assert output == expected_output, f"Failed: {output} != {expected_output}"
    print(f"Passed: {output} == {expected_output}")

test_cases = [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    ([], [0], [0]),
    ([1, 2, 3], [], [1, 2, 3]),
    ([2, 2, 2], [2, 2, 2], [2, 2, 2, 2, 2, 2]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([7, 8, 9], [1, 2, 3], [1, 2, 3, 7, 8, 9]),
    ([5], [3], [3, 5]),
    ([-3, -1, 0], [-2, 1, 2], [-3, -2, -1, 0, 1, 2]),
    ([1, 4, 5, 7], [2, 3], [1, 2, 3, 4, 5, 7]),
    ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
]

for list1_vals, list2_vals, expected in test_cases:
    test_mergeTwoLists(list1_vals, list2_vals, expected)