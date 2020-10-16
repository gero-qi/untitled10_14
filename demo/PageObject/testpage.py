
from selenium.webdriver.common.by import By
import time
from demo.base.base import Base

from selenium import webdriver



class SearchPage(Base):
    # 打开页面
    # 放大页m面

    # 查找火车按钮，点击
    def search_train(self):

        return self.findele(By.XPATH, "// b[contains(., '火车')]")


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
        time.sleep(2)
        self.search_leave().send_keys(leave)
        time.sleep(2)
        self.search_arrive().send_keys(arrive)
        time.sleep(2)
        self.search_leave_time().send_keys(ltime)
        time.sleep(2)
        # 直接点击无效
        # self.driver.find_element(By.ID, "searchTicket").click()
        self.driver.execute_script("arguments[0].click();", self.search_button())
        time.sleep(8)
        print(self.url())
        return self.url()
