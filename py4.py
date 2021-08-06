import random
lunen = [23,35,44]
hali = [60,77,68,88,90]
hemin = [97,99,89,91,95,90]
maerfu = [100,85,90]
grade1,grade2,grade3,grade4=0,0,0,0
for x in range(len(lunen)):
    grade1 +=lunen[x]
print("罗恩的成绩为:",grade1)
for x in range(len(lunen)):
    grade2 +=hali[x]
print("哈利的成绩为:",grade2)
for x in range(len(lunen)):
    grade3 +=hemin[x]
print("郝敏的成绩为:",grade3)
for x in range(len(lunen)):
    grade4 +=maerfu[x]
print("马尔福的成绩为:",grade4)
print("---------------------")

num = int(input('请输入一个数:'))
while num != 0:
    print(num % 10)
    num =num // 10
print("---------------------")

a = [1,5,15,89,80,99,105,14,10]
sum = 0
for a1 in a:
    if a1 % 5 == 0:
        sum += a1
print("列表中是5的倍数的和为:",sum)
print("---------------------")

list = [1,2,3,4,5,6,7,8,9]
list1 = [0]
for i in range(9):
    a = list.pop()
    list1.append(a)
list = list1
print(list)
print("---------------------")

list = [1,2,3,5,1,8,9,6,4,7,5,1]
dict = {}
for x in list:
    if x not in dict:
        dict[x] = 1
    else:
        dict[x] +=1
print(dict)