poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:

    #使用strip方法去除字符串中的空白字符
    #在使用center方法居中显示文本
    print("|%s|" %poem_str.strip().center(10," "))


