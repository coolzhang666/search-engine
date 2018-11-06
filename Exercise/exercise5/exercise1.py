def max_math_segment(line, dic, max_size):
    chars = line
    i = 0
    words = []
    idx = 0
    while idx < len(chars):
        matched = False
        for i in range(max_size, 0, -1):
            cand = chars[idx:idx + i]
            if cand in dic:
                words.append(cand)
                matched = True
                break
        if not matched:
            i = 1
            words.append(chars[idx])
        idx += i
    return words


if __name__ == "__main__":
    str = "中华民族从此站起来了"
    dic = ["中华", "中华民族", "从此", "站起来"]
    result = max_math_segment(str, dic, 5)
    print(result)
