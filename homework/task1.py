how_nums = int(input('Nechta raqam kiritasiz?\n>>> '))
nums_for_max, min_list, max_num, min_num, zero = [], [], '', '', 0
for i in range(0, how_nums):
    nums_for_max.append(int(input(f'{i+1}-raqamni kiriting: ')))
    if nums_for_max[i]<0 or nums_for_max[i]>9:
        print('Iltimos faqat raqam kiriting!')
        nums_for_max[i] = int(input(f'{i+1}-raqamni qaytadan kiriting: ')) 
print(nums_for_max)
nums_for_min = nums_for_max[:]
for i in range(0, how_nums):
    if min(nums_for_min) == 0:
        zero += 1
    min_list.append(str(min(nums_for_min)))
    nums_for_min.remove(min(nums_for_min))
    max_num += str(max(nums_for_max))
    nums_for_max.remove(max(nums_for_max))
min_list.insert(0, min_list.pop(zero - len(min_list)))
for i in min_list:
    min_num += i
if int(min_num) == 0:
    print(f'Max 0')
    print(f'Min 0')
else:
    print(f'Max {max_num}')
    print(f'Min {min_num}')
