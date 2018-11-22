studenmt = [
    {"name" : "啊土"},
    {"name" : "小妹"},
]

find_name = "张三"
for stu_dict in studenmt:

    print(stu_dict)

    if stu_dict["name"] == find_name :
        print("扎到了 %s" % find_name)
        break
else:
    print("抱歉没有找到%s"%find_name)
print("")
