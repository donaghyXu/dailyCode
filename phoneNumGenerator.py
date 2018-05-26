
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""
Created on 05/26 2018
author: donaghy

"""
import random
import string
import sys

def phoneNumGenerator(num):
    allPhoneNums = list()    
    # 中国移动 134(0-8)、135、136、137、138、139、147、150、151、152、157、158、159、178、182、183、184、187、188、198、1703、1705、1706
    # 中国联通 130、131、132、145、155、156、166、171、175、176、185、186、1704、1707、1708、1709
    # 中国电信 133、149、153、173、177、180、181、189、199、1700、1701、1702
    numStart = ['134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '157', '158', '159', '178', '182', '183', '184', '187',
                '188', '198', '170', '130', '131', '132', '145', '155', '156', '166', '171', '175', '176', '185', '186', '133', '149', '153',
                '173', '177', '180', '181', '189', '199']
    
    # 生成手机号
    i = 0
    while i < num :
        start = random.choice(numStart)               # 从numStart里随机选择手机号的前三位
        end = ''.join(random.sample(string.digits,8)) # 从数字中随机取8个数，返回一个list,组成手机号的后8位
        res = start + end + '\n'
        if res not in allPhoneNums:
            allPhoneNums.append(res)
            i += 1
            
    # 写入文件
    with open('D:\phoneNumGenerator.xls','w',encoding='utf-8') as f:
        f.writelines(allPhoneNums)

phoneNumGenerator(int(sys.argv[1]))