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


if __name__ == "__main__":
    list = []
    list = [int(x) for x in input("enter your list of ints : ").split()]
    merge_sort(0, len(list)-1, list)
    print(list)
