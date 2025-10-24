# Pick from both sides!

## Problem Description
You are given an integer array A of size N. </br>
You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A. </br>
Find and return the maximum possible sum of the B elements that were removed after the B operations.

***NOTE:*** Suppose B = 3, and array A contains 10 elements, then you can: </br>
Remove 3 elements from front and 0 elements from the back, OR </br>
Remove 2 elements from front and 1 element from the back, OR </br>
Remove 1 element from front and 2 elements from the back, OR </br>
Remove 0 elements from front and 3 elements from the back. </br>

### Problem Constraints
1 <= N <= 105 </br>
1 <= B <= N </br>
-103 <= A[i] <= 103

---

### Input Format
First argument is an integer array A. </br>
Second argument is an integer B.

### Output Format
Return an integer denoting the maximum possible sum of elements you removed.

---

## Example Input 
- Input 1: </br>
 A = [5, -2, 3 , 1, 2] </br>
 B = 3

- Input 2: </br>
 A = [ 2, 3, -1, 4, 2, 1 ] </br>
 B = 4

## Example Output
- Output 1: </br>
 8

- Output 2:
 9

## Example Explanation
- Explanation 1: </br>
 Remove element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8

- Explanation 2: </br>
 Remove the first element and the last 3 elements. So we get 2 + 4 + 2 + 1 = 9

---

# CODE:

```python
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def pick_from_both_sides(self, A, B):

        for i in range(1, len(A)):
            A[i] = A[i-1] + A[i]

        n = len(A)
        ans = 0
        if n > B:
            ans = max(A[B-1], A[n-1]-A[n-B-1])
        else:
            ans = A[n-1]

        for i in range(B+1):
            if i > 0:
                pref = A[i-1]
            else:
                pref = 0

            if n-B+i > 0:
                suff = A[n-1] - A[n-B+i-1]
            else:
                suff = A[n-1]

            ans = max(ans, pref + suff)
        
        return ans


solution = Solution()
print(solution.pick_from_both_sides(A = [2, 3, -1, 4, 2, 1], B = 4))  -->  O/P: 9
```
