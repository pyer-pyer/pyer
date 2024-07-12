# coding=utf-8
import requests

class Mulu:
    def __init__(self):
        pass


    def duqu_zidian(self,file_path):
        wenjian = []
        # 打开文件，读取文件的所有内容，存在wenjian列表中
        with open(file_path, "r", encoding="utf-8") as f:
            # 遍历列表，将列表中的内容，去掉换行符，存在wenjian列表中
            for i in f.readlines():
                # strip()去除字符串首尾\n
                wenjian.append(i.strip())
        # 把列表中的内容，返回
        return wenjian

    # 获取url
    def get_url(self, url, wenjian):
        # 获取url的内容
        new_url_1 = []
        for i in wenjian:
            # 拼接url
            new_url = "http://" + url + '/' + i
            res = requests.get(new_url)
            if res.status_code == 200 or res.status_code == 302 or res.status_code == 403:
                new_url_1.append(new_url)
        return new_url_1

if __name__ == '__main__':
    mulu = Mulu()
    wenjian = mulu.duqu_zidian("muben.txt")
    url = input("请输入你要扫描的url（不含协议）")
    print(mulu.get_url(url, wenjian))