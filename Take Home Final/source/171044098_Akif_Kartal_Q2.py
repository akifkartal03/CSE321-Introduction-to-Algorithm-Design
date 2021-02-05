# 171044098
# Akif Kartal
# Final Exam-Q2 Real Code

import random
def main():
    print("---------------------------------------------------------")
    arr = [-1, 6, 4, 2, 3, -7, -5]
    print("Test List:", arr)
    getAllMinValues(arr, len(arr))
    print("---------------------------------------------------------")
    arr = [95, 42, 27, 36, 91, 4, -4, 5]
    print("Test List:", arr)
    getAllMinValues(arr, len(arr))
    print("---------------------------------------------------------")
    arr = [71, 38, 69, 12, 67, 99, 35, 94, 0, 55]
    print("Test List:", arr)
    getAllMinValues(arr, len(arr))
    print("---------------------------------------------------------")
def getAllMinValues(arr, n):
    segtree = [0 for i in range(2 * n)]
    create_segment_tree(segtree, arr, n)
    for i in range(0,n):
        a = random.randint(1,n)
        b = random.randint(a, n)
        printMin(a,b,find_min(segtree,a-1,b,n),i+1)

def printMin(a,b,minimum,k):
    print("--------------",k,"---------------")
    print("Interval : [%d , %d]" % (a,b))
    print("Minimum in this interval:",minimum)

def create_segment_tree(segtree, arr, n):
    for i in range(n):
        segtree[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        if segtree[2 * i] < segtree[2 * i + 1]:
            segtree[i] = segtree[2 * i]
        else:
            segtree[i] = segtree[2 * i + 1]

def find_min(segtree, a, b, n):
    a += n
    b += n
    mi = 1e9 # initialize minimum to a very high value
    while (a < b):
        if (a % 2 == 1):  # if left interval in odd
            mi = min(mi, segtree[a])
            a = a + 1
        if (b % 2 == 1):  # if right interval in odd
            b -= 1
            mi = min(mi, segtree[b])
        # move one level higher
        a = a // 2
        b = b // 2
    return mi
main()