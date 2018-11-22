hello_str = "hello world"



#1, 判断是否以指定字符串开始
print(hello_str.startswith("hello"))

#2, 判断是否以指定字符串结束
print(hello_str.endswith("world"))

#3. 查找指定字符串
#index 同样可以查找指定的字符串在大字符串中的索引
#index 如果指定字符串不存在，会报错
#find如果指定字符串不存在，会返回
print(hello_str.find("llo"))
print(hello_str.index("llo"))
#4.替换字符串
print(hello_str.replace("world","python"))
print(hello_str

      )