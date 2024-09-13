# Selection Sort

def selectionSort(A):
    n = len(A)
    i = 1
    while i <= n:
        m = i
        j = i + 1
        while j <= n:
            if A[j] < A[m]:
                m = j
        was_i = A[i]
        was_j = A[j]
        A[i] = was_j
        A[j] = was_i