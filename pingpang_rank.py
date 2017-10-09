##获取乒乓球选手的世界排名
# url = http://info.sports.sina.com.cn/rank/ittf.php?sina-fr=bd.ala.top.ittf

import re
import urllib.request

from bs4 import BeautifulSoup as bsp

data = urllib.request.\
       urlopen('http://info.sports.sina.com.cn/rank/ittf.php?sina-fr=bd.ala.top.ittf').\
       read()

soup = bsp(data,"html.parser")
table = soup.find('table', width="98%")
all_person = []
for tag in table.descendants:
        if tag.name == 'tr':
                single = []
                for i in tag.children:
                        if i.name == 'td':
                                single.append(i.text)
                all_person.append(single)
rank_data = all_person[1:]
for i in rank_data:
        begin = int(i[0])
        end = int(i[1])
        fd = begin - end #浮动
        if fd > 0:
                i.append('下降' + str(fd) + '个名次')
        elif fd < 0:
                i.append('提升' + str(abs(fd)) + '个名次')
        else:
                i.append('不变')
