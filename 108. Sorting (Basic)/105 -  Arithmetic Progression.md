# Arithmetic Progression

## Problem Description
Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0. </br>
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

### Problem Constraints
2 <= N <= 105 </br>
-109 <= A[i] <= 109

---

### Input Format
The first and only argument is an integer array A of size N.

### Output Format
Return 1 if the array can be rearranged to form an arithmetic progression, otherwise return 0.

---

## Example Input
- Input 1: </br>
 A = [3, 5, 1]

- Input 2: </br>
 A = [2, 4, 1]


## Example Output
- Output 1: </br>
 1

- Output 2: </br>
 0


## Example Explanation
- Explanation 1: </br>
 We can reorder the elements as [1, 3, 5] or [5, 3, 1] with differences 2 and -2 respectively, between each consecutive elements.

- Explanation 2: </br>
 There is no way to reorder the elements to obtain an arithmetic progression.

---

# CODE

```python
class Solution:
    # @param A : list of integers
    # @return an integer
    def arithmetic_progression(self, A):
        A.sort()
        for i in range(1,len(A)-1):
            if A[i] - A[i-1] != A[i+1] - A[i]:
                return 0
        return 1
```

'or'

```python
class Solution:
    # @param A : list of integers
    # @return an integer
    def arithmetic_progression(self, A):
        n = len(A)
        A.sort()
        dif = A[1] - A[0]
        ans = 1
        for i in range(1, n):
            if(A[i] - A[i-1] != dif):
                ans = 0
                break
        return ans
```

```python
solution = Solution()
print(solution.arithmetic_progression(A = [3, 5, 1]))  --> O/P: 1
```
