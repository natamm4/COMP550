# The input is an array A of n distinct integers sorted in increasing order. Our goal is to
# return an array B such that B contains the squares of the elements of A, and B is sorted in non-decreasing
# order. Describe an O(n)-time algorithm for this problem and analyze its running time. Example: If
# A = [−1, 0, 1, 2], the algorithm should return B = [0, 1, 1, 4].


def ALG(A):
  n = len(A)
  B = [0] * n
  i, j = 0, n - 1
  k = j
  while i <= j:
    if abs(A[i]) > abs(A[j]):
        B[k] = A[i] * A[i]
        i += 1
    else:
        B[k] = A[j] * A[j]
        j -= 1
    k -= 1
  return B

A = [-1, 0, 1, 2]
test_1 = ALG(A)
print(test_1)

B = [-4, 0, 3, 6, 10]
test_2 = ALG(B)
print(test_2)