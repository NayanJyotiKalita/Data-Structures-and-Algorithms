# Double Character Trouble

## Problem Description

You have a string, denoted as **A**. </br>

To transform the string, you should perform the following operation repeatedly:  </br>
  1. Identify the **first occurrence** of **consecutive identical pairs** of characters within the string. </br>
  2. **Remove this pair** of identical characters from the string. </br>
  3. Repeat steps 1 and 2 until there are **no more** consecutive identical pairs of characters. </br>
The **final result** will be the transformed string. </br>


### Problem Constraints

1 <= |A| <= 100000

---

### Input Format
First and only argument is string A.

### Output Format
Return the final string.

---

## Example Input
```
Input 1:
 A = "abccbc"

Input 2:
 A = "ab"
```

## Example Output
```
Output 1:
 "ac"
 
Output 2:
 "ab"
```

## Example Explanation

  - **Explanation 1:**
```
The Given string is "abccbc".

Remove the first occurrence of consecutive identical pairs of characters "cc".
After removing the string will be "abbc".

Again Removing the first occurrence of consecutive identical pairs of characters "bb".
After remvoing, the string will be "ac".

Now, there is no consecutive identical pairs of characters.
Therefore the string after this operation will be "ac".
```

  - **Explanation 2:**
No removals are to be done

---

# CODE

```python
from collections import deque
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        st = deque()
        for i in range(len(A)):
            if len(st) > 0 and st[-1] == A[i]:
                st.pop()
            else:
                st.append(A[i])
        ans = []
        while st:
            ans.append(st.pop())
        return "".join(ans[::-1])
```
