import math
import jieba


# 生成摘要类
class CreateAbstract:

    def __init__(self, data, kv):
        self.data = data[0]
        self.tfidf = MyTfIdf(data)
        self.kv = kv

    def s_match(self, s, s1):
        loc = list()
        l_s = len(s)
        l_s1 = len(s1)
        for i in range(l_s - l_s1 + 1):
            index = i
            for j in range(l_s1):
                if s[index] == s1[j]:
                    index += 1
                else:
                    break
            if index - i == l_s1:
                loc.append(i)
        return loc

    def getLoc(self, keywords):
        locList = list()
        for kw in keywords:
            ll = self.s_match(self.data, kw)
            locList.extend(ll)
        locList.sort()
        # print('关键词的位置', locList)
        return locList

    def getShingle(self, locList):
        txtLine = list()
        for l in locList:
            txtLine.append(self.data[l:l + self.kv])
        # print('得到的窗口信息', txtLine)
        return txtLine

    def getScore(self, tfidfV, shingles, keywords):
        score = dict()

        for i, v in enumerate(shingles):
            if not score.get(i):
                score[i] = 0
            for keyw in keywords:
                if keyw in v:
                    score[i] += v.count(keyw) * tfidfV[keyw]

        sortedDic = sorted(score.items(), key=lambda t: t[1], reverse=True)
        # print('窗口得分', sortedDic)
        return sortedDic

    def getResult(self, keywords):
        _keywords = keywords.split(' ')
        tfidfV = self.tfidf.getTfIdfValues()
        # print('tfidf的分数', tfidfV)

        locList = self.getLoc(_keywords)
        txtLine = self.getShingle(locList)
        scores = self.getScore(tfidfV, txtLine, _keywords)
        maxShinge = txtLine[scores[0][0]]
        return maxShinge


class MyTfIdf:
    def __init__(self, s):
        self.s = s

    def fenci(self, s):
        seg_list = jieba.cut(s)
        result = []
        for seg in seg_list:
            seg = ''.join(seg.split())
            if (seg != '，' and seg != '？' and seg != '。'
                    and seg != "\n" and seg != "\n\n"):
                result.append(seg)
        return result

    def getCount(self, data):
        docCount = list()
        for i, word in enumerate(data):
            vec = dict()
            for w in word:
                if not vec.get(w):
                    vec[w] = 1
                else:
                    vec[w] += 1
            docCount.append(vec)
        return docCount

    def tf(self, data):
        tf_word = []
        for i, doc in enumerate(data):
            docLen = len(doc)
            tf = dict()
            for w in doc:
                tf[w] = doc[w] / docLen
            tf_word.append(tf)
        return tf_word

    def countWinDoc(self, data):
        countDic = dict()
        for i, v in enumerate(data):
            for w in v:
                if not countDic.get(w):
                    countDic[w] = set()
                countDic[w].add(i)
        return countDic

    def idf(self, data, docLen):
        idfDic = dict()
        for d in data:
            idfDic[d] = math.log(docLen / len(data[d]) + 1)
        return idfDic

    def tfIdf(self, tf, idf):
        tfidf = list()
        for t in tf:
            _tfidf = dict()
            for w in t:
                _tfidf[w] = 1.0 * t[w] * idf[w]
            tfidf.append(_tfidf)
        return tfidf

    def getTfIdfValues(self):
        if self.s:
            cut_s = list()
            for v in self.s:
                cut_s.append(self.fenci(v))
            tfCount = self.getCount(cut_s)
            tf_result = self.tf(tfCount)
            idfCount = self.countWinDoc(cut_s)
            idf_result = self.idf(idfCount, len(self.s))
            tfIdfValue = self.tfIdf(tf_result, idf_result)
            return tfIdfValue[0]


if __name__ == '__main__':
    stxt = [
        '搜索引擎包含了各个学科的概念和知识，这些学科包含了计算科学，数学，心理学等，'
        '特别是数学几乎在搜索引擎的各个系统都大量使用，例如布尔代数，概率论，数理统计等，'
        '这些数学知识的应用为搜索引擎解决了一个个的难题，最终使得搜索技术走向成熟。']
    keywords = '搜索引擎 数学'
    kView = 40
    abst = CreateAbstract(stxt, kView)
    txt = "这些学科包含了计算机科学，" + abst.getResult(keywords)[:30]
    print('摘要的内容:  ', txt)
