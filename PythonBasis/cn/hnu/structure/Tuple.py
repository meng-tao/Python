'''
Created on 2014年12月13日

@author: mengtao
'''

# 元组

zoo = ("小猪", "小猴");
print("长度：", len(zoo));

newZoo = ("大象", "羊", zoo);
print("长度：", len(newZoo));

# 输出
print(zoo[1]);
print(newZoo[2][0])

name = "小猪";
age = 2;
print ("%s今年%d岁了" % (name, age));

print("%s在努力学习python" % (name));