# Problem 1. The input is (G, T, e) where G is a connected, undirected graph with distinct edge weights,
# T is the MST of G, and e is an edge in T . Suppose w(e), the weight of e, increases. (Assume that all edge
# weights are still distinct.) Describe an O(m)-time algorithm that returns the MST of this new graph (i.e.,
# G with one edge weight increased), explain why it’s correct, and analyze its running time.

def weightChange(G, T, e):
    # remove edge e from T, now T is 2 connected parts
    # find new min-weight edge e' b/w the 2 parts of T that doesn't exist in T
    # replace e w/ e'

    # traverse T
    new_T = T
    return M