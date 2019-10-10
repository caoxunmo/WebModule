# -*- encoding:utf-8 -*-

"""
字符串中的一些操作方法
"""
'''
str_a = "xiaohong"
str_b = "987h654321"

print(str_a + "," + str_b)
print(len(str_a + str_b))
#print(cmp(str_a, str_b))

#扫描字符串
for i in str_b:
    if i in str_a:
        digit = str_b.index(i) + 1
print("目标字符在第%s个" % digit)

#翻转字符串
str_b = str_b[0::-1]
print(str_b)


str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print str.split(" ")            # 以空格为分隔符，包含 \n
print str.split(' ', 1)        # 以空格为分隔符，分隔成两个
'''

a = "abcdefghijkl"
print(a[0:2])