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




list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()

l3 = zip(list1, list2)
for nums in l3:
    print(nums)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
p = []
for x, y in zip(list1, list2[::-1]):
    print(x, y)
    p.append(x)
print(p)



list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

k = []
for i in list1:
    if len(i) > 0:
        k.append(i)
print(k)



list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)

print(list1)
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]
#['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
list1[2][1][2].extend(sub_list)

print(list1)

list1 = [5, 10, 15, 20, 25, 50, 20]

# a = list1.index(20)
# list1.remove(20)
# list1.insert(a, 200)
# print(list1)

list1[3] = 200
print(list1)


list1 = [5, 20, 15, 20, 25, 50, 20]
for num in list1:
    if num == 20:
        list1.remove(20)
print(list1)


s = [num for num in list1 if num != 20]
print(s)


#dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = dict(zip(keys, values))
print(dict)

from word_search_generator import WordSearch

puzzle = WordSearch("dog, cat, pig, horse, donkey, turtle, goat, sheep")
puzzle.show()


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks'].get('history'))




employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dict = dict.fromkeys(employees, defaults)

print(dict)