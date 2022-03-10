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


def intersect(n, arr):
    # base case
    if n == 1:
        return (arr, 0)

    # split array into halves
    mid = n // 2
    front = arr[:mid]
    back = arr[mid:]

    # recursion
    A, ctA = intersect(mid, front)
    B, ctB = intersect(n - mid, back)

    # merge
    C, ctC = merge_count(A, B)
    total_count = ctA + ctB + ctC

    return C, total_count


def main():
    # number of test cases
    instance = int(input())

    res = ""
    for _ in range(instance):
        n = int(input())  # length of q or p
        q, p = [], []

        # sanitize input
        for _ in range(n):
            q.append(int(input()))

        for _ in range(n):
            p.append(int(input()))

        # combine the list of q and p so they can be sorted together
        pairs = list(zip(q, p))

        # sort the two respective lists together by Q
        pairs = sorted(pairs, key=lambda pair: pair[0])

        bottom_row = [pair[1] for pair in pairs]

        _, count = intersect(n, bottom_row)
        res += f"{count}\n"

    # Get rid of trailing newline char
    print(res.rstrip())


if __name__ == "__main__":
    main()
