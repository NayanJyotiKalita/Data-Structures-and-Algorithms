Farmer and the cows

Problem Description
Farmer John's N cows, conveniently numbered 1…N, are all standing in a row (they seem to do so often that it now takes very little prompting from Farmer John to line them up). Each cow has a breed ID: 1 for Holsteins and 2 for Jerseys.
Farmer John would like your help counting the number of cows of each breed that lie within certain intervals of the ordering.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 2
1 <= Q.size() <= 105
1 <= Q[i][0] <= Q[i][1] <= N, which is the two end points of each Query.

Input Format
First Argument is an Array A
Second Argument is 2-d array B, which is the Queries.

Output Format
Return a 2-d array of size Qx2.

Example Input
Input 1:
A = [2, 1, 1, 2, 1]
B = [[1, 5],
     [3, 3],
     [2, 4]]

Example Output
Output 1:
[[3, 2], [1, 0], [2, 1]]

Example Explanation
Explanation 1:
For the first Query (1, 5): 
A[1:5] = [2, 1, 1, 2, 1]
Count of 1 : 3
Count of 2 : 2
Thus [3, 2] is the answer for this query.

For the second Query (3, 3):
A[3:3] = [1]
Count of 1 : 1
Count of 2 : 0
Thus [1, 0] is the answer for this query.

For the Third Query (2, 4):
A[2:4] = [1, 1, 2]
Count of 1 : 2
Count of 2 : 1
Thus [2, 1] is the answer for this query.

At last return the answer, [[3, 2], [1, 0], [2, 1]]. 

CODE:

 class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def countCows(self, A, B):
        c = []
        count1 = []
        count2 = []
        n = len(A)
        
        for i in range(n):
            if A[i] == 1:
                count1.append(1)
            else:
                count1.append(0)
                
        for i in range(n):
            if A[i] == 2:
                count2.append(1)
            else:
                count2.append(0)
                
        for i in range(1, len(count1)):
            count1[i] = count1[i-1] + count1[i]
        for i in range(1, len(count2)):
            count2[i] = count2[i-1] + count2[i]
        
        for i in range(len(B)):
            summ_1 = 0
            summ_2 = 0
            ls = []
            l = B[i][0]-1
            r = B[i][1]-1
            if l == 0:
                summ_1 = count1[r]
                summ_2 = count2[r]
            else:
                summ_1 = count1[r] - count1[l-1]
                summ_2 = count2[r] - count2[l-1]
                
            ls.append(summ_1)
            ls.append(summ_2)


solution = Solution()
print(solution.countCows( A = [2, 1, 1, 2, 1], B = [[1, 5], [3, 3], [2, 4]] ))
