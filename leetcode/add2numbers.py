# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        
        if l1 == None:
            return l2
        
        if l2 == None:
            return l1
        
        resultLLhead = None
        resultLLtail = None
        carry = 0
        
        while (l1 != None and l2 != None):
            currentValue = l1.val + l2.val + carry
            carry = 0
            if (currentValue >= 10): 
                carry = 1
                currentValue %= 10
            
            newNode = ListNode(currentValue)
            
            if (resultLLhead == None):
                resultLLhead = newNode
                resultLLtail = resultLLhead
            else:
                resultLLtail.next = newNode
                resultLLtail = newNode
            l1 = l1.next
            l2 = l2.next
            
        while l1 != None:
            currentValue = l1.val + carry
            carry = 0
            if (currentValue >= 10): 
                carry = 1
                currentValue %= 10
                
            newNode = ListNode(currentValue)
            
            if (resultLLtail == None):
                resultLLtail = newNode
            else:
                resultLLtail.next = newNode
                resultLLtail = newNode
            l1 = l1.next
                
        while l2 != None:
            currentValue = l2.val + carry
            carry = 0
            if (currentValue >= 10): 
                carry = 1
                currentValue %= 10
                
            newNode = ListNode(currentValue)
            
            if (resultLLtail == None):
                resultLLtail = newNode
            else:
                resultLLtail.next = newNode
                resultLLtail = newNode
            l2 = l2.next
        
        if carry == 1:
            newNode = ListNode(1)
            if (resultLLtail == None):
                resultLLtail = newNode
            else:
                resultLLtail.next = newNode
                resultLLtail = newNode
        
        return resultLLhead