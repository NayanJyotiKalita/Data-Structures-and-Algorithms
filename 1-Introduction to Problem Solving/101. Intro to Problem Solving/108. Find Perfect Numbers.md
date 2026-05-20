# Find Perfect Numbers

## Problem Description

You are given an integer A. You have to tell whether it is a perfect number or not. </br> 
Perfect number is a positive integer which is equal to the sum of its proper positive divisors. </br> 
A proper divisor of a natural number is the divisor that is strictly less than the number.</br> 
 
### Problem Constraints
1 <= A <= 106

---

### Input Format
First and only argument contains a single positive integer A.

### Output Format
Return 1 if A is a perfect number and 0 otherwise.

---

## Example Input
- Input 1: </br> 
A = 4

- Input 2: </br> 
A = 6


## Example Output
- Output 1: </br> 
0 

- Output 2: </br> 
1 

## Example Explanation:
- Explanation 1: </br> 
For A = 4, the sum of its proper divisors = 1 + 2 = 3, is not equal to 4.

- Explanation 2: </br> 
For A = 6, the sum of its proper divisors = 1 + 2 + 3 = 6, is equal to 6. 

---

# CODE

```python
def perfect_num(self, A):
    summ = 0
    for i in range(1, A//2 + 1):
        if A % i == 0:
            summ = summ + i
    if summ == A:
        return 1
    else:
        return 0

solution = Solution()
print(solution.perfect_num(A = 4))
```
