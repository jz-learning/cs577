res = []

# First input shows how many instances
for _ in range(int(input())):
    # number of total intervals
    num_inter = int(input())

    S = []
    # turn input into dict of lists
    for _ in range(num_inter):
        interval = input().split()
        S.append(interval)

    order = sorted(S, key=lambda [a, b]: b)
    print(order)
