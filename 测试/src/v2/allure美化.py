#！/usr/bin/python
#-*-coding:utf-8-*-
import allure
import pytest
from allure_commons.types import AttachmentType

# 标注 feature,将具有相同标注名字的测试用例放到一起
# @allure.feature("妖")
# def test_1():
#     assert 0 == 0
#
# @allure.feature("妖")
# def test_2():
#     assert 1>100

# story：对一个测试用例进行简述
# @allure.feature("妖人")
# @allure.story("这是一个很有用的测试用例")
# def test_3():
#     assert 1==1

# 定义用例的优先级  p1最高，p5最低
# @allure.severity
# Blocker级别：阻塞中断缺陷  p1
# Critical级别：严重缺陷   p2
# Normal级别：普通缺陷   p3
# Minor级别： 次要     p4
# Trivial级别：轻微  p5

# @allure.feature("五个等级")
# @allure.severity('blocker')
# def test_4():
#     assert 0
#
# @allure.feature("五个等级")
# @allure.severity('critical')
# def test_5():
#     assert 0
#
# @allure.feature("五个等级")
# @allure.severity('normal')
# def test_6():
#     assert 0
#
# @allure.feature("五个等级")
# @allure.severity('minor')
# def test_7():
#     assert 0
#
# @allure.feature("五个等级")
# @allure.severity('trivial')
# def test_8():
#     assert 0

# '''

# # step :记录测试用例执行的步骤
#
# # step 记录测试用例中的一些步骤，日志代码可以通过step记录到报告中
# # isinstance(参数一，参数二) 判断数据类型的类，参数一和参数二是否是同一个类型
# # 是的话 ---> True
# # 不是 ---> Flase
# '''
#
# @allure.step("字符串相加：{0},{1}")
# def str_add(str1, str2):
#     if not isinstance(str1, str):
#         return f"{str1} 不是字符串类型的"
#
#     if not isinstance(str2, str):
#         return f"{str2} 不是字符串类型的"
#
#     return str1 + str2
#
#
# @allure.feature("模块四")
# def test_10():
#     str1 = "hello"
#     str2 = "world"
#     allure.step("开始进行断言")
#     assert str_add(str1, str2) == "helloworld"
#
# # 打开图片
# with open(file="1.png",mode="rb")as fb:
#     d = fb.read()
# #attach 对测试用例进行添加附件
# def test_100():
#     allure.attach(name="bug.png", body=d, attachment_type=AttachmentType.PNG)
#     assert 1 > 0