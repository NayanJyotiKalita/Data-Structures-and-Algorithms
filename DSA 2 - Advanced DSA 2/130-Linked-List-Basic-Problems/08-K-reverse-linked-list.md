# K reverse linked list

## Problem Description

You are given the head of a singly linked list A and an integer B. </br>

Reverse the nodes of A in groups of B consecutive nodes, traversing the list from beginning to end. Each group is reversed independently, and the relative order of the groups themselves stays the same. Return the head of the resulting list. </br>


### Problem Constraints
```
1 <= |A| <= 103
1 <= B <= |A|
B always divides |A| (the length of the list).
1 <= value of any node <= 109
```

---

### Input Format
```
The first argument is a pointer to the head of the linked list A.
The second argument is the integer B.
```

### Output Format

Return a pointer to the head of the modified linked list.

---

## Example Input
```
Input 1:
A = 1 -> 2 -> 3 -> 4 -> 5 -> 6
B = 2

Input 2:
A = 1 -> 2 -> 3 -> 4 -> 5 -> 6
B = 3
```

## Example Output
```
Output 1:
2 -> 1 -> 4 -> 3 -> 6 -> 5

Output 2:
3 -> 2 -> 1 -> 6 -> 5 -> 4
```

## Example Explanation
```
Explanation 1:
A = 1 -> 2 -> 3 -> 4 -> 5 -> 6, B = 2.
The consecutive groups of 2 nodes are (1, 2), (3, 4), (5, 6).
After reversing each group, the list becomes
2 -> 1 -> 4 -> 3 -> 6 -> 5.
Result: 2 -> 1 -> 4 -> 3 -> 6 -> 5

Explanation 2:
A = 1 -> 2 -> 3 -> 4 -> 5 -> 6, B = 3.
The consecutive groups of 3 nodes are (1, 2, 3), (4, 5, 6).
After reversing each group, the list becomes
3 -> 2 -> 1 -> 6 -> 5 -> 4.
Result: 3 -> 2 -> 1 -> 6 -> 5 -> 4
```

---

# CODE

```python
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        curr = A
        prev = None
        count = 0
        while curr != None and count < B:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1

        if nxt != None:
            A.next = self.reverseList(nxt, B)
        return prev

```
