# INPUT: <a_1, a_2, ..., a_n>
# OUTPUT: <b_1, b_2, ..., b_n> s.t. b_1=<b_2=<...,=<b_n

# Incremental Algorithm:
def insertion_sort(A):
    # (1) Iterate over A by starting from the second element
    for i in range(1, len(A)):
        # (2) Consider the i.th element
        key = A[i]
        # (3) Consider the j.th index s.t. j=i-1
        j = i - 1
        # (4) If j.th element is greater than (2) and j is greater than 0
        while j > 0 and A[j] > key:
            # (5) Swap index j+1 with the element pointed with index j
            A[j + 1] = A[j]
            # (6) Decrease the j.th index
            j -= 1
        A[j + 1] = key
    return A


print(insertion_sort([-1, 1, 3, 8, 2, 11]))
