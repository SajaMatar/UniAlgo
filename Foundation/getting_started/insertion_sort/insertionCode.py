def insertionSort(array=[]):
    for x in range(1, len(array), 1):
        key = array[x]
        i = x - 1
        while i > -1 and array[i] > key:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key
