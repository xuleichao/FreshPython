'''
介绍
ASCii码
33-47 符号
48-59 0-9
65-90 大写字母
97-122 小写字母

在shell里试验：输入chr(46),chr(98).
'''

sig_asc = range(33,48) #符号
num_asc = range(48,60) #数字
uper_asc = range(65,91) #大写字母
lower_asc = range(97,123) #小写字母
import random
#写一个函数来生成数字密码
def num_pwd(length=6):#默认密码长度是6
    import random #随机函数
    if length < 6:
        print('请输入大于6的数字')
    else:
        length = int(length)
        pwd = '' #密码字符串
        for i in range(length):
            single_num = random.randint(0,9)
            pwd += str(single_num)
    return pwd

###08.23
def string_pwd(n,with_upper=1): #生成一个n位的随机字符串密码
                                   #可以定义是否大小写，默认有大写
    if with_upper == 1:
        if n < 6:
            print('请输入大于6的数字')
        else:
            length = int(n)
            pwd = '' #密码字符串
            for i in range(length):
                random_asc = random.randint(65,123)
                if random_asc not in range(91,97):
                    asc = chr(random_asc)
                    pwd += asc
                else:
                    pass ##这里有一个bug，要怎么改这个bug,可以试试用while循环来写。
    return pwd

###09.03
def save_pwd(password):
    f = open(r'D:\github\FreshPython\mm.txt','ab')
    f.write(password.encode('utf-8'))
    f.write('\n'.encode('utf-8'))
    f.close()
    
