# The input is an array A of n positive integers. Our goal is to return indices (i, j) such that
# i < j and (j − i) · min(A[i], A[j]) is maximized. Describe an O(n)-time algorithm for this problem, 
# briefly explain why it’s correct, and analyze its running time.

def ALG(A):
  i, j = 0, len(A) - 1
  res_i, res_j = i, j
  while i < j:
    curr = (res_j - res_i) * min(A[res_i], A[res_j])
    if (j - i) * min(A[i], A[res_j]) > curr:
        res_i = i
    if (j - i) * min(A[res_i], A[j]) > curr:
        res_j = j
    i += 1
    j -= 1
  return res_i, res_j

A = [4, 3, 7, 8, 10, 0]
test_1 = ALG(A)
print(test_1)