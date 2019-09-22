#！/usr/bin/python
#-*-coding:utf-8-*-

import pytest

# fixture  夹具，作用给不同的测试用例赋予不同的功能
# scope：指的是一个被@pytest.fixture装饰的函数作用范围有多大
# scope = 'function'

"""
scope = 'function',意味着每个测试用例执行之前跑一次
前提是：测试用例使用了被@pytest.fixture装饰的函数名
注意：它可以作用于整个脚本中

scope="module",意味着整个脚本中只有第一个使用被@pytest.fixture装饰的
函数名的测试用例执行一次

scope="class",意味着在类中被，只有第一个测试用例使用@pytest.fixture装饰的函数才被执行一次

scope="package"---->测试阶段
scope="session" 会话级别，多个测试用例在不同的脚本，可以一起执行
"""


@pytest.fixture(scope="function")
def login():
    print("已经登陆账号了1")
#
# def test_1(login):
#     print("执行测试用例1")
#     assert 0 > 100
#
# def test_2():
#     print("执行测试用例2")
#     assert 1 > 0
#
# def test_3(login):
#     print("执行测试用例3")
#     assert 2 == 2

class TestOne(object):

    @pytest.fixture(scope="class")
    def logins(self):
        print("退出操作")

    def test_4(self):
        print("执行测试用例4")
        assert 0 > 100

    def test_5(self):
        print("执行测试用例5")
        assert 1 > 0

    def test_6(self,login,logins):
        print("执行测试用例6")
        assert 2 == 2

# def test_7(logins):
#