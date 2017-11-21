'''

by xlc time:2017-11-17 17:03:45
'''
import sys
sys.path.append('D:/mypyfunc')
import json
import pandas
from pandas import DataFrame


if __name__ == '__main__':
    f = open(r"D:\github\FreshPython\result.txt", 'r', encoding='utf-8')
    lenth = set()
    count = 0
    result = []
    for line in  f:
        dct = {'选文题目': '', '创建时间': '', '收藏次数': '', '上传用户': '', '题目': '', \
       '题目编号': '', '浏览次数': '', '上传时间': '', '考点详细': '', \
       '命题类型': '', '质量平均': '', '是否推荐': '', '难度平均': '', \
       '所考词语': '', '使用次数': ''}
        lst = json.loads(line)
        tm = lst[0] # 题目
        #print(tm)
        sx = lst[1] # 属性
        new_sx = {}
        for i in range(len(sx)):
            key = sx[i].split('：')
            new_sx[key[0]] = key[1]
        dct['选文题目'] = tm[0]
        dct.update(new_sx)
        if lst[2] != []:
            dct['试题内容'] = lst[2][0]
        else:
            dct['试题内容'] = ''
        if lst[3] != []:
            dct['答案'] = lst[3][0]
        else:
            dct['答案'] = ''
        #print(dct)
        count += 1
        result.append(dct)
    df = DataFrame(result) # 创建一个DataFrame
    shape = df.shape[0]
    f = open('toexcel.txt', 'w', encoding='utf-8')
    for i in range(shape):
        data = df.iloc[i]
        excel_data = data.tolist()
        file_data = '\t'.join(excel_data)
        f.write(file_data + '\n')
    f.close()
        
        
    
    
        
            
