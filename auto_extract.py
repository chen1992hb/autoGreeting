# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from datetime import datetime
from datetime import date
import calendar
import random
from apscheduler.schedulers.background import BackgroundScheduler

from appium import webdriver
import time

caps = {"platformName": "Android", "platformVersion": "10", "deviceName": "STS0219A30002071",
        "appPackage": "com.tencent.mm", "appActivity": ".ui.LauncherUI", "noReset": "True",
        "ensureWebviewsHavePages": True}

scheduler = BackgroundScheduler()



def send_message(text: str):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    time.sleep(3)
    el1 = driver.find_element_by_id("com.tencent.mm:id/f8y")
    el1.click()
    time.sleep(1)
    el2 = driver.find_element_by_id("com.tencent.mm:id/bhn")
    el2.send_keys("795")
    time.sleep(1)
    el3 = driver.find_element_by_id("com.tencent.mm:id/tm")
    el3.click()
    time.sleep(1)
    el5 = driver.find_element_by_id("com.tencent.mm:id/al_")
    el5.send_keys(text)
    time.sleep(1)
    el6 = driver.find_element_by_id("com.tencent.mm:id/anv")
    el6.click()
    time.sleep(10)


def get_now():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")


def get_mothers_day():
    cal = calendar.Calendar(firstweekday=6)
    year = int(datetime.now().year)
    weeks = cal.monthdays2calendar(year, 5)
    return str(year) + '-05-' + str(weeks[2][0][0])


# 在 2017-12-13 14:00:01 时刻运行一次 job_func 方法

twqh=['不要抱怨，抱我',
      '我是九你是三，除了你还是你',
      '我的手被划了一道口子 你也划一下 这样我们就是两口子了',
      '我觉得你好像一款游戏-我的世界',
      '你是不是喜欢我?请在3秒内找出这句话中重复的字',
      '你猜我喜欢什么制服-被你制服',
      '我得给你买个指南针-免得你被我惯得找不着北',
      '我最近要换个造型-没你不行'
      '齾 爩 鱻 我 喜 欢 你 龗 灪 龖 厵 爨 癵 籱 饢 骉 鲡 麣 纞 虋 讟 钃 鸜 麷 鞻 请找出里面你认识的字',
      '遇到你后，我都没吃过糖了-因为你太甜了',
      ]
morning=['人生就两件事，一件是拿事儿把时间填满，另一件是被你把心填满。早安！',
         '所有美好，都不负归期，选一种姿态让自己活得无可替代，没有所谓的运气只有绝对的努力。早安！',
         '万个美丽的未来，抵不上一个温暖的现在，每一个真实的现在，都是我们曾经幻想的未来，愿你爱上现在，梦见未来，早安！',
         '愿你撞过的南墙，都成为坦途，愿你遇见的绝望，都成为盛放。早安！',
         '不要急着让生活给予所有的答案，有时我们需要耐心的等待。相信过程，坦然前行，不负生活，生活也必不负你。早安！'
         '我们来到这个世上，应该跟最好的人、最美的事、最芬芳的花朵倾心相见，如此才不负命运一场。早安！',
         '借时光之手，暖一树花开。借一方晴空，拥抱阳光。你若裹足不前，有人偷着笑。你若挣开束缚，前方春暖花开。生命很短，当下最美。早安！',
         '若美好迟迟未发生也不要着急，最好的总会在不经意间出现，你的幸福只是姗姗来迟。而你只需努力，剩下的交给时光。早安！']


# 早安:08-00
scheduler.add_job(send_message, 'cron', hour='8', minute='00', second='00',
                  args=['现在是' + get_now() + morning[random.randint(0,morning.__len__())]])
# 晚安:22-00
scheduler.add_job(send_message, 'cron', hour='22', minute='00', second='00',
                  args=['晚安，现在是' + get_now() + twqh[random.randint(0,twqh.__len__())]])
# 生日:10-23 00:00
scheduler.add_job(send_message, 'cron', month='10', day='23', hour='8', args=['可以只过生日，不用长大，永远都是18岁～'])
# 情人节:02-14 00:00
scheduler.add_job(send_message, 'cron', month='2', day='14', hour='0', args=['情人节快乐！10分钟内回复想要的礼物有惊喜～'])
# 结婚纪念日节:03-03 00:00
scheduler.add_job(send_message, 'cron', month='3', day='3', hour='0', args=['结婚纪念日快乐！晚上想吃啥，西餐、火锅、还是烧烤？'])
# 妇女节:03-08 00:00
scheduler.add_job(send_message, 'cron', month='3', day='8', hour='0', args=['女神节快乐！'])
# 母亲节:每个5月的第二个周日
scheduler.add_job(send_message, 'date', run_date=get_mothers_day(), args=['母亲节快乐！'])
#圣诞节：12-25 00：00
scheduler.add_job(send_message, 'cron', month='12', day='25', hour='0', args=['圣诞节快乐！'])

# driver.quit()

scheduler.start()
while True:
    time.sleep(5)
