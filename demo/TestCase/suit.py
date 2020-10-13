import unittest
import time

from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

from demo.common.function import project_path

if __name__ == '__main__':
    test_dir = project_path() + "TestCase"
    print(test_dir)
    tests = unittest.defaultTestLoader.discover(test_dir, pattern='Train*.py', top_level_dir=None)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime((time.time())))
    file_path = project_path() + "Reports\\" + now + '.html'
    print(file_path)
    fp = open(file_path, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试报告')
    runner.run(tests)
    fp.close()
