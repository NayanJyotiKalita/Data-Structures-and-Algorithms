Maximum AND Pair

Problem Description: Given N +ve array elements. Find the maximum value of ( arr[ i ] & arr[ j ] ) where i ! = j ( indices must be different for 2 number )

CODE:

ans = 0
for i in range(31, -1, -1):
  count = 0
  for j in range(len(A)):
    if A[j] & (1 << i) > 0:
      count += 1

  if count >= 2:
    for j in range(len(A)):
      if A[j] & (1 << i) == 0:
        A[j] = 0
    # print(A)
    ans = ans | (1 << i)
