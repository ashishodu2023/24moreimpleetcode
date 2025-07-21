class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(head1: ListNode, head2: ListNode) -> ListNode:

    dummy = current = ListNode(0)

    carry = 0

    while head1 or head2 or carry:

        val1 = head1.val if head1 else 0
        val2 = head2.val if head2 else 0

        total = val1 + val2 + carry

        carry = total // 10

        current.next = ListNode(total % 10)

        current = current.next

        if head1:
            head1 = head1.next

        if head2:
            head2 = head2.next

    return dummy.next


def printList(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def main():
    # List 1: 2 -> 4 -> 3  (342)
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    # List 2: 5 -> 6 -> 4  (465)
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    result_head = addTwoNumbers(l1, l2)
    print("Sum as List:")
    printList(result_head)


if __name__ == "__main__":
    main()
