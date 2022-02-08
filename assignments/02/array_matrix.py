def print_mtx(arr):
    for i in arr:
        print(i)


def transform(arr):
    """O(n^2) Algo for transforming array into matrix with the sum"""
    n = len(arr)
    res = [n * [0] for _ in range(n)]

    for i in range(n):
        sum = arr[i]
        for j in range(1 + i, n):
            sum += arr[j]
            res[i][j] = sum

    return res


sample = [
    [0, 3, 6, 10],
    [0, 0, 5, 9],
    [0, 0, 0, 7],
    [0, 0, 0, 0],
]

input = [1, 2, 3, 4]
output = transform(input)


print_mtx(output)
