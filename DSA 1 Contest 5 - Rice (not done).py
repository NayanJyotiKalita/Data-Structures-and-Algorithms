Rice

Problem Description

You have to buy at least A kgs of rice. There are N packets of rice. The i-th (1-based indexing) packet of rice costs Bi rupees and contains 2i-1 kgs of rice. 
Find the minimum amount of money required to buy at least A kgs of rice. You can buy any packet any number of times.
Note :- It is guaranteed that the answer lies between the integer range.

Problem Constraints
1 <= N <= 105
1 <= A <= 109
1 <= Bi <= 109

Input Format
The first argument contains an integer denoting A.
The second argument contains an integer array denoting B.

Output Format
Return a single integer denoting the minimum amount of money required to buy at least A kgs of rice.

Example Input
Input 1:
A = 12
B = [1, 1, 1, 1]
Input 2:
A = 1
B = [2, 1]

Example Output
Output 1:
2
Output 2:
1

Example Explanation
Explanation 1:
Buy 1 packet of the 3rd type(4 kgs of rice) with cost 1 and 
Buy 1 packet of the 4th type(8 kgs of rice) with cost 1.
So the total amount of rice bought is 12 with a cost of 2.

Explanation 2:
Buy 1 packet of the 2nd type(2kgs of rice) with cost 1.
This is the minimum amount required to buy atleast 1 kg of rice.

CODE:

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
