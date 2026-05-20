# Reverse in a range

## Problem Description
Given an array A of N integers and also given two integers B and C. Reverse the elements of the array A within the given inclusive range [B, C].


### Problem Constraints
1 <= N <= 105 </br>
1 <= A[i] <= 109 </br>
0 <= B <= C <= N - 1

---

### Input Format
The first argument A is an array of integer. </br>
The second and third arguments are integers B and C

### Output Format
Return the array A after reversing in the given range.

---

## Example Input
- **Input 1:**             </br>
A = [1, 2, 3, 4]       </br>
B = 2                  </br>
C = 3                  </br>

- **Input 2:**             </br> 
A = [2, 5, 6]          </br> 
B = 0                  </br>
C = 2                  </br>

## Example Output
- **Output 1:**            </br>
[1, 2, 4, 3]

- **Output 2:**            </br>
[6, 5, 2]

---

# CODE

```python
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def reverse_in_range(self, A, B, C):
        for i in range((C-B+1)//2):
            A[B+i], A[C-i] = A[C-i], A[B+i]
        return A
```
'or'

```python
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        for i in range(B, (C+B+1)//2):
                A[i], A[C+B-i] = A[C+B-i], A[i]
        return A
```
'or'

```python
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def reverse_in_range(self, A, B, C):
        i , j = B , C
        while i < j :
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i , j = i + 1 , j - 1
        return A
```

```python
solution = Solution()
print(solution.reverse_in_range(A = [1, 2, 3, 4], B = 2, C = 3))  -->  O/P: [1, 2, 4, 3]
```
