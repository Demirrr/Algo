# Divide and Conqure
import math


def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    # Left part
    L = [arr[p + i] for i in range(n1)]
    # Right part
    R = [arr[q + 1 + i] for i in range(n2)]

    i, j, k = 0, 0, p
    # Rethin
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted


def merge_sort(input_array, p, r):
    if p < r:
        m = math.floor((p + r) / 2)
        merge_sort(input_array, p, m)
        merge_sort(input_array, m + 1, r)
        merge(input_array, p, m, r)


# Driver code to test above
A = [-1, 1, 3, 8, 2, 11]
merge_sort(A, 0, len(A) - 1)
print(A)
