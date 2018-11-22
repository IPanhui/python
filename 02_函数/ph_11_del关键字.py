name_list = ["张三","张三","李四","王五","王小二"]

list_len = len(name_list)
print("列表中包含%d个元素"%list_len)

count = name_list.count("张三")
print("张三出现了%d次"%  count)

name_list.remove("张三")


print(name_list)