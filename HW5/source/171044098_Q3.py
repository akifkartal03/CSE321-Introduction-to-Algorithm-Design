# 171044098
# Akif Kartal
# HW5-Q3 Real Code


def main():
    print("------------------------------------------------------")
    w = [5, 4, 2]
    v = [10, 4, 3]
    W = 9
    n = len(v)
    print("weights:", w)
    print("values:", v)
    print("W:", W, "and n:", n)
    print("Total value that can fit the knapsack:", different_knapsack(W, n, w, v))
    print("------------------------------------------------------")


def different_knapsack(W, n, w, v):
    K = [int] * (W+1)
    K[0]=0
    for x in range(0,W+1):
        K[x]=0
        for i in range(0,n):
            if (w[i] <= x):
                K[x] = max(K[x], K[x - w[i]] + v[i])
    return K[W]

main()
