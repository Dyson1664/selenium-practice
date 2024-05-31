# #lists
#
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [3, 4, 8, 12, 16, 20, 24, 28]
#
#
# def even_odd(li, l2):
#     l3 = []
#     for num in li:
#         if num % 2 == 0:
#             l3.append(num)
#
#     for nums in l2:
#         if nums % 2 != 0:
#             l3.append(nums)
#
#     print(l3)
# # even_odd(l1, l2)
#
#
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [3, 4, 8, 12, 16, 20, 24, 28]
#
#
#
# def odd_e(li, l2):
#     l3 = []
#     num = l1[1::2]
#     print(type(num))
#     print(num)
#     nums = l2[::2]
#     empty = ''
#     num.extend(nums)
#
# #what about if you couldnt use extend???
#
#
#     return num
#
#
#
# print(odd_e(l1, l2))
#
# l4 = '12345'
#
# l5 = ['6', '7', '8']
#
# for num in l5:
#     l4 += num
# print(l4)
# sample_list = [34, 54, 67, 89, 11, 43, 94]
#
# print("Original list ", sample_list)
# element = sample_list.pop(4)
# print("List After removing element at index 4 ", sample_list)
#
# sample_list.insert(2, element)
# print(sample_list)
# sample_list.append(element)
# print(sample_list)


# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
#
# def split_revearse(sample_list):
#     l1 = sample_list[:3]
#     l2 = sample_list[3:6]
#     l3 = sample_list[6:9]
#     l1.reverse()
#     l2.reverse()
#     l3.reverse()
#
#     print(l1, l2, l3)
#
#
# split_revearse(sample_list)


sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count = {}

for num in sample_list:
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1

print(count)


# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]

# third = zip(first_list, second_list)
# t = set(third)
# print(t)


first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

first_set.difference_update(second_set)
print(first_set)


roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

print(type(sample_dict.values()))

roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print(roll_number)


roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
r2 = [100, 1001, 1002]

roll_number[:1] = r2


print(roll_number)


speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

l3 = []

for um in speed.values():
    if um not in l3:
        l3.append(um)


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l3 = []
list3 = zip(list1, list2)
for i in list3:
    l3.append(''.join(i))

print(l3)

e = [i + m for i, m in zip(list1, list2)]
print(e)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
l3 = []
s = [x + y for x in list1 for y in list2]

for l in list1:
    for o in list2:
        l3.append(l + o)
print(s)
print(l3)







# for num in sample_list:
#     if num not in l:
#         l.append(num)
#
# m = max(l)
# s = min(l)
# print(m, s)

