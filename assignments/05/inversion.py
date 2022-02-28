def merge_count(arr1, arr2):
    merged, count, l, r = list(), 0, 0, 0

    while l < len(arr1) and r < len(arr2):
        if arr2[r] < arr1[l]:
            merged.append(arr2[r])
            count += len(arr1)
            r += 1
        else:
            merged.append(arr1[l])
            l += 1

    if l == len(arr1):
        merged.extend(arr2[r:])
    elif r == len(arr2):
        merged.extend(arr1[l:])

    return (merged, count)


def inversion(n, arr):
    # base case
    if n == 1:
        return (arr, 0)

    mid = n // 2

    front = arr[:mid]
    back = arr[mid:]

    A, ctA = inversion(mid, front)
    B, ctB = inversion(n - mid, back)

    C, ctC = merge_count(A, B)

    return (C, ctA + ctB + ctC)


def main():
    # number of test cases
    instance = int(input())

    res = ""
    for _ in range(instance):
        n = int(input())  # input array length

        # sanitize input
        arr = [int(i) for i in input().split()]  # main array of ints

        _, count = inversion(n, arr)
        res += f"{count}\n"

    # Get rid of trailing newline char
    return res[:-1]


if __name__ == "__main__":
    sol = main()

    print(sol)
