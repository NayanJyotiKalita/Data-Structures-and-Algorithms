# Redundant Braces

## Problem Description

Given a string **A** denoting an expression. It contains the following operators '+', '-', '*', '/'. </br>

Check whether A has redundant braces or not. </br>

**NOTE:** A will be always a valid expression and will not contain any white spaces. 



### Problem Constraints

1 <= |A| <= 105

---

### Input Format

The only argument given is string A.


### Output Format

Return 1 if A has redundant braces else, return 0.

---

## Example Input
```
Input 1:
 A = "((a+b))"
 
Input 2:
 A = "(a+(a+b))"
```


## Example Output
```
Output 1:
 1
 
Output 2:
 0
```

## Example Explanation
```
Explanation 1:
 ((a+b)) has redundant braces so answer will be 1.
 
Explanation 2:
 (a+(a+b)) doesn't have have any redundant braces so answer will be 0.
```

---

# CODE

```python
from collections import deque
class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        A = list(A)

        stack = deque()
        status = 0

        for i in range(len(A)):

            if A[i] == ")":
                status = 1
                while stack and stack[-1] != "(":
                    x = stack.pop()
                    if x in ["+", "-", "*", "/"]:
                        status = 0
                stack.pop()

                if status == 1:
                    return status
 
            else:
                stack.append(A[i])

        return int(status)
```
