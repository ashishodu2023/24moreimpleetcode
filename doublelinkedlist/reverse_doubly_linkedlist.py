"""
Input: Head of a doubly linked list, where each node has val, next, and prev pointers.
Output: Head of the same list after reversing the direction of all pointers.

Original: 1 ⇄ 2 ⇄ 3 ⇄ 4
Reversed: 4 ⇄ 3 ⇄ 2 ⇄ 1

T O(n)
S O(n)

"""


class Node:

    def __init__(self,val:int):
        self.val = val
        self.prev = None
        self.next = None


    def __repr__(self):
        return f"Node({self.val})"
    



def reverse_doubly_linkedlist(head:Node)->Node:

    current = head 
    new_head = None


    while current:
        current.prev, current.next = current.next,current.prev 
        new_head = current
        current = current.prev


    return new_head

def build_dll(values: list[int]) -> Node:
    """Builds a DLL from a list of values and returns its head."""
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for v in values[1:]:
        node = Node(v)
        curr.next = node
        node.prev = curr
        curr = node
    return head

def dll_to_list(head: Node) -> list[int]:
    """Converts a DLL starting at head into a Python list of values."""
    out = []
    curr = head
    while curr:
        out.append(curr.val)
        curr = curr.next
    return out

if __name__ == "__main__":
    # Test cases
    cases = [
        ([], []),              # empty list
        ([1], [1]),            # single-node list
        ([1, 2], [2, 1]),      # two-node list
        ([1, 2, 3, 4], [4, 3, 2, 1]),  # longer list
    ]

    for vals, expected in cases:
        head = build_dll(vals)
        rev_head = reverse_doubly_linkedlist(head)
        result = dll_to_list(rev_head)
        print(f"{vals} -> {result} (expected {expected})")
        assert result == expected
