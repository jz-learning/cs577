def ff(cache: set, positions: dict):
    """
    evicts the furthest-in-future element from cache
    """

    # keeps track of the furthest page
    furthest = {"loc": -1, "page": ""}

    for c in cache:
        # list of positions of where c will occur in the future
        occur = positions[c]

        if not occur:
            cache.discard(c)
            return

        # the next time c will appear in the page sequence
        next_loc = occur[0]

        if next_loc > furthest["loc"]:
            furthest["loc"] = next_loc
            furthest["page"] = c

    cache.discard(furthest["page"])


def find_positions(pages: list) -> dict:
    """
    Returns a dict with each page and where their locations are in the sequence
    """

    result = dict()

    for i, page in enumerate(pages):
        if page not in result:
            result[page] = []

        result[page].append(i)

    return result


def main():
    res = ""
    # First input shows how many instances
    for _ in range(int(input())):

        size = int(input())  # size of cache
        _ = input()  # total request size
        pages = input().split()  # all requests

        faults = 0
        cache = set()
        positions = find_positions(pages)

        for page in pages:
            positions[page].pop(0)
            # don't care if page is in the cache, nothing happens
            if page in cache:
                continue

            # only in the begining will the cache be not full
            if len(cache) >= size:
                ff(cache, positions)

            cache.add(page)
            faults += 1

        res += f"{faults}\n"

    # gets rid of last new line char
    print(res[:-1])


if __name__ == "__main__":
    main()
