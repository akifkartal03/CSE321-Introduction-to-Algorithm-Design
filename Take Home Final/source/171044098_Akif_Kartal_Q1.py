# 171044098
# Akif Kartal
# Final Exam-Q1 Real Code

def main():
    print("---------------------------------------------------------")
    arr = "noon"
    rvsArr = arr[::-1]  # reverse array
    subArr = [[0 for x in range(len(arr) + 1)] for y in range(len(arr) + 1)]
    print("Test Array: ", arr)
    print("Length of SubArray: : ", maxLength(arr, rvsArr, len(arr), subArr))
    print("Subarray with maximum length having the property:",
          printPalindromeRecursively(arr, rvsArr, len(arr), len(arr), subArr))
    print("---------------------------------------------------------")
    arr = "racecaris"
    rvsArr = arr[::-1]  # reverse array
    subArr = [[0 for x in range(len(arr) + 1)] for y in range(len(arr) + 1)]
    print("Test Array: ", arr)
    print("Length of SubArray: : ", maxLength(arr, rvsArr, len(arr), subArr))
    print("Subarray with maximum length having the property:",
          printPalindromeRecursively(arr, rvsArr, len(arr), len(arr), subArr))
    print("---------------------------------------------------------")
    arr = "abbdcacb"
    rvsArr = arr[::-1]  # reverse array
    subArr = [[0 for x in range(len(arr) + 1)] for y in range(len(arr) + 1)]
    print("Test Array: ", arr)
    print("Length of SubArray: : ", maxLength(arr, rvsArr, len(arr), subArr))
    print("Subarray with maximum length having the property:", printPalindromeRecursively(arr, rvsArr, len(arr), len(arr), subArr))
    print("---------------------------------------------------------")
    arr = "repapwhat"
    rvsArr = arr[::-1]  # reverse array
    subArr = [[0 for x in range(len(arr) + 1)] for y in range(len(arr) + 1)]
    print("Test Array: ", arr)
    print("Length of SubArray: : ", maxLength(arr, rvsArr, len(arr), subArr))
    print("Subarray with maximum length having the property:",
          printPalindromeRecursively(arr, rvsArr, len(arr), len(arr), subArr))
    print("---------------------------------------------------------")

#recursive helper method to print substring
def printPalindromeRecursively(arr, rvsArr, m, n, subArr):
    if m == 0 or n == 0:
        return ""
    if arr[m - 1] == rvsArr[n - 1]:
        return printPalindromeRecursively(arr, rvsArr, m - 1, n - 1, subArr) + arr[m - 1]
    if subArr[m - 1][n] > subArr[m][n - 1]:
        return printPalindromeRecursively(arr, rvsArr, m - 1, n, subArr)
    return printPalindromeRecursively(arr, rvsArr, m, n - 1, subArr)

#dynamic programming Algorithm to find maximum length having the property that subarray
def maxLength(arr, rvsArr, n, subArr):

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i - 1] == rvsArr[j - 1]:
                subArr[i][j] = subArr[i - 1][j - 1] + 1
            else:
                subArr[i][j] = max(subArr[i - 1][j], subArr[i][j - 1])
    return subArr[n][n]

main()