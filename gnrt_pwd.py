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
uper_asc = range(65,91) #大学字母
lower_asc = range(97,123) #小写字母

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
