import os, sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from demo.common.excel_data import read_excel
from demo.common.function import project_path, config_url
from demo.PageObject.testpage import SearchPage







class LogingTest(unittest.TestCase):
    # setupClase 打开数据 打开文件 打浏览器等操作
    @classmethod
    def setUpClass(cls):
        cls.data = read_excel(project_path() + "data\\testdata.xlsx", 0)
        # read_excel(os.path.split(os.path.realpath(__file__))[0].split('c')[0] + "data\\testdata.xlsx"
        #cls.driver = webdriver.Chrome()
        chromedriver = "D:\\chromedriver.exe"
        cls.driver = webdriver.Chrome(chromedriver)
        cls.driver.get(config_url())
        cls.driver.maximize_window()

    def test_02(self):
        # sp = SearchPage(self.driver)
        #self.driver.find_element_by_xpath("// b[contains(., '火车')]").click()
        self.driver.find_element(By.XPATH,"// b[contains(., '火车')]").click()
        print("====================================================")
        # print(self.data.get(1)[0], self.data.get(1)[2], self.data.get(1)[3])
        # sp.search_trains(self.data.get(1)[0], self.data.get(1)[2], self.data.get(1)[3])

    @classmethod
    def tearDownClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.close()

    # if __name__ == "__main__":
    # suiteTest = unittest.TestSuite()
    # suiteTest.addTest(logingTest("test_02"))
