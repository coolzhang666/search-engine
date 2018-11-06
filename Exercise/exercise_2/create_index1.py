def create_index1(filename):
    """
    多文件建立索引函数
    :param filename: a file name
    :return: a dictionary of index
    """
    a = list()
    dic = dict()
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                line = line.strip("\n")
            else:
                a.append(line.split())

    for line in a[0:]:
        book_id = line[0]
        for j in line[1:]:
            if not dic.get(j):
                dic[j] = list()
            dic[j].append(book_id)

    return dic


if __name__ == "__main__":
    dic = create_index1("text/text.txt")
    print(dic)
