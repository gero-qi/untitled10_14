from demo.common.framlog import FrameLog

class Base():
    # chromedriver = "D:\\chromedriver.exe"
    # driver = webdriver.Chrome(chromedriver)

    def __init__(self, dirver):
        self.driver = dirver
        self.log = FrameLog().log()

    def findele(self, *args):
        try:
            print(args)
            self.log.info("通过" + args[0] + "定位，元素是" + args[1])
            print()
            return self.driver.find_element(*args)
        except:
            self.log.erro("元素定位失败")

    def max_windows(self):
        self.driver.maximize_window()

    def url(self):
        return self.driver.current_url



