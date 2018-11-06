import time


def kmp_search(text_string, pat_string):
    time1 = time.perf_counter()
    next = get_next(pat_string)
    print(next)
    i = 0
    j = 0
    while i < len(text_string) and j < len(pat_string):
        if j == -1 or text_string[i] == pat_string[j]:
            i += 1
            j += 1
        else:
            j = next[j]

    if j >= len(pat_string):
        print(time.perf_counter() - time1)
        return i - len(pat_string)
    else:
        print(time.perf_counter()-time1)
        return 0


def get_next(pat_string):
    i = 0
    next = [-1, ]
    j = -1
    while i < len(pat_string) - 1:
        if j == -1 or pat_string[i] == pat_string[j]:
            i += 1
            j += 1
            next.append(j)
        else:
            j = next[j]
    return next


if __name__ == "__main__":
    text_string = "bacbababadababacambabacaddababacasdsd"
    pat_string = "ababaca"
    result = kmp_search(text_string, pat_string)
    print(result)
