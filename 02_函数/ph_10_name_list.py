name = ["zhangsan","lisi","wangwu"]

print(name[2])

print(name.index("wangwu"))

name[1]="李四"

name.append("王小二")
name.insert(1,"小妹妹")

temp_list = ["孙悟空","猪八戒","沙师弟"]
name.extend(temp_list)

name.remove("wangwu")

name.pop(3)

name.clear()

print(name)