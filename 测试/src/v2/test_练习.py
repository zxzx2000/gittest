#！/usr/bin/python
#-*-coding:utf-8-*-
import pytest

def setup():
    print("执行setup")
def test_1():
    print('11111')
    assert 1==1
def test_2():
    print("22222")
    assert 1==1
def teardown():
    print("开始teardown")