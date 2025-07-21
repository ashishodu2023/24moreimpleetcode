class ListNode:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def mergeTwoLists(head1: ListNode, head2: ListNode) -> ListNode:

    dummy = tail = ListNode(0)

    current1 = head1
    current2 = head2

    while current1 and current2:

        if current1.value < current2.value:
            tail.next = current1
            current1 = current1.next

        else:
            tail.next = current2
            current2 = current2.next

        tail = tail.next

    tail.next = current1 or current2

    return dummy.next

def printList(head: ListNode):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

def main():
    # First list: 1 -> 2 -> 4 -> None
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    # Second list: 1 -> 3 -> 4 -> None
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    merged_head = mergeTwoLists(l1, l2)
    print("Merged Sorted List:")
    printList(merged_head)


if __name__ == "__main__":
    main()
