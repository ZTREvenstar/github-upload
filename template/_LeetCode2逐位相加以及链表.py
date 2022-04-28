# template for 逐位相加 and Linked List

from typing import List


class ListNode:
    def __init__(self, val=0, Next=None):
        self.val = val
        self.next = Next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2

        # calc the first node in result
        carry_digit = 0
        head = ListNode(-1)
        myNode = head  # 第一个，需要一个工具node，return到head的next
        while node1 is not None or node2 is not None:
            val1 = node1.val if node1 is not None else 0
            val2 = node2.val if node2 is not None else 0
            newValue = val1 + val2 + carry_digit
            if newValue >= 10:
                newValue -= 10
                carry_digit = 1
            else:
                carry_digit = 0
            myNode.next = ListNode(newValue)
            myNode = myNode.next
            node1 = node1.next if node1 is not None else None
            node2 = node2.next if node2 is not None else None

        if carry_digit == 1:
            myNode.next = ListNode(1)

        return head.next


def initLikedList(myList: List) -> ListNode:
    myNode = ListNode(myList[0])
    head = myNode
    for i in range(1, len(myList)):
        newNode = ListNode(myList[i])
        myNode.next = newNode
        myNode = newNode
    return head


if __name__ == "__main__":
    print("hello")
    l1 = initLikedList([9, 9, 9, 9, 9, 9, 9])
    l2 = initLikedList([9, 9, 9, 9])
    obj = Solution()
    result = obj.addTwoNumbers(l1, l2)

    print("finished")
