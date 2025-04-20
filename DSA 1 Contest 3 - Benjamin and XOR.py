Benjamin and XOR

Problem Description

In the picturesque town of Bitville, nestled amidst rolling hills and shimmering lakes, the residents had a deep fascination with the world of bits and binary operations. 
The townsfolk were avid mathematicians, always seeking new puzzles to unravel and insights to gain.
One sunny morning, the towns esteemed professor of mathematics, Dr. Benjamin, presented a captivating challenge to his students. 
He introduced them to an array A of N integers, representing a sequence of numbers with each element holding a special significance.
Dr. Benjamin explained that the students' task was to analyze the array and determine the count of pairs that satisfied a unique condition. 
The condition revolved around the XOR operation on the ith bit of the pair's elements. The goal was to count the pairs for which the xor of the ith bit resulted in one. 
You have to answer for Q queries given in array B, each query B[i] denotes the index for which you need to find the count of pairs with xor of that index equals 1.

Can you solve the task given by Dr. Benjamin?
Please read the examples given below for better understanding of the problem.
HINT : Look at the binary representation of given numbers

Problem Constraints
1 <= N <= 4 * 104
1 <= A[i] <= 109
1 <= Q <= 100
0 <= B[i] < 32

Input Format
First argument contains an array A.
Second argument contains an array B.

Output Format
Return an array of integers containing answer to all the queries.

Example Input
Input 1:
A = [1, 2, 3]
B = [0, 1]
Input 2:
A = [2, 4, 7, 11]
B = [3]

Example Output
Output 1:
[2, 2]
Output 2:
[3]

Example Explanation
Explanation 1:
Query with index = 0 means we have to find the total pairs whose XOR have index bit set. 
The corresponding pairs are [[1, 2], [2, 3]].    
Query with index = 1 means we have to find the total pairs whose XOR have 'index' bit set. 
The corresponding pairs are [[1, 2], [1, 3]].

Explanation 2:
Query with index = 3 means we have to find the total pairs whose XOR have 'index' bit set. 
The corresponding pairs are [[2, 11], [4, 11], [7, 11]].

CODE:

 class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def benjamin_XOR(self, A, B):
        c = []
        for i in B:
            idx = i
            
            k = 0
            k1 = 0
            
            for a in A:
                if a >> idx & 1:
                    k += 1
                else:
                    k1 += 1
            
            count = k * k1
            c.append(count)
        return c 


solution = Solution()
print(solution.benjamin_XOR( A = [1, 2, 3], B = [0, 1] ))  -->  O/P: [2, 2]
