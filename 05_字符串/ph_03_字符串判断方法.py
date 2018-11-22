#1.判断空白字符
space_str = " \t\n\r"

print(space_str.isspace())

#2.判断是否包含数字
num_str = "\u00b2"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())