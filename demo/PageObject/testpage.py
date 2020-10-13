
from selenium.webdriver.common.by import By
import time
from demo.base.base import Base


class SearchPage(Base):
    # 打开页面
    # 放大页m面

    # 查找火车按钮，点击
    def search_train(self):
        return self.findele(By.XPATH, "// b[contains(., '火车')]").click()

    # 查找出发地并输入
    def search_leave(self):
        return self.findele(By.ID, "notice01")

    # 查找到达地并输入
    def search_arrive(self):
        return self.findele(By.ID, "notice02")

    # 查找出发时间并输入
    def search_leave_time(self):
        return self.findele(By.ID, "DdateObj")

    # 查找搜索按钮
    def search_button(self):
        return self.findele(By.ID, "searchTicket")

    def search_trains(self, leave, arrive, ltime):
        #self.max_windows()
        self.search_train().click()
        self.search_leave().sendkeys(leave)
        self.search_arrive().sendkeys(arrive)
        self.search_leave_time().sendkeys(ltime)
        self.search_button().click()
        time.sleep(8)
        return self.url()
