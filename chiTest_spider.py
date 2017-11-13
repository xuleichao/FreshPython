'''

by xlc time:2017-11-13 17:04:33
'''
import sys
sys.path.append('D:/mypyfunc')
from bs4 import BeautifulSoup as bsp
import re
import urllib.request


if __name__ == '__main__':
    ywst = urllib.request.\
           urlopen('http://www.gzywtk.com/tmshow/1.html').\
           read()

    soup = bsp(ywst, 'lxml')
    mydiv = soup.find('div', id='pageroot') #获得主要分支
    #title = soup.find('h1', attrs={'class':'title'})
    title = soup.find('ul', attrs={'class':'tmshowul'}) #获得字段
    for tag in mydiv.descendants:
        c = soup.find('h1', attrs={'class':'title'})
        break
    
