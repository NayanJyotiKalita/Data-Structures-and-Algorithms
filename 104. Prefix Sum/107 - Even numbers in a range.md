# Even numbers in a range

## Problem Description
You are given an array A of length N and Q queries given by the 2D array B of size Q×2. </br>
Each query consists of two integers B[i][0] and B[i][1]. </br>
For every query, your task is to find the count of even numbers in the range from A[B[i][0]] to A[B[i][1]]. </br>

### Problem Constraints
1 <= N <= 105 </br>
1 <= Q <= 105 </br>
1 <= A[i] <= 109 </br>
0 <= B[i][0] <= B[i][1] < N </br>

---

### Input Format
First argument A is an array of integers. </br>
Second argument B is a 2D array of integers. </br>

### Output Format
Return an array of integers.

---

## Example Input

- Input 1: </br>
A = [1, 2, 3, 4, 5] </br>
B = [   [0, 2] 
        [2, 4]
        [1, 4]   ]

- Input 2: </br>
A = [2, 1, 8, 3, 9, 6] </br>
B = [   [0, 3]
        [3, 5]
        [1, 3] 
        [2, 4]   ]

## Example Output

- Output 1: </br>
[1, 1, 2]

- Output 2: </br>
[2, 1, 1, 1]


## Example Explanation

- For Input 1: </br> 
The subarray for the first query is [1, 2, 3] (index 0 to 2) which contains 1 even number. </br> 
The subarray for the second query is [3, 4, 5] (index 2 to 4) which contains 1 even number. </br> 
The subarray for the third query is [2, 3, 4, 5] (index 1 to 4) which contains 2 even numbers. </br>

- For Input 2: </br>
The subarray for the first query is [2, 1, 8, 3] (index 0 to 3) which contains 2 even numbers. </br>
The subarray for the second query is [3, 9, 6] (index 3 to 5) which contains 1 even number. </br>
The subarray for the third query is [1, 8, 3] (index 1 to 3) which contains 1 even number. </br> 
The subarray for the fourth query is [8, 3, 9] (index 2 to 4) which contains 1 even number. </br>

---

# CODE:


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def even_num_in_range(self, A, B):
        c = []
        count = 0
        pref = [0] * len(A)
            
        for i in range(len(A)):
            if A[i] % 2 == 0:
                count += 1
                pref[i] = count
            else:
                pref[i] = pref[i - 1]
            
        for i in range(len(B)):
            count = 0
            l = B[i][0]
            r = B[i][1]
            if l == 0:
                count = pref[r]
            else:
                count = pref[r] - pref[l-1]
            c.append(count)
             
        return c

'or'

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def even_num_in_range(self, A, B):
        c = []
        count = 0
        pref = []
             
        for i in range(len(A)):
            if A[i] % 2 == 0:
                pref.append(1)
            else:
                pref.append(0)
        
        for i in range(1, len(pref)):
            pref[i] = pref[i] + pref[i-1]
        
        for i in range(len(B)):
            count = 0
            l = B[i][0]
            r = B[i][1]
            if l == 0:
                count = pref[r]
            else:
                count = pref[r] - pref[l-1]
            c.append(count)
             
        return c
                
             
solution =  Solution()
print(solution.even_num_in_range(A = [2, 1, 8, 3, 9, 6],
                                 B = [   [0, 3]
                                         [3, 5]
                                         [1, 3] 
                                         [2, 4]   ]))      -->  O/P: [2, 1, 1, 1]
