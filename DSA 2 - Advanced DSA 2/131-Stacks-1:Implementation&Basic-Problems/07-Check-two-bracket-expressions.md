# Check two bracket expressions

## Problem Description
```
Given two strings A and B. Each string represents an expression consisting of lowercase English alphabets, '+', '-', '(' and ')'.

The task is to compare them and check if they are similar. If they are identical, return 1 else, return 0.

NOTE: It may be assumed that there are at most 26 operands from ‘a’ to ‘z’, and every operand appears only once.
```

### Problem Constraints

1 <= length of the each String <= 100

---

### Input Format

The given arguments are string A and string B.


### Output Format

Return 1 if they represent the same expression else return 0.

---

## Example Input
```
Input 1:
 A = "-(a+b+c)"
 B = "-a-b-c"
 
Input 2:
 A = "a-b-(c-d)"
 B = "a-b-c-d"
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
 The expression "-(a+b+c)" can be written as "-a-b-c" which is equal as B. 
 
Explanation 2:
 Both the expression are different.
```

 # CODE

```python
from collections import deque
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        return 1 if self.process_expression(A) == self.process_expression(B) else 0

    def process_expression(self, string):
        string = list(string)
        ans = {}
        stack = deque()
        '''refer notes '''
        sign = 1
        stack.append(sign)
        for i in range(len(string)):
            #if there is positive sign , consider as no change , so let the sign be 1
            if string[i] == "+":
                sign = 1 * stack[-1]
            #if there is -ve sign , consider change to -1 and append the same to stack
            elif string[i] == "-":
                sign = -1 * stack[-1]
            #if there is -ve sign , consider change to -1 and append the same to stack
            elif string[i] == "(":
                stack.append(sign)
            elif string[i] == ")":
                stack.pop()
            elif string[i].isalpha():
                ans[string[i]] = sign
        #print("ans",ans)
        return ans 
```
