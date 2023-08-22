# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sumList = ListNode(0)
        sumListTail = sumList
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            carry, val = divmod(sum + carry, 10)
            sumListTail.next = ListNode(val)
            sumListTail = sumListTail.next
        return sumList.next

# Main
def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()
    sumList = solution.addTwoNumbers(l1, l2)
    while sumList:
        print(sumList.val)
        sumList = sumList.next

if __name__ == '__main__':
    main()