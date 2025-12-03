# implement binary search based on pseudocode in docs

def binary_search(array, K):
    n = len(array)
    # establish low and high search bounds
    l,r = 0,n-1
    while l <= r:
        # find and compare key K with middle value
        m = (l+r)//2
        if K == array[m]: return m
        elif K < array[m]: r = m-1
        else: l = m+1
    return -1 # not found