## Elements Removal

## Problem Description
Given an integer array A of size N. You can remove any element from the array in one operation. </br>
The cost of this operation is the sum of all elements in the array present before this operation. </br>
Find the minimum cost to remove all elements from the array.

### Problem Constraints
0 <= N <= 1000 </br>
1 <= A[i] <= 103

---

### Input Format
First and only argument is an integer array A.

### Output Format
Return an integer denoting the total cost of removing all elements from the array.

---

## Example Input
- Input 1: </br>
 A = [2, 1]
 
- Input 2: </br>
 A = [5]

## Example Output
- Output 1: </br>
 4
 
- Output 2: </br>
 5

## Example Explanation
- Explanation 1: </br>
 Given array A = [2, 1] </br>
 Remove 2 from the array => [1]. Cost of this operation is (2 + 1) = 3. </br>
 Remove 1 from the array => []. Cost of this operation is (1) = 1. </br>
 So, total cost is = 3 + 1 = 4. </br>
 
- Explanation 2: </br>
 There is only one element in the array. So, cost of removing is 5.

---

# CODE

```python
class Solution:
    # @param A : list of integers
    # @return an integer
    def ele_removal(self, A):
        A.sort(reverse = True)
        summ = 0
        for i in range(len(A)):
            summ += A[i] * (i+1)
        return summ
```

'or'

```python
class Solution:
    # @param A : list of integers
    # @return an integer
    def ele_removal(self, A):
        n = len(A)
        # sort the given array
        A.sort()
        count = 1 # how many times a number will contribute to ans.
        ans = 0
        for i in range(n-1, -1, -1):
            # add the ith element count times to the ans. 
            ans += count * A[i] 
            count += 1
        return ans
```

```python
solution = Solution()
print(solution.ele_removal(A = [2, 1]))  -->  O/P: 4
```
