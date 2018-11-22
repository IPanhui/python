"""
语法
for 变量 in 集合：
    循环体代码
else：
    没有通过break退出循环，循环结束后，会执行的代码
"""

for num in [1,2,3]:

    print(num)
    if num == 2:
        break
else:
    print("会执行吗")
print("循环结束")