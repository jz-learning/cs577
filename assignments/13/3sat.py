import random


def main():
    # number of variabels
    n = int(input())
    res = ""

    for _ in range(n):
        res += f"{random.choice([1, -1])} "

    # Get rid of trailing newline char
    print(res.rstrip())


if __name__ == "__main__":
    main()
