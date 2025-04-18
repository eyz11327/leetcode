from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Spent 60% of the time trying to figure out how to append to a linked list lol
    retLst: ListNode = ListNode()
    carry = 0
    while True:
        first_val = l1.val
        second_val = l2.val
        val = first_val + second_val
        if carry != 0:
            val += carry
            carry = 0
        if val >= 10:
            carry = 1

        newNode = ListNode()
        newNode.val = val % 10

        last = retLst
        while last.next:
            last = last.next
        
        last.next = newNode

        if l1.next == None and l2.next == None and carry == 0:
            return retLst.next

        if l1.next == None:
            l1.val = 0
        else:
            l1 = l1.next

        if l2.next == None:
            l2.val = 0
        else:
            l2 = l2.next