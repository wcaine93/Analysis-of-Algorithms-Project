# implement mergesort based on pseudocode in docs

def mergesort(array_a):
    n = len(array_a)
    if n > 1:
        # copy first half of array_a into array_b
        array_b = array_a[:n//2].copy()
        # copy second half of array_a into array_c
        array_c = array_a[n//2:].copy()

        # sort each half recursively and merge together
        mergesort(array_b)
        mergesort(array_c)
        merge(array_b, array_c, array_a)

def merge(array_b, array_c, array_a):
    p = len(array_b)
    q = len(array_c)
    # merge sorted halves back into array_a
    i,j,k = 0,0,0
    while i < p and j < q:
        # put least element into next position in array_a
        if array_b[i] <= array_c[j]:
            array_a[k] = array_b[i]
            i += 1
        else:
            array_a[k] = array_c[j]
            j += 1
        k += 1
    # copy the remainder from the nonempty array into array_a
    if i == p: array_a[k:] = array_c[j:]
    else: array_a[k:] = array_b[i:]