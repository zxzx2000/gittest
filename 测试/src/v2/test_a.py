#！/usr/bin/python
#-*-coding:utf-8-*-
import pytest

# def test_1(k):
#     print("执行测试用例1")
#     assert 1 > -1

# 参数化
"""
对同一个测试用例，传入多组参数，一组参数执行一次测试用例
"""
import pytest
# 测试数据 ----->针对输入框
test_data = [1, 2, 3, 4, 5, 6]

# name 别名
# ids 对测试用例进行一个编号，编号的作用：区分测试用例。
# request  想测试数据test_data中请求一组测试数据
# params  ------> 赋值test_data
# request.param ------>每次请求一组测试数据
@pytest.fixture(params=test_data,ids=['a','b','c','d','e','f'])
def get_data(request):
    return request.param      # 固定写法

def test_2(get_data):
    print(f"获取到的测试数据是：{get_data}")
    # 设置一个预期结果
    b = 4
    assert get_data > b



import pytest


# @pytest.fixture()
# def uk():
#     print("每个测试用例执行之前执行一次uk函数")
#
#
# def test_1(uk):
#     print("运行测试用例test_1")
#
#
# def test_2(uk):
#     print("运行测试用例test_2")
#
#
# def test_3(uk):
#     print("运行测试用例test_3")

# sutouse  默认False
# autouse = True
"""
autouse = True
被@pytest.fixture装饰的函数下面所有的测试用例都会被自动执行该函数
"""

# @pytest.fixture(autouse=True)
# def ab():
#     print("每个测试用例执行之前执行一次uk函数")
#
#
# def test_4():
#     print("运行测试用例test_4")
#
#
# def test_5():
#     print("运行测试用例test_5")
#
#
# def test_6():
#     print("运行测试用例test_6")

@pytest.fixture(name="new_name")
def uk():
    print("每个测试用例执行之前执行一次uk函数")


def test_1(new_name):
    print("运行测试用例test_1")


# def test_2(new_name):
#     print("运行测试用例test_2")

