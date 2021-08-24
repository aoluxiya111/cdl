from threading import Thread
import time
breank = 0
class chushi(Thread):
    maker = ""
    def run(self) -> None:
        global breank
        while True:
            if breank < 500:
                breank = breank + 1
                time.sleep(2)
                print("恭喜",self.maker,"做了",breank,"个面包")
            elif breank == 500:
                print("篮子已经满了不用做面包")
class buyer(Thread):
    nem = 0
    buymoney = 3000
    def run(self) -> None:
        global buymoney
        global breank
        global buyer
        while True:
            if breank >= 1:
                breank = breank - 1
                self.buymoney = self.buymoney - 3
                print("买到了一个面包","金钱剩余",self.buymoney)
                time.sleep(1)
            elif self.buymoney < 3:
                print("你的余额不足无法继续购买")
                break
p1 = chushi()
p2 = chushi()
p3 = chushi()
a1 = buyer()
a2 = buyer()
a3 = buyer()
a4 = buyer()
a5 = buyer()
p1.maker = "大厨师"
p2.maker = "二厨师"
p3.maker = "三厨师"
a1.buyer = "张三"
a2.buyer = "李四"
a3.buyer = "王五"
a4.buyer = "赵六"
a5.buyer = "陈大龙"
p1.start()
p2.start()
p3.start()
a1.start()
a2.start()
a3.start()
a4.start()
a5.start()