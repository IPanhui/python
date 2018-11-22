def demo(num, *nums, **person):
    # *:元组  **：字典
    print(num)
    print(nums)
    print(person)

# demo(1)
demo(1, 2, 3, 4, name = "小明",age = 18)