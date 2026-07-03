# Balanced Paranthesis

## Problem Description

Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A. </br>
Refer to the examples for more clarity. </br>


### Problem Constraints
1 <= |A| <= 100

----

### Input Format

The first and the only argument of input contains the string A having the parenthesis sequence.


### Output Format
```
Return 0 if the parenthesis sequence is not balanced.
Return 1 if the parenthesis sequence is balanced.
```

---

## Example Input
```
Input 1:
 A = {([])}
 
Input 2:
 A = (){
 
Input 3:
 A = ()[] 
```

## Example Output
```
Output 1:
 1 
 
Output 2:
 0 
 
Output 3:
 1 
```

## Example Explanation
```
We can clearly see that the first and third case contain valid paranthesis.
In the second case, there is no closing bracket for {, thus the paranthesis sequence is invalid.
```

---

# CODE

```python
from collections import deque
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        st = deque()
        for i in range(len(A)):
            if A[i] in ['(', '{', '[']:
                st.append(A[i])
            elif A[i] == ')':
                if len(st) == 0 or st[-1] != '(':
                    return 0
                st.pop()
            elif A[i] == '}':
                if len(st) == 0 or st[-1] != '{':
                    return 0
                st.pop()
            else:
                if len(st) == 0 or st[-1] != '[':
                    return 0
                st.pop()
        return int(len(st) == 0)
```

'or'

```python
    def solve(self, A):
        st = deque()
        for i in range(len(A)):
            if A[i] in ['(', '{', '[']:
                st.append(A[i])
            elif A[i] == ')':
                if len(st) > 0 and st[-1] == '(':
                    st.pop()
                else:
                    return 0
            elif A[i] == '}':
                if len(st) > 0 and st[-1] == '{':
                    st.pop()
                else:
                    return 0
            else:
                if len(st) > 0 and st[-1] == '[':
                    st.pop()
                else:
                    return 0
        return int(len(st) == 0)
```
