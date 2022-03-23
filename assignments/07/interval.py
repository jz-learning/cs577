def find_i(jobs: list[tuple], job: tuple, n: int) -> int:
    """
    finds the index with the largest end time < job[start time]
    """
    start = job[0]
    for i in range(n - 1, -1, -1):
        if jobs[i][1] <= start:
            # need + 1 since dp has an extra blank space in the begining
            return i + 1
    return 0


def interval(jobs, n):
    # zero index is empty by default
    dp = [0] + [0] * n

    for i, job in enumerate(jobs):
        j = i + 1

        # finds closest available request
        prev = find_i(jobs, job, i)

        count = dp[prev] + job[2]
        no_count = dp[i]
        # print(i, job, count, no_count)
        dp[j] = max(count, no_count)

    return dp[j]


def main():
    # number of test cases
    instance = int(input())
    res = ""

    for _ in range(instance):
        n = int(input())  # num of jobs
        jobs = []

        # sanitize input
        for _ in range(n):
            # (start time, finish time, value)
            request = tuple(map(int, input().split()))
            jobs.append(request)

        # sort jobs by increasing end time
        jobs = sorted(jobs, key=lambda job: job[1])

        # run algo
        value = interval(jobs, n)
        res += f"{value}\n"

    # Get rid of trailing newline char
    print(res.rstrip())


if __name__ == "__main__":
    main()
