import jieba
import math


class tf_idf:
    def __init__(self, file_list):
        self.file_list = file_list  # 文件列表
        self.docs = None  # 分词之后的分档列表
        self.docv = None  # 文档词频
        self.tf = None  # tf列表
        self.word2df = None  # 包含各个单词的文档库
        self.idf = None  # idf
        self.tf_idf = None
        self.deal_files()
        self.get_docv()
        self.get_tf()
        self.get_word2df()
        self.get_idf()
        self.get_tf_idf()

    def deal_files(self):
        docs = list()
        for file in self.file_list:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
            words = list(jieba.cut(content))
            doc = list()
            for word in words:
                if word == "，" or word == "？" or word == "\n":
                    continue
                doc.append(word)
            docs.append(doc)
        self.docs = docs

    def get_docv(self):
        docv = list()
        for i, doc in enumerate(self.docs):
            vec = dict()
            for word in doc:
                if word not in vec:
                    vec[word] = 1
                else:
                    vec[word] += 1
            docv.append(vec)
        self.docv = docv

    def get_tf(self):
        tf_word = list()
        for i, doc in enumerate(self.docs):
            doc_count = len(doc)
            tf = dict()
            for word in doc:
                word_count = self.docv[i][word]
                word_tf = 1.0 * word_count / doc_count
                tf[word] = word_tf
            tf_word.append(tf)
        self.tf = tf_word

    def get_word2df(self):
        word2df = dict()
        for i, doc in enumerate(self.docs):
            for word in doc:
                if word not in word2df:
                    word2df[word] = []
                    word2df[word].append(i)
                else:
                    word2df[word].append(i)

        for key in word2df:
            word2df[key] = len(set(word2df[key]))
        self.word2df = word2df

    def get_idf(self):
        idf_word = {}
        docs_count = len(self.docs)
        for word in self.word2df:
            idf_word[word] = math.log(docs_count / (self.word2df[word] + 1))
        self.idf = idf_word

    def get_tf_idf(self):
        word_tfidf = dict()
        for word_vec in self.tf:
            for word in word_vec:
                word_tfidf[word] = 1.0 * word_vec[word] * self.idf[word]
        self.tf_idf = word_tfidf


if __name__ == "__main__":
    file_list = ["files/1.txt", "files/2.txt", "files/3.txt", "files/4.txt"]
    a = tf_idf(file_list)
    print(a.tf_idf)
    key = list()
    value = list()
    for i in a.tf_idf:
        key.append(i)
        value.append(a.tf_idf[i])


    def get_cos(key, value, doc):
        demo = dict()
        for i in key:
            demo[i] = 0
        for j in doc:
            if j in demo:
                demo[j] += 1

        sum = 0
        for i in demo:
            sum += demo.get(i) * a.tf_idf.get(i)
        # print(sum)

        A = 0
        for i in a.tf_idf:
            A += pow(a.tf_idf.get(i), 2)
        A = math.sqrt(A)
        # print(A)

        B = 0
        for i in demo:
            B += pow(demo.get(i), 2)
        B = math.sqrt(B)
        # print(B)

        fenmu = A * B
        cos = sum / fenmu
        print(cos)


    for i in a.docs:
        get_cos(key, value, i)
