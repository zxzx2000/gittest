#！/usr/bin/python
#-*-coding:utf-8-*-

import pytest

# 所有的测试用例必须以test_x开头，每一个测试用例都是一个函数
def test_1():
    # print('执行测试用例一')
    # 预期结果
    a=100
    # 实际结果
    b=50
    # 判断实际结果与预期结果是否一致
    assert a == b

def test_2():
    # 预期结果
    a=100
    # 实际结果
    b=50
    # 判断实际结果与预期结果是否一致
    assert a != b
    assert a + b == 150

# def test_3():
#     c='hello'
#     assert 'o' in c


