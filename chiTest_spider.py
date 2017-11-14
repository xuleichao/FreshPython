'''

by xlc time:2017-11-13 17:04:33
'''
import sys
sys.path.append('D:/mypyfunc')
from bs4 import BeautifulSoup as bsp
import re
import urllib.request
import json
import time


if __name__ == '__main__':
    f = open('result.txt', 'w', encoding='utf-8')
    for num in range(1, 26189):
        try:
            url = 'http://www.gzywtk.com/tmshow/' + str(num) + '.html'
            ywst = urllib.request.\
                   urlopen(url).\
                   read()
            answer = '<a href=\"/tmshow/1\.html\">(.*?)</a>'
            soup = bsp(ywst, 'lxml')
            mydiv = soup.find('div', id='pageroot') #获得主要分支
            #title = soup.find('h1', attrs={'class':'title'})
            title = soup.find('ul', attrs={'class':'tmshowul'}) #获得字段
            for tag in mydiv.descendants:
                c = soup.find('h1', attrs={'class':'title'})
                break
    
            tag_data = title.text.split('\n')
            tag_data = [i for i in tag_data if i != '']
            r_shiti = soup.find('div', attrs={'class':'content'}) #获得试题
            shiti = soup.find_all('div', attrs={'class':'content'}) #获得试题及答案
            answer_data = re.findall(answer, str(shiti))
            result = [[c.text], tag_data, [r_shiti.text], answer_data]
            f.write(json.dumps(result, ensure_ascii=False))
            f.write('\n')
        except:
            pass
    f.close()
        
        
    
    
