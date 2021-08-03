#判断下列变量命名是否合法
#char(√) Cy%ty(×) Oax_li(√) $123(×) fLul(√) 3_3(×) BYTE(√) T_T(√)

A , B=56 , 78
print('A =' , A + 22)
print('B =' , B - 22)

stu1 = 45
stu2 = 23
print('stu1 + stu2 =' , stu1+stu2)

a,b,c,d,e=35.5,25.7,352.7,4577.6,55.5
print("平均值:",(a+b+c+d+e)/5)
print("五个数的和:",a+b+c+d+e)

num1 = 45
num2 = num1
print("num2",num2)

import  random
a = int(random.randint(0,100))
i = 0
while True:
    i +=1
    guess = int(input("请输入要猜的数字:"))
    if guess>a:
        print("太大了")

    elif guess<a:
        print("太小了")

    else:
        print("猜对了","猜错了",i,'次')
        break