import math


def merge(p, q, r, A=[]):
    left = p
    right = q + 1

    while left <= r and right <= r:
        if A[left] > A[right]:
            A[left], A[right] = A[right],  A[left]

        left += 1

        if (left >= right):
            right += 1
            left = p


def merge_sort(p, r, A=[]):
    if (p < r):
        mid = math.floor((p+r)/2)
        merge_sort(p, mid, A)
        merge_sort(mid + 1, r, A)
        merge(p, mid, r, A)
