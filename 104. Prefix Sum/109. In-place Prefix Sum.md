# In-place Prefix Sum

## Problem Description
Given an array A of N integers. Construct prefix sum of the array in the given array itself.

### Problem Constraints
1 <= N <= 105 </br>
1 <= A[i] <= 103

---

### Input Format
Only argument A is an array of integers.

### Output Format
Return an array of integers denoting the prefix sum of the given array.

---

## Example Input
- **Input 1:** </br>
A = [1, 2, 3, 4, 5]

- **Input 2:** </br>
A = [4, 3, 2]

## Example Output
- **Output 1:** </br>
[1, 3, 6, 10, 15]

- **Output 2:** </br>
[4, 7, 9]

## Example Explanation
- **Explanation 1:** </br>
The prefix sum array of [1, 2, 3, 4, 5] is [1, 3, 6, 10, 15].

- **Explanation 2:** </br>
The prefix sum array of [4, 3, 2] is [4, 7, 9].

---

# CODE

```python
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def in_place_psum(self, A):
        for i in range(1, len(A)):
            A[i] = A[i] + A[i-1]
        return A

solution = Solution()
print(solution.in_place_psum(A = [1, 2, 3, 4, 5]))  -->  O/P: [1, 3, 6, 10, 15]
```
