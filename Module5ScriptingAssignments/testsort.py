def isSorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def testIsSorted():
    assert isSorted([]) == True
    assert isSorted([1]) == True
    assert isSorted([1, 2]) == True
    assert isSorted([2, 1]) == False
    assert isSorted([1, 2, 3, 4, 5]) == True
    assert isSorted([1, 3, 2, 4, 5]) == False
    assert isSorted([1, 1, 2, 2, 3, 3]) == True
    assert isSorted([5, 4, 3, 2, 1]) == False

testIsSorted()
