# Merge Sort

def mergeSort(A):
    n = len(A)
    if n == 1:
        return A
    k = n // 2
    a_L = mergeSort(A[1 : k])
    a_R = mergeSort(A[k + 1 : n])
    i, j, B = 1, 1, []
    while i <= k and j <= n - k:
        if a_L[i] <= a_R[j]:
            B.append(a_L[i])
            i += 1
        else:
            B.append(a_R[j])
            j += 1
    if i > k:
        B.append(a_R[j : n - k])
    else:
        B.append(a_L[i : k])
    A = B
    return A