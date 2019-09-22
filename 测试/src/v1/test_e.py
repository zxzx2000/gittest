#！/usr/bin/python
#-*-coding:utf-8-*-

"""
n 指定初始值100
测试用例修改n的值，修改之后进行运算
用例执行之后将n的值恢复为100
其他的用例在进行运算
"""

def setup_module():
    global n
    n = 100  #

def test_0():
    n = 101
    c = n + 100
    assert c == 200

def tesrdown_module():
    n = 100

def setup_function():
    print("开始执行setup_function")
def test_1():
    b=10
    o=100
    m=b+o
    assert n != m

def tesrdown_function():
    n=100

def test_dd():
    print()
