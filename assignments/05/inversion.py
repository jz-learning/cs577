def merge_count(arr1, arr2):
    merged, count, i, j = [], 0, 0, 0
    l, r = len(arr1), len(arr2)

    # merge sort
    while i < l and j < r:
        # increase count by 1 if merging from the right array
        if arr2[j] < arr1[i]:
            merged.append(arr2[j])
            count += l - i
            j += 1
        else:
            merged.append(arr1[i])
            i += 1

    # add remaining elements once the other reaches the end
    # all elements here are the largest onces, so they won't increase count
    if i == l:
        merged.extend(arr2[j:])
    elif j == r:
        merged.extend(arr1[i:])

    return merged, count


def inversion(n, arr):
    # base case
    if n == 1:
        return (arr, 0)

    # split array into halves
    mid = n // 2
    front = arr[:mid]
    back = arr[mid:]

    # recursion
    A, ctA = inversion(mid, front)
    B, ctB = inversion(n - mid, back)

    # merge
    C, ctC = merge_count(A, B)
    total_count = ctA + ctB + ctC

    return C, total_count


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
    return res.rstrip()


if __name__ == "__main__":
    print(main())
