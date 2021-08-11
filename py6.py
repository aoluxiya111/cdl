'''
数值类型：int(整形),float(浮点型)字符串,str 布尔型 T F
        集合set (小括号来表示) 列表list[中括号来表示] 字典doct{花括号来表示} 7种数据类型
        def：定义一个函数def (方法的名字) (元素1，元素2)：
        循环：   while：通常使用在一个整体的开始/判断一直的条件：
while T:  while i < 10:
                for:通常使用在需要遍历的内容：遍历列表，字典，set
        break：跳出整个循环
        continue:跳出本次循环
pycharm：快捷键：ctrl+/快速多行注释
写代码的思路：1、需求分析 2、大体设计(画个草图、伪代码(pass))
           3、分析细小问题进行编码
'''

# def add (x,y):
#     z=x+y
#     print(z)
#     return 1
#
# print(add(1,2))
import random
print("-----------------------------------------")
print("|----------中国工商银行账户管理系统----------")
print("|----------1、开户              ----------")
print("|----------2、存钱              ----------")
print("|----------3、取钱              ----------")
print("|----------4、转账              ----------")
print("|----------5、查询              ----------")
print("|----------6、退出              ----------")
print("|----------------------------------------")
bank={"name":{"money":1000}}
def bank_adduser(account,username,password,country,province,street,door):
    if len(bank) >100:
        return 3
    if username in bank:
        # 如果名字在brank执行下面的代码
        return 2

    bank[username]={
        "account":account,
        #键一个名字      ：值来自传入的参数:account
        "password":password,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "brnk_name":bank_name#直接调用全局参数
    }
    return 1

bank_name="中国工商银行昌平分行"
def useradd():
    username = input("请输入用户名")
    password = input("请输入密码")
    print("请输入详细信息")
    country = input("请输入国家")
    province = input("请输入省份")
    street  = input("请输入街道")
    door = input("请输入门牌号")
    account=random.randint(10000000,99999999)
    status=bank_adduser(account,username,password,country,province,street,door)
    if status == 3:
        print("对不起，该银行的用户已满，请到其他银行办理")
    if status == 2:
        print("对不起，该用户已经开户，不要重复")
    if status == 1:
        print("恭喜你成功开户，以下是你的信息")
        info = '''
            ----------个人信息----------
            用户名：%s
            账号：%s
            密码：*****
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
        '''
        print(info % (account,username,country,province,street,door,bank[username]["money"],bank_name))

# 存钱
def cunqian_bank(username, money):
    if username in bank:
        bank["name"]["money"] += money
        return True
    else:
        return False

def cunqian():
    name = input("请输入用户名")
    money = int(input("money"))
    status = cunqian_bank(name, money)
    if status is True:
        print("存钱成功，以下是你的余额信息")

        info = '''
           ----------余额信息----------
                 用户名：%s
                 余额：%s
        '''
        print(info % (name, bank["name"]["money"]))
    else:
        print("存钱no")

# 取钱
def quqian_bank(account,password,money):
    if account in bank:
        bank[account]["money"] +=int(money)
        return 0
    elif account not in bank:
        return 1
    elif password !=password:
        return 2
    elif money < money:
        return 3

def quqian():
    account = input("请输入你的账号")
    password = input("请输入你的密码")
    money = input("请输入取钱金额")
    status = quqian_bank(account,password,money)
    if status == 0:
        print("取钱成功")
    elif status == 1:
        print("账号不存在")
    elif status == 2:
        print("密码错误")
    elif status == 3:
        print("余额不足")
        info = '''
        ----------余额信息----------
        账号：%s
        余额：%s
        '''
        print(info % (account,password,bank["name"]["money"]))

#转账
def zhuanzhang1(account,accounts,password,money):
    if account not in bank:
        return 1
    if password !=password :
        return 2
    if money < money:
        return 3
    if account in bank:
        bank[account]["money"] -= int(money)
        # bank["name"]["money"]
        return 0

def zhuanzhang():
    account = input("请输入转出账号") #"name"
    accounts = input("请输入转入账号")
    password = input("请输入密码")
    money =  input("请输入金额")
    statuss = zhuanzhang1(account,accounts,password,money)
    if statuss == 0:
        print("转账成功")
    if statuss == 1:
        print("账号不存在")
    if statuss == 2:
        print("密码错误")
    if statuss == 3:
        print("余额不足")
        info = '''
        ------------转账信息------------
        转出账号：%s
        转入账号：%s
        转账金额：%s
        '''
        print(info % (account,accounts,password,money))

#查询
def chaxun(account,password):
    if account not in bank:
        return 0
    elif password != password:
        return 1
    if account in bank:
        return 2

def cha_xun():
    account = input("请输入账号")
    password = input("请输入密码")
    statusss = chaxun(account,password)
    if statusss == 0:
        print("账号错误")
    if statusss == 1:
        print("密码错误")
    if statusss == 2:
        print("查询成功")
        info = '''
        ------------查询信息--------------
        ------------个人信息------------
            用户名:%s
            账号：%s
            密码：*****
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
        '''
        print(info % (account,password))

while True:
    num=input("请输入您要办理的业务：")
    if num == "1":
        useradd()
        print(bank)
    if num == "2":
        print(bank)
        print("存钱")
        cunqian()
    if num == "3":
        print("取钱")
        quqian()
    if num == "4":
        print("转账")
        zhuanzhang()
    if num == "5":
        print("查询")
        chaxun("account","password")
    if num == "6":
        print("退出")
        break
    else :
        print("别瞎搞")
        break
