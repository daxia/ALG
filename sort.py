
#2018/12/19
#Auth : WangShengZhong

#test 测试
print('wang')

#插入排序  2018/12/20
'''
插入排序介绍: 
    拿到一副牌，如何将其排好序，就可以用到插入排序。

'''

def Insertion_Sort_Small_to_Big(list):
    print('test')
    num = 1
    len1 = len(list)
    while num < len1 :       
        key = list[num]
        i = num - 1
        while (i >= 0) and (list[i]>key):
            list[i+1] = list[i]
            i=i-1
        list[i+1] = key
        num+=1


def Insertion_Sort_Big_to_Small(list):
    print('test')
    num = 1
    len1 = len(list)
    while num < len1 :       
        key = list[num]
        i = num - 1
        while (i >= 0) and (list[i]<key):
            list[i+1] = list[i]
            i=i-1
        list[i+1] = key
        num+=1   


List1 = [8,6,4,11,9,3]
Insertion_Sort_Small_to_Big(List1)
print(List1)

Insertion_Sort_Big_to_Small(List1)
print(List1)



#2018/12/22
'''



'''


