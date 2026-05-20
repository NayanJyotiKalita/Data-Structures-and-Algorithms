# Count Intersection

Problem Description
You are given a 2D array A of length N3 consisting of N intervals.
where interval from A[i][1] to A[i][2] is defined below

1. if A[i][0] = 1 then both A[i][1] and A[i][2] is included in interval
2. if A[i][0] = 2 then A[i][1] is included and and A[i][2] is excluded in interval
3. if A[i][0] = 3 then A[i][1] is excluded and and A[i][2] is included in interval
4. if A[i][0] = 4 then both A[i][1] and A[i][2] is excluded in interval

Your task is to find How many pairs of intervals are so their intersection is not null.

Problem Constraints
1 <= |A| <= 1000
1 <= A[i][0] <= 4
1 <= A[i][1] <A[i][2] <= 109

Input Format
Argument A is a 2D array of integers

Output Format
Return an Integer

Example Input
Input 1:
A = [[1, 1, 2],
[2, 2, 3],
[3, 2, 4]]
Input 2:
A = [[1, 1, 2],
[2, 3, 4]] 

Example Output
Output 1:
2 
Output 2:
0

Example Explanation*
Explanation 1: -
Two pairs of the interval will share some common points
first pair - [1, 2] and [2, 3)
Second pair - [2, 3) and (2, 4]

Explanation 2: -
No such pair exists

CODE:

 class Solution:
    # @param A : list of list of integers
    # @return an integer
    def count_intersection(self, A):
        c = []
        n = len(A)
        
        for i in range(n):
            k, l, r = A[i]
            if k == 1:
                c.append((l, r))
            elif k == 2:
                c.append((l, r-0.5))
            elif k == 3:
                c.append((l+0.5, r))
            elif k == 4:
                c.append((l+0.5, r-0.5))
        
        c.sort()
        count = 0
        
        for i in range(len(c)):
            for j in range(i+1, len(c)):
                if c[j][0] > c[i][1]:
                    break
                if max(c[i][0], c[j][0]) <= min(c[i][1], c[j][1]):
                    count += 1
        
        return count 


solution = Solution()
print(solution.count_intersection( A = [[1, 1, 2], [2, 2, 3], [3, 2, 4]] ))  -->  O/P: 2
