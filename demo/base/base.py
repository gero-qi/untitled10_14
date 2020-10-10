from Common log import FrameLog
from selenium import webdriver
class Base():
    def __init__(self,driver):
        #ChromeDriver = "D:\\chromedriver.exe"
        #self.driver = webdriver.Chrome(ChromeDriver)
        self.driver = driver
        self.log = FrameLog().log()

        def findele(self,*args):
            try:
                print(args)
                self.log.info("通过"+args[0]+ "定位，元素是"+args[1])
                retrun self.driver.find_element(*args)
            except:
                self.log.erro("元素定位失败")

        def  wq3er


