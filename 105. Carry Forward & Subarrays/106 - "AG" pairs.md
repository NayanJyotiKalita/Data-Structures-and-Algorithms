## Special Subsequences "AG" - 2

## Problem Description
You have given a string A having Uppercase English letters. </br>
You have to find the number of pairs (i, j) such that A[i] = 'A', A[j] = 'G' and i < j.

### Problem Constraints
1 <= length(A) <= 105

---

### Input Format
First and only argument is a string A.

### Output Format
Return an long integer denoting the answer.

---

## Example Input
- Input 1: </br>
 A = "ABCGAG"

- Input 2: </br>
 A = "GAB"

## Example Output
- Output 1: </br>
 3
- Output 2: </br>
 0

## Example Explanation
- Explanation 1: </br>
 Subsequence "AG" is 3 times in given string, the pairs are (0, 3), (0, 5) and (4, 5).

- Explanation 2: </br>
 There is no subsequence "AG" in the given string.

---

# CODE:

### 1. Brute Force - O(n^2) :

```python
class Solution:
    # @param A : string
     # @return an long
    def count_AG_pairs(self, A):
        count = 0
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                 if A[i] == 'A' and A[j] == 'g':
                      count += 1
        return count
```

### 2. Optimised - Prefix Sum - T.C. - O(n), S.C. - O(n) :

```python
class Solution:
    # @param A : string
     # @return an long
    def scount_AG_pairs(self, A):
        pref_a = [0] * len(A)
        if A[0] == 'A':
            pref_a[0] = 1
        for i in range(1, len(A)):
            if A[i] == 'A':
                pref_a[i] = pref_a[i - 1] + 1
            else:
                pref_a[i] = pref_a[i - 1]

        count = 0
        for i in range(1, len(A)):
            if A[i] == 'G':
                count += pref_a[i - 1]

        return count
```

### 3. Optimised - Carry Forward - T.C. - O(n), S.C. - O(n) :

```python
 class Solution:
    # @param A : string
     # @return an long
    def count_AG_pairs(self, A):
        countA = 0
        count = 0
        for i in range(len(A)):
            if A[i] == 'A':
                countA += 1
            if A[i] == 'G':
                count += countA
        return count
```

solution = Solution()
print(solution.count_AG_pairs(A = "ABCGAG"))  -->  O/P: 3
