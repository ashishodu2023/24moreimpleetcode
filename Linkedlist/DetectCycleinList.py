class ListNode:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def hasCycle(head: ListNode) -> bool:

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def main():
    # Create cycle: 3 -> 2 -> 0 -> -4 -> (points back to node 2)
    node4 = ListNode(-4)
    node3 = ListNode(0, node4)
    node2 = ListNode(2, node3)
    head = ListNode(3, node2)
    node4.next = node2  # Creating cycle

    print("Has cycle:", hasCycle(head))


if __name__ == "__main__":
    main()
