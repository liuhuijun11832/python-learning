# -*-encoding: utf-8 -*-
import unittest
import HTMLTestRunner
import time

if __name__ == '__main__':
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(r'E:\PycharmProjects\python-learning', pattern='test_*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            suite.addTests(test_case)
    # suite.addTests([
    #     unittest.defaultTestLoader.loadTestsFromTestCase(LoginTest)
    # ])
    now = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
    filename = now+'_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'登录页测试报告',
        description=u'用例执行情况',
        verbosity=2
    )
    runner.run(suite)
    fp.close()