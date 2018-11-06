'''

by xlc time:2018-11-06 14:45:19
'''
import sys
#sys.path.append('D:/svn_codes/source/public_fun')
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])
from bs4 import BeautifulSoup as bsp
from pandas import DataFrame
#&kindid=0&page=2.htm

def get_info(html):
#if __name__ == '__main__':
    #html = open('./qwer.txt', 'r', encoding='utf-8').read()
    soup = bsp(html, 'lxml')
    # 获取所有table
    tables = soup.find_all('table', {'align':'center', 'border':'0'})
    for i in tables:
        if '电话' in i.text and '地址' in i.text:
            the_table = i
            break
    # 获取核心table
    target_table = the_table.find_all('table')
    # 获取`tr`
    trs = target_table[0].find_all('tr')
    result = []
    td_dct = {}
    for i in trs[1: ]:
        tds = i.find_all('td')
        td_data = [i.text.strip() for i in tds]
        td_dct[td_data[0]] = td_data[1]
    del td_dct['']
    result.append(td_dct)
    return td_dct

def gnrt_url():
    # 生成所有解析网址
    fix = '&kindid=0&page=%s.htm'
    f = open('some_url.txt', 'r', encoding='utf-8')
    data = [i.strip().split(': ') for i in f]
    for i in data:
        ff = open(i[0]+'/all_url.txt', 'w', encoding='utf-8')
        ff.write(i[1]+'\n')
        for idx in range(2, 300):
            url = i[1][:-4] + fix%str(idx)
            ff.write(url+'\n')
        ff.close()
            
        
    
