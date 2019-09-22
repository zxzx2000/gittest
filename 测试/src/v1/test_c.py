#！/usr/bin/python
#-*-coding:utf-8-*-

# 初始化测试环境与清理测试环境
# setup_module、teardown_module
"""
setup_module ---->一个脚本仅运行一次，【在所有测试用例开始之前执行一次】
teardown_module ---->在所有测试用例执行之后执行一次

"""
# def setup_module():
#     print("开始执行setup_module")

# def setup_function():
#     print("开始执行setup_function")
#
#
# def test_1():
#     print("test_1运行")
#     assert 0 == 0
#
# def test_2():
#     print("test_2运行")
#     assert 1 < 0
#
# def test_3():
#     print("test_3运行")
#     assert 1 > 0

# def teardown_module():
#     print("开始执行teardown_module")

# def teardown_function():
#     print("开始执行teardown_function")


# setup_function   teardown_function
'''
setup_function  每个测试用例执行之前运行一次
teardown_function 每个测试用例执行之后运行一次
'''

# setup   teardown
"""
setup  在类里面使用的，类中的每个测试用例之前运行setup一次
teardown  在类里面使用的，类中的每个测试用例之后运行teardown一次
"""

# class Testmi(object):
#     def setup_class(self):
#         print("正在运行setup_class函数")
#
#     def teardown_class(self):
#         print("开始执行teardown_class")
#
#     def test_1(self):
#         print("test_1运行")
#         assert 0 == 0
#
#     def test_2(self):
#         print("test_2运行")
#         assert 1 < 0
#
#     def test_3(self):
#         print("test_3运行")
#         assert 1 > 0
#
#     def teardown_function(self):
#         print("开始执行teardown_function")
# Testmi()

# setup_class  teardown_class
"""
setup_class  作用在类中，类中所有的测试用例执行之前，运行一次
teardown_class  作用在类中，类中所有的测试用例执行之后，运行一次
"""


# setup_method、teardown_method
'''
setup_method  在类里面使用的，类中的每个测试用例之前运行setup_method一次
teardown_method  在类里面使用的，类中的每个测试用例之后运行teardown_method一次
setup 和 setup_method  不需要出现在同一个类中，因为作用一样的 
'''

'''
预期结果  a=100
实际结果  算法
'''


# n=0
#
# b=100
# c=1000
'''
+   -   *   /
'''

# n = 100

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
    assert c==200

def tesrdown_module():
    n = 100

def test_10():
    pass