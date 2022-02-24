res = ""


def eviction_strat(cache: set):
    cache.pop()


# First input shows how many instances
for _ in range(int(input())):

    # size of cache
    size = int(input())
    # total request size
    num_page = int(input())
    # all requests
    pages = input().split()

    cache = set()
    faults = 0

    for page in pages:
        # don't care if page is in the cache, nothing happens
        if page not in cache:
            # only in the begining will the cache be not full
            if len(cache) >= size:
                eviction_strat(cache)

            cache.add(page)
            faults += 1

    res += f"{faults}\n"

print(res)
