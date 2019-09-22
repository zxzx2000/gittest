#！/usr/bin/python
#-*-coding:utf-8-*-

import pytest
"""
conftest.py 的作用？
将多个测试脚本都需要引用的函数，放在conftest.py下，
当前文件夹下所有的测试脚本，在使用公共函数的时候，不需要导入，直接引用就可以了

1、一个文件夹下只能存在一个
2、conftest固定写法
"""

@pytest.fixture(scope="session")
def k():
    print("执行k")

