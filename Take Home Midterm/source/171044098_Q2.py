# 171044098
# Akif Kartal
# Q2 Real Code

def main():
    arr = ["0000", "0001", "0010", "0011", "0100",
           "0101", "0110", "0111", "1000", "1010", "1011"]
    print("Absent element is:", find_absent(arr))


def find_absent(A):
    for i in range(0, len(A)):
        size = len(A[i])
        last_bit = A[i][size-1]
        if i % 2 == 0:
            if last_bit == "1":
                return i
        else:
            if last_bit == "0":
                return i
    return -1  # no absent element


main()
