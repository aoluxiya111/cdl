'''
python:数据类型
   int str float bool
   list[]、tuple()
          key      value
   dict{   ""   :   ""   }
         键    值    键值对
         取键来获取值
   回家:
   三层字典：第一层:几号线{，，，，，}input出入了一个地铁没有的线路 为错
           第二层:那个小区 input出入了一个地铁没有的线路为错
          打印 乘法表 99 1010：我输入的数字打印出来的乘法表
'''
#dict1={"小宝":"男"}
#print(dict1["小宝"])
# dict1={"01": {"011":"北京"},"02": {"012":"上海"}
#     ,"03": {"013":"天津"},"04": {"014":"香港"}
#     ,"05": {"015":"浙江"},"06":{"016":"河南"}}
# a=dict1["01"]["011"]
# print(a)
#
#
# name = input("请输入一个数字")
# if name == "01":
#     print(dict1["01"])
#     name = input("请输入一个数字")
#     if name == "011":
#         print(dict1["01"]["011"])
'''
list=[1,2,3,4,5,6,7,8,9]
#while True/范围:
    #       循环数数 (        5)
for i in range(len(list)): #range 数数  数出来的数字给了i 0 1 2 3 4 5
    p=list[i]
    print(p)
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',j*i,end='')
    print()

n = int(input("请输入一个数字:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,'*',i,'=',j*i,end='')
    print()


data = {'13号线':{
             '流星花园':
                   ['001','002','003'],
             '育荣教育园区':
                   ['0001','0002','0003'],

       },
      '1号线':{
          '兴隆花园':
              ['001','002','003'],
          '康家园小区':
          ['0001','0002','0003']
      },
       '昌平线':{
           '博雅德园':
               ['001','002','003'],
           '润泽家园':
           ['0001','0002','0003']
       }
}
def print_adress(choose):
    for i in choose:
        print(i)

for x in data.keys():
    print(x)
line = input("请选择地铁线路:")
if line in data:
    print_adress(data[line])
    adress = input("请选择小区:")
    if adress in data[line]:
        print_adress(data[line][adress])
        num = input("请输入门牌号:")
        if num in data[line][adress]:
            print(num)