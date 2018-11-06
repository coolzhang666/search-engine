from docx import Document


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


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


def findstr(s1, s2, k):
    set1 = set()
    set2 = set()
    dic1 = getShingle(s1, k)
    dic2 = getShingle(s2, k)

    for i in dic1.keys():
        set1.add(i)

    for i in dic2.keys():
        set2.add(i)

    return set1 & set2


def getindex(string, set1, k):
    set5 = set()
    for i in range(0, len(string) - k + 1):
        s1 = string[i:i + k]
        if s1 in set1:
            for x in range(i, i+k+1):
                set5.add(str(x))
            # set5.add(str(i+1))

    for i in range(0, len(string)):
        s1 = string[i:i+1]
        if str(i) in set5:
            print(bcolors.WARNING + s1 + bcolors.ENDC, end="")
        else:
            print(s1, end="")


if __name__ == "__main__":
    content1 = getdocx("files/testfile1.docx")

    content2 = getdocx("files/testfile2.docx")

    result = findstr(content1, content2, 8)
    print("重复字符串有 %d 个，分别为\n %s" % (len(result), result))
    getindex(content1, result, 8)
