# 171044098
# Akif Kartal
# HW5-Q2 Real Code


def main():

    print("------------------------------------------------------")
    triangle = [[2],
                [5, 4],
                [1, 4, 7],
                [8, 6, 9, 6]]
    print("Test Triangle: ", triangle)
    print("Smallest Sum Path: ",smallest_sum_path(triangle))
    print("------------------------------------------------------")
    triangle = [[5],
                [3, 4],
                [9, 8, 1],
                [4, 5, 8, 2]]
    print("Test Triangle: ", triangle)
    print("Smallest Sum Path: ", smallest_sum_path(triangle))
    print("------------------------------------------------------")


def smallest_sum_path(triangle):
    size = len(triangle)
    for i in range(size - 2, -1, -1):
        for j in range(0, i+1):
            if (triangle[i + 1][j] < triangle[i + 1][j + 1]):
                triangle[i][j] = triangle[i][j] + triangle[i+1][j]
            else:
                triangle[i][j] = triangle[i][j] + triangle[i+1][j+1]
    return triangle[0][0]

main()
