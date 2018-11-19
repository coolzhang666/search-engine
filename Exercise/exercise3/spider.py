import requests
from bs4 import BeautifulSoup
import re


def save(text, name, type):
    with open(name, type, encoding="utf-8") as f:
        f.write(text)


def get_url(soup, name):
    lk = soup.find_all("a")
    links = ""
    for i in lk:
        link = i.get("href")
        if not (link is None):
            if "http" in link:
                links += link + "\n"
    save(links, name, "w")


def get_image(soup):
    img = soup.find_all("img")
    for i in img:
        flag = i.get("src")
        if not (flag is None):
            if "http" in flag:
                image = requests.get(flag, allow_redirects=False)
                with open("image/"+flag.split("/")[-1], "wb") as f:
                    f.write(image.content)


def get_content(soup, name):
    # [s.extract() for s in soup.find_all('script')]
    r = re.compile(r'''<script.*?</script>''', re.I | re.M | re.S)
    r1 = re.compile(r'''<style.*?</style>''', re.I | re.M | re.S)
    reg1 = re.compile("<[^>]*>")
    content = r.sub('', soup.prettify())
    content = r1.sub('', content)
    content = reg1.sub("", content)
    content = content.replace(" ", "")
    save(content, name, "w")

    content1 = ""
    with open("content.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line == "\n":
                line = line.strip("\n")
            else:
                content1 += line

    save(content1, name, "w")


if __name__ == "__main__":
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple"
                      "WebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    url = r"https://baike.baidu.com/item/搜索引擎"

    resp = requests.get(url, headers=header)
    resp.encoding = "utf-8"

    beautifulSoup = BeautifulSoup(resp.text, 'html.parser')
    get_content(beautifulSoup, "content.txt")
    get_url(beautifulSoup, "links.txt")
    get_image(beautifulSoup)
