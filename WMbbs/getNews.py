from urllib import request
from bs4 import BeautifulSoup
import json

if __name__ == "__main__":
    webpare = json.load(open("../Web.json"))
    head = {'User-Agent': webpare['User-Agent']}
    req = request.Request("https://bbs.pku.edu.cn/v2/hot-topic.php", headers=head)
    res = request.urlopen(req)
    html = BeautifulSoup(res.read().decode("utf-8"), "lxml")
    top100 = html.find("div", id="list-content").find_all("div", class_="list-item list-item-topic")
    index = 1
    for topic in top100:
        title = topic.find("div", class_="title l limit").string
        board = topic.find("div", class_="board l limit").string
        author = topic.find("div", class_="name limit").string
        time = topic.find("div", class_="time").string
        output = "%03d:%-30s 版面:%s 作者:%s" % (index, title, board, author)
        print(output)
        index += 1
        if index > 20:
            break


