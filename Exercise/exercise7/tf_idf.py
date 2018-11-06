import jieba


def cut(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    words = list(jieba.cut(content))
    result = list()
    for word in words:
        if word == "，" or word == "？" or word == "\n":
            continue
        result.append(word)
    return result


def deal_docs(file_list):
    docs = list()
    for file in file_list:
        doc = cut(file)
        docs.append(doc)
    return docs


def get_docv(docs):
    docv = list()
    for i, doc in enumerate(docs):
        vec = dict()
        for word in doc:
            if word not in vec:
                vec[word] = 1
            else:
                vec[word] += 1
        docv.append(vec)
    return docv


def tf(docs):
    tf_word = list()
    for i, doc in enumerate(docs):
        doc_count = len(doc)
        tf = dict()
        for word in doc:
            word_count = get_docv(docs)[i][word]
            word_tf = 1.0 * word_count / doc_count
            tf[word] = word_tf
        tf_word.append(tf)
    return tf_word


if __name__ == "__main__":
    file_list = ["files/1.txt", "files/2.txt", "files/3.txt", "files/4.txt"]
    # result = deal_docs(file_list)
    # print(result)
    # a = get_docv(result)
    # print(a)
    # b = tf(result)
    # print(b)
    docs = deal_docs(file_list)
    docv = get_docv(docs)
    tf_word = tf(docs)
    print(tf_word)
