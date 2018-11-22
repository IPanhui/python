cars = ['bmw', 'audi', 'toyota', 'subaru']
# # sort() 按照字母顺序永久排列
# cars.sort()
# print(cars)

# # 反向字母顺序永久排列
# cars.sort(reverse=True)
# print(cars)

print("Here is the original list:")
print(cars)

# sorted()临时排序
print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)