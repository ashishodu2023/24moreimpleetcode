class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


def printList(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def main():
    # List: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original List:")
    printList(head)

    new_head = removeNthFromEnd(head, 2)
    print("List after removing 2nd node from end:")
    printList(new_head)


if __name__ == "__main__":
    main()
