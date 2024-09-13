# Binary Search

def binarySearch(A, t):
    n = len(A)
    i, j = 0, n - 1
    while i <= j:
        m = (i+j) // 2
        if A[m] == t:
            return m
        elif A[m] < t:
            i = m + 1
        else:
            j = m - 1

array = [1, 2, 3, 4, 7, 8, 9, 12, 13, 14, 15, 16, 18, 19, 22, 23, 27, 28, 29, 30, 33, 35, 36, 41, 42, 43, 44, 47, 49, 50, 55, 56, 57, 58, 60, 61, 62, 63, 64, 68, 69, 70, 71, 72, 73, 75, 76, 78, 79, 83, 84, 86, 87, 88, 89, 90, 93, 94, 96, 98]
t = 33
q2 = binarySearch(array, t);
print(q2 - 1)
print(len(array))
index = 21
print(array[index - 1])

# had to -1 bc of the way python index starts at 0, when our array starts at 1