Flip

Problem Description
You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.
If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.

Problem Constraints
1 <= size of string <= 100000

Input Format
First and only argument is a string A.

Output Format
Return an array of integers denoting the answer.

Example Input
Input 1:
A = "010"
Input 2:
A = "111"

Example Output
Output 1:
[1, 1]
Output 2:
[]

Example Explanation
Explanation 1:
A = "010"

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | "110"
[1 2]          | "100"
[1 3]          | "101"
[2 2]          | "000"
[2 3]          | "001"
We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].

Explanation 2:
No operation can give us more than three 1s in final string. So, we return empty array [].

CODE:

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        cur = 0
        maxx = 0
        l = 0
        r = 0
        ans = [-1, -1]
        # basic kadane's algorithm implementation
        for i in range(0, len(A)):
            if(A[i] == '1'):
                cur -= 1
            else:
                cur += 1
            
            if(cur > maxx):
                ans[0] = l+1
                ans[1] = r+1
                maxx = cur

            if(cur < 0): 
                cur = 0
                l = i+1
                r = i+1
            else:
                r += 1

        if(maxx == 0):
            return []
        else:
            return ans

'or'

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        A=list(A)
        #print(A)
        for i in range(len(A)):
            if A[i] == "0":
                A[i] = 1
            else:
                A[i] = -1
        
        #print(A)

        max_sum = 0
        current_sum = 0
        start = -1
        end = -1
        temp = 0
        
        for i in range(len(A)):
            #print("max_sum",max_sum)
            current_sum = A[i]+max(0,current_sum)       
            #print("current_sum",current_sum)
            if current_sum > max_sum:
                max_sum = max(current_sum,max_sum)
                start = temp
                end = i
                #end=i
                #print("start",start)
            
            if current_sum < 0:
                temp = i+1
                
                #print("end",end)
        if start == -1 and end == -1:
            return []
        else:
            return [start+1, end+1]


solution = Solution()
print(solution.flip(A = "010"))  -->  O/P: [1, 1]
