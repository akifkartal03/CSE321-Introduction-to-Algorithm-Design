# 171044098
# Akif Kartal
# HW5-Q1 Real Code
from collections import deque
number_of_subset = 0
def main():
    global number_of_subset
    subset = deque()
    arr = [2, 3, -5, -8, 6, -1]
    print("------------------------------------------------------")
    print("Test Array: ", arr)
    checkWithBacktracking(arr, len(arr)-1, subset)
    if number_of_subset == 0:
        print("No subset with total sum of elements equal to zero!")
    print("------------------------------------------------------")
    number_of_subset=0
    subset = deque()
    arr = [2, 3, 5]
    print("Test Array: ", arr)
    checkWithBacktracking(arr, len(arr) - 1, subset)
    if number_of_subset == 0:
        print("No subset with total sum of elements equal to zero!")
    print("------------------------------------------------------")
    number_of_subset=0
    subset = deque()
    arr = [95, 42, 27, 36, 91, 4, -4, 5]
    print("Test Array: ", arr)
    checkWithBacktracking(arr, len(arr) - 1, subset)
    if number_of_subset == 0:
        print("No subset with total sum of elements equal to zero!")
    print("------------------------------------------------------")

def checkWithBacktracking(arr,size,subset):
    if(size<0):
        checkSubset(subset)
        return
    # include current element into the subset and call again
    subset.append(arr[size])
    checkWithBacktracking(arr,size-1,subset)
    # don't include current element into the subset and call again
    subset.pop()
    checkWithBacktracking(arr, size - 1, subset)
def checkSubset(subset):
    sum = 0
    global number_of_subset
    for i in subset:
        sum = sum + i;
    if  (sum == 0 and len(subset)>0):
        number_of_subset=number_of_subset+1
        print(number_of_subset,")", end=" ")
        for i in subset:
            print(i,end =", ")
        print("")
main()