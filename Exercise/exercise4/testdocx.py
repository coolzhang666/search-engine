from docx import Document


def getdocx(path):
    content = ""
    document = Document(path)
    for p in document.paragraphs:
        content += p.text
    return content


if __name__ == "__main__":
    str = getdocx("D:\\WorkSpace\\PyCharm\\Search_Engine\\exercise_4\\files\\a\\1.docx")
    print(str)
