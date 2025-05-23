Majority Element (N / 2)

Problem Description
Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.

Problem Constraints
1 <= N <= 5*105
1 <= num[i] <= 109

Input Format
Only argument is an integer array.

Output Format
Return an integer.

Example Input
Input 1:
[2, 1, 2]
Input 2:
[1, 1, 1]

Example Output
Input 1:
2
Input 2:
1

Example Explanation
For Input 1:
2 occurs 2 times which is greater than 3/2.
For Input 2:
 1 is the only element in the array, so it is majority

CODE:

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElementn/2(self, A):
        maj = -1
        cnt = 0
        for i in range(len(A)):
            if cnt == 0:
                maj = A[i]
                print(maj)
                cnt = 1
            if A[i] == maj:
                cnt += 1
                # print('maj', maj)
            else:
                cnt -= 1
        # print('maj', maj)
        # print('count', cnt)
        return maj

solution = Solution()
print(solution.majorityElementn/2(A = [2, 1, 2]))
