def addingBinary(A=[], B=[]):
    C = []
    sum = 0
    carry = 0
    for x in range(len(A)-1, -1, -1):
        sum = A[x] ^ B[x]
        C.insert(0, (sum + carry) % 2)
        # used kmap to get it
        carry = (carry and (A[x] or B[x]) or (A[x] and B[x]))

    C.insert(0, carry)
    return C
