#!/usr/bin/env python
# encoding:utf-8
"""需要下载一个html的python文件，下载地址http://tungwaiyip.info/software/HTMLTestRunner.html
    然后将该文件放到Python27/lib里面，或者放置到当前路径下
"""
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


class TestMoutain(unittest.TestCase):

    def SetUP(self):
        pass

    def tearDown(self):
        pass

    def test_it_is_true(self):
        self.assertTrue(1 == 0)
        print "fail....."

    def test_it_is_failse(self):
        self.assertFalse(1 == 0)
        print "success....."

    def test_strip_strings(self):
        self.assertTrue("aaa" == "aaa")

    def test_strip_strings(self):
        self.assertTrue("  aaa  ".strip() == "aaa")
        self.assertTrue("  aaa".lstrip() == "aaa")
        self.assertTrue("aaa  ".rstrip() == "aaa")


class TestMain(unittest.TestCase):

    def SetUP(self):
        pass

    def tearDown(self):
        pass

    def test_it_is_true(self):
        if True:
            assert 1 == 1
        else:
            assert 1!=1


def fun_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader
    suite.addTest(TestMain("test_if_else"))
    suite.addTest(TestMoutain("test_it_is_true"))
    suite.addTest(TestMoutain("test_it_is_true"))
    return suite

if __name__ == "__main__":
    fp = open("./test_result_%s.html" % time.strftime("%Y-%m-%d %H-%M-%S"), "wb")
    runner = HTMLTestRunner(stream = fp,
                            title = u"测试报告生成范例",
                            description = u"测试用例执行情况：")
    runner.run(fun_suite())
    fp.close()
    sys.exit(0)