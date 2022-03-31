def knapsack(items, cap):
    dp = [0] * (cap + 1)
    dp[0] = 0
    n = len(items)

    for i in range(n):
        weight, value = items[i]
        for j in range(cap, weight, -1):
            dp[j] = max(dp[j - weight] + value, dp[j])

    return dp[cap]


def main():
    # number of test cases
    instance = int(input())
    res = ""

    for _ in range(instance):
        items = []
        n, cap = map(int, input().split())

        for _ in range(n):
            items.append(list(map(int, input().split())))

        value = knapsack(items, cap)
        res += f"{value}\n"

    # Get rid of trailing newline char
    print(res.rstrip())


if __name__ == "__main__":
    main()
