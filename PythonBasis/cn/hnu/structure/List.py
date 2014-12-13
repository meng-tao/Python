'''
Created on 2014年12月13日

@author: mengtao
'''

# 列表的使用

testList = ["1test", "4test", "3test"];

# 列表的长度
print("列表的长度：", len(testList));

# 列表的输出
for test in testList:
    print(test);
    
# 列表的添加
testList.append("2test");
print("列表的长度：", len(testList));

# 列表的排序
testList.sort(key=None, reverse=False);
for test in testList:
    print(test);

# 按照索引读取数据
print(testList[0]);

# 列表数据的删除
testList.remove("1test");
del testList[0];
print('删除');
for test in testList:
    print(test);
    

