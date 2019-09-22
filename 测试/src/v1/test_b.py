#！/usr/bin/python
#-*-coding:utf-8-*-

import pytest

# -m参数  执行被@pytest.mark装饰的用例
# @pytest.mark.固定的
"""
将测试用例test_one起一个别名
"""

@pytest.mark.run_1
def test_one():
    a = 1
    b = 2
    c = a + b
    # 实际结果是3，预期结果是2
    # 设定断言
    assert c == 2


# @pytest.mark.run_1
def test_two():
    str_1="hello pytest"
    str_2 = "python"
  # 设定断言，判断str_2 在 str_1内
    assert str_2 in str_1

def test_three():
    """docstring for test_three"""
    n = 100
    assert n < 101

class TestOne(object):
    def test_v(self):
        assert 0
# --collect-only
# 参数是用来显示当前目录下所有的伊test开头的测试模块，test开头的测试类及test开头的测试函数的

# pytest 执行某个模块下的测试用例
'''
必须进入模块名所在的目录
pytest 模块名字
'''
# 执行具体的测试用例
"""
pytest test_b.py::test_one
"""