'''

by xlc time:2017-11-17 17:03:45
'''
import sys
sys.path.append('D:/mypyfunc')
import json

dct = {'选文题目': '', '创建时间': '', '收藏次数': '', '上传用户': '', '题目': '', \
       '题目编号': '', '浏览次数': '', '上传时间': '', '考点详细': '', \
       '命题类型': '', '质量平均': '', '是否推荐': '', '难度平均': '', \
       '所考词语': '', '使用次数': ''}

if __name__ == '__main__':
    f = open(r"D:\github\FreshPython\result6.txt", 'r', encoding='utf-8')
    lenth = set()
    for line in  f:
        lst = json.loads(line)
        tm = lst[0] # 题目
        #print(tm)
        sx = lst[1] # 属性
        new_sx = {}
        for i in range(len(sx)):
            key = sx[i].split('：')
            new_sx[key[0]] = key[1]
        lenth = lenth | set(new_sx.keys())
            
    print(lenth)
