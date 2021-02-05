# 171044098
# Akif Kartal
# Final Exam-Q3 Real Code

def main():
    print("------------------------------------------------------")
    M = 35
    x = [3, 8, 10, 12, 15]
    money = [15, 10, 12, 6, 23]
    n = len(x)
    print("Total Distance:",M)
    print("List of ads Locations:", x)
    print("List of money from ads:", money)
    print("number of ads location:", n)
    print("Your maximized total earned money:",max_money(M, x, money, n))
    print("------------------------------------------------------")
    M = 15
    x = [6, 8, 12, 14, 15]
    money = [3, 6, 5, 3, 5]
    n = len(x)
    print("Total Distance:", M)
    print("List of ads Locations:", x)
    print("List of money from ads:", money)
    print("number of ads location:", n)
    print("Your maximized total earned money:", max_money(M, x, money, n))
    print("------------------------------------------------------")


def max_money(M, x, money, n):
    dp = [0] * (M + 1)
    nextAds=0
    for i in range(1, M + 1):

        if (nextAds >= n):
            dp[i] = dp[i - 1]
        else:
            if (i != x[nextAds]):
                dp[i] = dp[i - 1]
            else:
                if (4 >= i):
                    dp[i] = max(dp[i - 1], money[nextAds])

                elif (x[nextAds - 1] + 4 >= i):
                    dp[i] = max(dp[i - 1], dp[i - 5] + money[nextAds] )
                else:
                    dp[i] = dp[i - 1] + money[nextAds]
                nextAds += 1

    return dp[M]

main()