Merge Intervals

Problem Description
You have a set of non-overlapping intervals. You are given a new interval [start, end], insert this new interval into the set of intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Problem Constraints
0 <= |intervals| <= 105

Input Format
First argument is the vector of intervals
second argument is the new interval to be merged

Output Format
Return the vector of intervals after merging

Example Input
Input 1:
Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
Input 2:
Given intervals [1, 3], [6, 9] insert and merge [2, 6] .

Example Output
Output 1:
 [ [1, 5], [6, 9] ]
Output 2:
 [ [1, 9] ]

Example Explanation
Explanation 1:
(2,5) does not completely merge the given intervals
Explanation 2:
(2,6) completely merges the given intervals

CODE:

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def insert(self, A, B):
        A.append(B)
        A.sort()
        curr_s = A[0][0]
        curr_e = A[0][1]
        c = []
        for i in range(1, len(A)):
            if A[i][0] <= curr_e:
                curr_e = max(curr_e, A[i][1])
            else:
                c.append([curr_s,curr_e])
                curr_s = A[i][0]
                curr_e = A[i][1]
        c.append([curr_s,curr_e])
        return c


solution = Solution()
print(solution.insert( A = [[1, 3], [6, 9]], B = [2, 5] ))
