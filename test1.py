# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 10:55:11 2022

@author: 22570

print函数的使用
1.print函数可以输出数字、字符串、含有运算符的表达式
2.print函数可以将内容输出到显示器和文件
3.print的输出形式有换行和不换行
"""
print(520)
print(98.5)

#字符串必须加引号
print('hello world')
print("hello world")

print(3+22)

#将数据输出到文件中
#注意点：1.所指定的盘存在 2.使用file=fp 3.a+文件不存在会自动创建，存在就在后面追加
fp=open('E:/大三下/py/file1/test1.txt','a+')
print('helloworld',file=fp)
fp.close()

#不进行换行输出
print('hello','world','python')

