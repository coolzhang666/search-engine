import string


def create_index(filename):
    """
    单文件中字符串索引建立
    :param filename: a file name
    :return: a dictionary of index
    """
    a = list()
    dic = dict()
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip("\n")
            for c in string.punctuation:
                line = line.replace(c, "")
            a.extend(line.split())
    print(a)
    for i in range(len(a)):
        text = a[i]
        if not dic.get(text):
            dic[text] = list()
        dic[text].append(i)

    return dic


if __name__ == "__main__":
    dic = create_index("text/text1.txt")
    print(dic)
