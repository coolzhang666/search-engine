from docx import Document


def getdocx(path):
    content = ""
    document = Document(path)
    for p in document.paragraphs:
        content += p.text
    return content


def getShingle(s, k):
    dic = dict()
    for i in range(0, len(s) - k + 1):
        s1 = s[i:i + k]
        j = dic.get(s1)
        if j:
            dic[s1] += 1
        else:
            dic[s1] = 1
    return dic


def getSimilarity(s1, s2, k):
    if s1 == s2:
        return 1
    set1 = set()
    set2 = set()
    dic1 = getShingle(s1, k)
    dic2 = getShingle(s2, k)

    for i in dic1.keys():
        set1.add(i)

    for i in dic2.keys():
        set2.add(i)

    return 1.0 * len(set1 & set2) / len(set1 | set2)


if __name__ == "__main__":
    content1 = getdocx("files/testfile1.docx")

    content2 = getdocx("files/testfile2.docx")

    similarity = getSimilarity(content1, content2, 2)
    print("两个文本的相似度为：%.5f" % similarity)
