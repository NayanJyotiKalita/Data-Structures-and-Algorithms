Good Pair

Problem Description
Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.

Problem Constraints
1 <= A.size() <= 104
1 <= A[i] <= 109
1 <= B <= 109

Input Format
First argument is an integer array A.
Second argument is an integer B.

Output Format
Return 1 if good pair exist otherwise return 0.

Example Input
Input 1:
A = [1,2,3,4]
B = 7
Input 2:
A = [1,2,4]
B = 4
Input 3:
A = [1,2,2]
B = 4

Example Output
Output 1:
1
Output 2:
0
Output 3:
1


CODE:
1.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def good_pair(self, A, B):
        freq = {}
        for num in A:
            if B - num in freq:
                return 1
            freq[num] = True
        return 0

optional codes:

2. Hashset
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def good_pair(self, A, B):
    hs = set()
    for i in range(len(A)):
        if B - A[i] in hs:
            return 1
        hs.add(A[i])
    return 0

3. Hashmap (Dictionary)
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def good_pair(self, A, B):
    hm = {}
    for i in range(len(A)):
        if A[i] in hm:
            hm[A[i]] += 1
        else:
            hm[A[i]] = 1
    
    for i in hm.keys():
        if B - i in hm:
            if B - i != i or hm[B - i] > 1:
                return 1
    return 0

3. Brute Force
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def good_pair(self, A, B):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == B:
                return 1
    return 0


solution = Solution()
print(solution.good_pair( A = [1,2,3,4], B = 7 ))  -->  O/P: 1
print(solution.good_pair( A = [1,2,4], B = 4 ))  -->  O/P: 0
