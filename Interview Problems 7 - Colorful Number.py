Colorful Number

Problem Description
Given a number A, find if it is COLORFUL number or not.
If number A is a COLORFUL number return 1 else, return 0.

What is a COLORFUL Number:
A number can be broken into different consecutive sequence of digits. 
The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245. 
This number is a COLORFUL number, since the product of every consecutive sequence of digits is different

Problem Constraints
1 <= A <= 2 * 109

Input Format
The first and only argument is an integer A.

Output Format
Return 1 if integer A is COLORFUL else return 0.

Example Input
Input 1:
 A = 23
Input 2:
 A = 236

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 Possible Sub-sequences: [2, 3, 23] where
 2 -> 2 
 3 -> 3
 23 -> 6  (product of digits)
 This number is a COLORFUL number since product of every digit of a sub-sequence are different. 
Explanation 2:
 Possible Sub-sequences: [2, 3, 6, 23, 36, 236] where
 2 -> 2 
 3 -> 3
 6 -> 6
 23 -> 6  (product of digits)
 36 -> 18  (product of digits)
 236 -> 36  (product of digits)
 This number is not a COLORFUL number since the product sequence 23  and sequence 6 is same. 

CODE:

class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):
        ls = []
        while A > 0:
            rem = A % 10
            # print('rem',rem)
            ls.append(rem)
            A = A // 10

        ls = ls[::-1]
        # print(ls)

        hs = set()
        for i in range(len(ls)):
            prod = 1
            for j in range(i, len(ls)):
                prod *= ls[j]
                if prod in hs:
                    return 0
                else:
                    hs.add(prod)
                    # print(hs)

        return 1


solution = Solution()
print(solution.colorful( A = 236 ))
