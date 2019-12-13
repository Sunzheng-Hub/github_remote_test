# !/usr/bin/env python
# -*- coding:utf-8 -*-
#
# # 12
# print(ord('B'))  #将字母转换成ASCII码
# print(chr(1238))  #将ASCII数字转换成字母
#
# # 13
# # Unicode转换成字符
# print(u'中文')
# print('中文')
# print(u'\u4e2d')
# # 将Unicode转成其他格式：encode编码
# print(u'中文'.encode('utf-8'))
# print(u'中文'.encode('gb2312'))
# print(u'中文'.encode('gbk'))
# # 将其他编码字符串转成Unicode格式：decode解码
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# print(b'\xd6\xd0\xce\xc4'.decode('gb2312'))
# print(b'\xd6\xd0\xce\xc4'.decode('gbk'))
#
# # 14 占位符使用
# name = '张三'
# bank = '建设银行'
# money = 12345.678
# interest = 56.78956
# suminterest = 576.85876
# print('尊敬的%s您好,欢迎您使用%s,您的账户余额为%d,截止利息为%.3f%%，累计收益%s' % (name, bank, money, interest, suminterest))
# print('%.4f' % 1.333333334)  # 小数点后位数
# print('%04d' % 123.456)  # 输出宽度，不足的用0补齐
# print('%f' % 123.456)

# 15 python内置数据类型
# list相关用法
a = [51, 42, 33, 14, 5, 16, 7, -8, 79, 100]
b = [1, 2, 3, 4, 5]
c = [97, 98, 99]
d = [10009]
print('len a:', len(a))
print('max a:', max(a))
print('min a:', min(a))
print('sum a:', sum(a))
# print(sorted(a))  # 升序排列
# print(a.count(100))  # 出现次数
a.append(d)  # 添加项若是数，则与extend效果相同；若添加项是列表，则将列表中嵌套列表
print(a)
b.extend(d)  # 将添加项内容追加到后面
print(b)
