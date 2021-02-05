# 171044098
# Akif Kartal
# Final Exam-Q5 Real Code

def main():
    print("------------------------------------------------------")
    list = [92, 82, 21, 16, 18, 95, 26, 47]
    extra_space = list.copy()
    print("Test List:",list)
    print("Total number of inversions:", getTotalInversion(list, extra_space, 0, len(list) - 1))
    print("------------------------------------------------------")
    list = [3, 11, 22, 33, 73, 64, 41, 11]
    extra_space = list.copy()
    print("Test List:", list)
    print("Total number of inversions:", getTotalInversion(list, extra_space, 0, len(list) - 1))
    print("------------------------------------------------------")
    list = [41, 5, 15, 2, 7]
    extra_space = list.copy()
    print("Test List:", list)
    print("Total number of inversions:", getTotalInversion(list, extra_space, 0, len(list) - 1))
    print("------------------------------------------------------")


def getTotalInversion(list, extraSpace, low, high):

    if high == low:  # base case
        return 0
    mid = low + ((high - low) >> 1)
    total_inversion = 0
    total_inversion += getTotalInversion(list, extraSpace, low, mid)  # split left half
    total_inversion += getTotalInversion(list, extraSpace, mid + 1, high)  # split right half
    total_inversion += combine(list, extraSpace, low, mid, high)  # combine the two half
    return total_inversion
def combine(list, extra_space, low, mid, high):
    k = i = low
    j = mid + 1
    total_inversion = 0

    while i <= mid and j <= high:
        if list[i] > 2*(list[j]): # xi > 2 xj
            total_inversion += (mid - i + 1)
            extra_space[k] = list[j]
            j = j + 1
        else:
            extra_space[k] = list[i]
            i = i + 1

        k = k + 1
    while i <= mid:
        extra_space[k] = list[i]
        k = k + 1
        i = i + 1

    for i in range(low, high + 1):
        list[i] = extra_space[i]
    return total_inversion


main()