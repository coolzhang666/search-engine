import jieba
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def deal():
    dic = dict()
    key_word = ["曹操", "曹孟德", "阿瞒", "刘备", "玄德", "玄德曰", "诸葛亮",
                "孔明", "孔明曰", "关羽", "关公", "张飞", "吕布", "司马懿", "周瑜", "袁绍", "马超", "魏延"]
    with open("sanguo.txt", "r", encoding="utf-8") as f:
        string = f.readlines()

    for lines in string:
        words = list(jieba.cut(lines))
        for word in words:

            if word == "曹孟德" or word == "阿瞒":
                word = "曹操"
            if word == "玄德" or word == "玄德曰":
                word = "刘备"
            if word == "孔明" or word == "孔明曰":
                word = "诸葛亮"
            if word == "关公":
                word = "关羽"

            if word in key_word:
                flag = dic.get(word)
                if flag:
                    dic[word] += 1
                else:
                    dic[word] = 1
    return dic


def show(data):
    x = range(len(data))
    y = list()
    lables = list()
    for i in data:
        lables.append(i[0])
        y.append(i[1])

    plt.bar(x, y)
    plt.xticks(x, lables)
    plt.title("三国人数统计")
    plt.xlabel("英雄人物")
    plt.ylabel("出现次数")
    plt.show()


if __name__ == "__main__":
    result = deal()
    show(result)
