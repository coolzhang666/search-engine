import os
import k_shingle
import findstr
from docx import Document


def getdocx(path):
    content = ""
    document = Document(path)
    for p in document.paragraphs:
        content += p.text
    return content


path = r"D:\WorkSpace\PyCharm\Search_Engine\exercise_4\files"
files = list()

for maindir, subdir, file_name_list in os.walk(path):

    for filename in file_name_list:
        apath = os.path.join(maindir, filename)  # 合并成一个完整路径
        files.append(apath)

myfile_path = r"D:\WorkSpace\PyCharm\Search_Engine\exercise_4\files\testfile1.docx"
str1 = getdocx(myfile_path)

for file in files:
    str2 = getdocx(file)
    similarity = k_shingle.getSimilarity(str1, str2, 2)
    if similarity >= 0.6:
        set1 = findstr.findstr(str1, str2, 2)
        print("%s \n和 \n%s \n的文本相似度过高（%.5f），有抄袭嫌疑，重复字符串为：\n" % (myfile_path, file, similarity))
        print(set1)
