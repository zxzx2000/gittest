#！/usr/bin/python
#-*-coding:utf-8-*-

# 装饰器的作用？
# 函数的一种包装，把函数A作为函数B中的一个参数，类似于函数的嵌套
# 装饰器的本质就是函数，利用函数的返回值实现装饰器与装饰器函数之间数据的传递

# def foo():
#     print("执行foo函数")
#     # return None
#
# # 函数不写return，也依旧会返回一个None
# # print(foo())
#
# def koo(arg):
#     print("执行koo函数")
#     arg()
#
# koo(foo)

# 两个函数嵌套到一起

def wa(func):
    print("开始执行wa函数")
    def inner():
        print("开始执行inner函数")
        func()
        print("执行inner函数结束")
    # print("执行wa函数结束")
    return inner


@wa        # @wa等价于wa(say)
def say():
    print("say函数运行了")

say()

'''
wa(say)()
装饰器工作原理
1、定义wa函数
2、定义say函数
3、执行wa(say) --->执行wa函数
4、进入wa函数内部，打印第一个print，定义inner函数，将inner函数返回给wa(say)
   wa(say)=inner
5、wa(say)()----->inner()
6、执行inner函数，打印第一个print，func()替换--->say(),
    执行say函数，将say函数的返回值返回给func()，打印第二个print
    将inner函数的返回值返回给wa(say)()
7、程序退出！
'''


"""
@在python中被称为语法糖
@+函数名--->装饰器
@下的函数在执行时自动被创建并被调用
"""
'''
@wa
1、定义wa函数
2、执行@wa，执行wa函数，先打印print，定义inner函数，将inner函数返回给@wa
3、执行say(),相当于inner()，执行inner函数，先打印print，再通过@wa定义say函数，
    并且执行say函数，将say函数的结果返回给func()，打印最后一个print
    将inner函数的结果返回给say()
4、代码终止！
'''