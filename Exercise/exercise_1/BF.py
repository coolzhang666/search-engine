import time


def bf_search(text_string, pat_string):
    time1 = time.perf_counter()
    i = 0
    j = 0
    while i < len(text_string) and j < len(pat_string):
        if text_string[i] == pat_string[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j >= len(pat_string):
        print(time.perf_counter() - time1)
        return i - len(pat_string)
    else:
        print(time.perf_counter()-time1)
        return -1


if __name__ == "__main__":
    text_string = "bcdejfa;kdjfkabcde"
    pat_string = "abcde"
    result = bf_search(text_string, pat_string)
    print(result)
