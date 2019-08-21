# Created by Jack Brewer August 2019

# Description
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Strategy
# Start at the single digits node of each list. Walk down both lists simultaneously, 
# adding together values at the same digit place and accounting for remainders.
# Continue walking down both lists until both ends are reached and final remainder has been added.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        remainder = 0
        nodeHead = ListNode(0)
        nodePtr = nodeHead
        l1Val = 0
        l2Val = 0        
        
        while(l1 != None or l2 != None or remainder != 0):
            
            # Get value of current nodes, or leave as 0 if end was reached
            if(l1 != None):
                l1Val = l1.val
                l1 = l1.next
            if (l2 != None):
                l2Val = l2.val
                l2 = l2.next
            
            val = l1Val + l2Val + remainder
            l1Val = 0
            l2Val = 0
            remainder = 0
                
            # Calculate remainder
            if(val > 9):
                remainder = val // 10
                nodePtr.val = val % 10
            else:
                nodePtr.val = val
                
            # Create next digit node if necessary
            if(remainder != 0 or l1 != None or l2 != None):
                tmpNode = ListNode(0)
                nodePtr.next = tmpNode
                nodePtr = tmpNode            
            
        return nodeHead
