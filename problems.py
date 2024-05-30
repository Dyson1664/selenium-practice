#lists

# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [3, 4, 8, 12, 16, 20, 24, 28]


def even_odd(li, l2):
    l3 = []
    for num in li:
        if num % 2 == 0:
            l3.append(num)

    for nums in l2:
        if nums % 2 != 0:
            l3.append(nums)

    print(l3)
# even_odd(l1, l2)


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [3, 4, 8, 12, 16, 20, 24, 28]



def odd_e(li, l2):
    l3 = []
    num = l1[1::2]
    print(type(num))
    print(num)
    nums = l2[::2]
    empty = ''
    num.extend(nums)

#what about if you couldnt use extend???


    return num



print(odd_e(l1, l2))