def frac_knap(v, w, B):
    #sort items by decreasing v[i]/w[i]
    n = len(B)
    i = 1
    while i <= n:
        
        m = i
        j = i + 1
        while j <= n:
            if A[j][1] < A[m][1]:
                m = j
        was_i = A[i][1]
        was_j = A[j][1]
        A[i][1] = was_j
        A[j][1] = was_i
    x = [0] * n
    for each item i:
        increase x[i] by as much as possible
    return x