def find_i_bs(endtimes, target):
    """
    BINARY SEARCH: finds the index with the largest end time < job[start time]
    """
    l, r = 0, len(endtimes) - 1
    mid = 0

    while l <= r:
        # edge case to save some time
        if target >= endtimes[r]:
            return r + 1

        mid = (l + r) // 2
        mid_num = endtimes[mid]

        if target < mid_num:
            if target >= endtimes[mid - 1]:
                return mid
            r = mid - 1

        elif target >= mid_num:
            l = mid + 1

    return 0


def interval(jobs, endtime, n):
    # zero index is empty by default
    dp = [0] + [0] * n

    for i, job in enumerate(jobs):
        j = i + 1

        # finds closest available request
        prev = find_i_bs(endtime[:i], job[0])

        # max of adding a previous job or not adding
        dp[j] = max(dp[prev] + job[2], dp[i])

    return dp[j]


def main():
    # number of test cases
    instance = int(input())
    res = ""

    for _ in range(instance):
        n = int(input())  # num of jobs
        jobs = []
        endtime = []

        # sanitize input
        for _ in range(n):
            # (start time, finish time, value)
            jobs.append(tuple(map(int, input().split())))

        # sort jobs by increasing end time
        jobs = sorted(jobs, key=lambda job: job[1])
        endtime = [job[1] for job in jobs]

        # run algo
        value = interval(jobs, endtime, n)
        res += f"{value}\n"

    # Get rid of trailing newline char
    print(res.rstrip())


if __name__ == "__main__":
    main()
