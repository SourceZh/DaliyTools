from urllib import request
from bs4 import BeautifulSoup
import json

if __name__ == "__main__":
    webpare = json.load(open("../Web.json"))
    head = {'User-Agent': webpare['User-Agent']}
    req = request.Request("https://bbs.pku.edu.cn/v2/thread.php?bid=322&mode=single", headers=head)
    res = request.urlopen(req)
    html = BeautifulSoup(res.read().decode("utf-8"), "lxml")
    latest = html.find("div", class_="list-item-single list-item")
    id = latest.find("div", class_="id l").string
    file = open("temp", "r")
    oldid = file.readline()
    file.close()
    if oldid != id:
        file = open("temp", "w")
        file.write(id)
        file.close()
        print("some topic new in eecs!")
        print(latest.find("div", class_="title l limit").string)
    else:
        print("nothing new")
