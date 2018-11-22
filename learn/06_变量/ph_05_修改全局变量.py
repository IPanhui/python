num = 10

def demo1():

    # 希望修改全局变量的值
    # 在Python中，不允许直接修改全局变量的值
    # 如果使用赋值语句，会在函数内部，定义一个局部变量
    # global 关键字会告诉解释器后面的变量是一个全局变量
    # 再使用赋值语句时，就不会创建局部变量
    global num

    num = 99
    print("demo1 ==> %d" % num)

def demo2():

    print("demo2 ==> %d" % num)

demo1()
demo2()

