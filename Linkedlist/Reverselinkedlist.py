class ListNode:

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def printList(head: ListNode):
    while head:
        print(head.value, end="->")
        head = head.next
    print("None")


def reverseList(head: ListNode) -> ListNode:

    previous = None
    current = head

    while current:

        nxt = current.next
        current.next = previous
        previous = current
        current = nxt

    return previous


def main():
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original List:")
    printList(head)

    reversed_head = reverseList(head)
    print("Reversed List:")
    printList(reversed_head)


if __name__ == "__main__":
    main()
