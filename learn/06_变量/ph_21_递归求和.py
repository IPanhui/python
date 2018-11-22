# 定义一个函数 sum_numbers
# 能够接受一个 num 的整数参数
# 计算 1 + 2 + ... num 的结果

def sum_numbers(num):

    if num == 1:
        return 1

    temp = sum_numbers(num - 1 )

    return num + temp

result = sum_numbers(100)
print(result)