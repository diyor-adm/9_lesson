from random import randint
# num= int(input('Son kiriting: '))
# nums=[]
# i = 0

# while i< num:
#     nums.append(randint(0,100))
#     i+=1
# print(nums)

# ====================

# print([randint(0,100) for i in range(int(input('Enter num:')))])


# ==================

# num = int(input('Enter num: '))
# list = [randint(0,100) for i in range(num)]
# print(list)
# num_list=[]
# for nums in list:
#     num_list.append(f"{nums}")
# print(num_list)


# ===============

# a = [[1,2,3], [4,5,6], [7,8,9]]

# for line in a:
#     for elem in line:
#         print(elem)

# ==================
list = []
num = int(input('Son kiriting: '))
for i in range(0,num):
    list.append(int(input(f'{i+1}-sonni kiriting: ')))

print(list)
