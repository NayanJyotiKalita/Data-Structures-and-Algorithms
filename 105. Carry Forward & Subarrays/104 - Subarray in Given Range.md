# Subarray in given range

## Problem Description
Given an array A of length N, return the subarray from B to C.

### Problem Constraints
1 <= N <= 105 </br>
1 <= A[i] <= 109 </br>
0 <= B <= C < N </br>

---

### Input Format
The first argument A is an array of integers </br>
The remaining argument B and C are integers.

### Output Format
Return a subarray

---

## Example Input
- Input 1: </br>
A = [4, 3, 2, 6] </br>
B = 1 </br>
C = 3

- Input 2: </br>
A = [4, 2, 2] </br>
B = 0 </br>
C = 1

## Example Output
- Output 1: </br>
[3, 2, 6]

- Output 2: </br>
[4, 2]

## Example Explanation
- Explanation 1: </br>
The subarray of A from 1 to 3 is [3, 2, 6].
- Explanation 2: </br>
The subarray of A from 0 to 1 is [4, 2].

---

# CODE:

```python
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def subarray_in_range(self, A, B, C):
        d = []
        for i in range(B, C+1):
            d.append(A[i])
        return d
```

'or'

```python
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def subarray_in_range(self, A, B, C):
        return A[B : C + 1]
```

```python
solution = Solution()
print(solution.subarray_in_range(A = [4, 3, 2, 6], B = 1, C = 3))  -->  O/P: [3, 2, 6]
```
