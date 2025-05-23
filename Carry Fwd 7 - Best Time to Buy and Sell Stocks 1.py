Best Time to Buy and Sell Stocks I

Problem Description
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Return the maximum possible profit.

Problem Constraints
0 <= A.size() <= 700000
1 <= A[i] <= 107

Input Format
The first and the only argument is an array of integers, A.

Output Format
Return an integer, representing the maximum possible profit.

Example Input
Input 1:
A = [1, 2]
Input 2:
A = [1, 4, 5, 2, 4]

Example Output
Output 1:
1
Output 2:
4

Example Explanation
Explanation 1:
Buy the stock on day 0, and sell it on day 1.
Explanation 2:
Buy the stock on day 0, and sell it on day 2.

CODE:

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        maxprofit = 0
        n = len(A)
        if n == 0:
            return 0
        maxi = A[n-1]
        for i in range(n-2, -1, -1):
            if A[i] > maxi:
                maxi = A[i]
            maxprofit = max(maxprofit, maxi-A[i])
        return maxprofit
'or'

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        maxprofit = 0
        n = len(A)
        if n == 0:
            return 0
        mini = A[0]
        for i in range(len(A)):
            if A[i] < mini:
                mini = A[i]
            maxprofit = max(maxprofit, A[i]-mini)
        return maxprofit


solution = Solution()
print(solution.maxProfit(A = [1, 4, 5, 2, 4]))  -->  O/P: 4
