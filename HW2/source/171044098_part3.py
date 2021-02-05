# 171044098
# Akif Kartal
# HW2-Part 3 Real Code

# A basic class to keep pairs whose multiplication yields
# the desired numbers.
class Pairs:
    def __init__(self, i1, i2):
        self.x = i1
        self.y = i2

    def print_info(self):
        print("(", self.x, ",", self.y, ")")

    def get_index1(self):
        return self.x

    def get_index2(self):
        return self.y


def main():
    arr = [1, 2, 3, 6, 5, 4]
    mult_pairs = get_multiplication_pairs(arr, 6, 6)
    print("Multiplication Pairs:")
    for pair in mult_pairs:
        pair.print_info()


def get_multiplication_pairs(arr, arr_length, desired_element):
    merge_sort(arr)  # sort array with with merge sort
    down = 0
    up = arr_length - 1
    mult_pair_arr = []
    k = 0
    while down < up:
        mult_result = arr[down] * arr[up]
        if mult_result == desired_element:
            mult_pair_arr.append(Pairs(arr[down], arr[up]))
            down = down + 1
            up = up - 1
        elif mult_result > desired_element:
            up = up - 1
        else:
            down = down + 1
    return mult_pair_arr


def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)


def merge(l, r, a):
    nl = len(l)
    nr = len(r)
    i = 0
    j = 0
    k = 0
    while i < nl and j < nr:
        if l[i] < r[j]:
            a[k] = l[i]
            i = i + 1
        else:
            a[k] = r[j]
            j = j + 1
        k = k + 1
    while i < nl:
        a[k] = l[i]
        i = i + 1
        k = k + 1
    while j < nr:
        a[k] = r[j]
        j = j + 1
        k = k + 1


main()
