# Print Linked List

## Problem Description

You are given A which is the head of a linked list. Print the linked list in space separated manner. </br>

***Note***: The last node value must also be succeeded by a space and after printing the entire list you should print a new line



### Problem Constraints

1 <= size of linked list <= 105 </br>
1 <= value of nodes <= 109

---

### Input Format
The first argument A is the head of a linked list.


### Output Format
You dont need to return anything

---

## Example Input
```
Input 1:
A = 1 -> 2 -> 3

Input 2:
A = 4 -> 3 -> 2 -> 1
```

## Example Output
```
Output 1:
1 2 3

Output 2:
4 3 2 1
```

## Example Explanation
```
For Input 1:
We print the given linked list

For Input 2:
We print the given linked list
```

---

# CODE

```python
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def solve(self, A):
        temp = A
        print(temp.val, end = ' ')
        i = 0
        while temp.next != None:
            temp = temp.next
            print(temp.val, end = ' ')
            i += 1
        print()
```
