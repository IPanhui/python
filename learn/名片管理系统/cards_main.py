#！ /usr.bin/python3
# _*_ coding:utf-8 _*_
import cards_tool


#无限循环，由用户主动决定什么时候退出循环
while True:

    # 显示功能菜单
    cards_tool.show_menu()




    action_str = input("请选择希望执行的操作：")
    print("您选择的操作的是 【%s】" % action_str)


    if action_str in ["1","2","3"]:

        #新增名片处理
        if action_str == "1":
            cards_tool.new_card()
        #显示全部
        elif action_str == "2":
            cards_tool.show_all()
        #查询名片
        elif action_str == "3":
            cards_tool.search_card()

    #退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        #如果在开发程序时，不希望立刻编写分支内部代码
        #可以使用pass关键字
        #程序运行时，pass关键字不会执行任何操作
        break
    else:
        print("您输入的不正确，请重新选择")