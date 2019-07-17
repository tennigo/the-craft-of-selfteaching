#!/usr/bin/env python3

"""
A Python version of the classic "bottles of beer on the wall" programming
example.

By Guido van Rossum, demystified after a version by Fredrik Lundh.
"""
#20190717
# 调用sys
import sys
# n默认值为100
n = 100
# 如果python beer.py 后面有跟参数,取第一个参数,0是文件名
if sys.argv[1:]:
	# 整数化参数
    n = int(sys.argv[1])
# 创建一个bottle函数,传入参数是上面的n
def bottle(n):
	# 0 和 1 的情况为特殊,1的时候bottle不用复数,所以也是特殊
    if n == 0: return "no more bottles of beer"
    if n == 1: return "one bottle of beer"
    # 返回 n的值的字符串形态,后面接句子
    return str(n) + " bottles of beer"
#正式运行的语句是一个for
#从n开始,到0结束,步长是-1,就是倒着来
for i in range(n, 0, -1):
	# 根据n当前的值,print
    print(bottle(i), "on the wall,")
    print(bottle(i) + ".")
    print("Take one down, pass it around,")
    # 承接上一句,取走一个之后剩下i-1
    print(bottle(i-1), "on the wall.")
