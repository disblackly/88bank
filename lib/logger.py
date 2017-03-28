#!/usr/bin/env python
# encoding:utf-8
import os
import time
import logging


class Logger(object):
    def __init__(self, logname = './log/logger.log', loglevel = logging.DEBUG):
        """
            定义初始化函数
            两个参数logname和loglevel都配置了默认值
            logname定于了输出日志的路径和名称
            loglevel = logging.DEBUG 表明级别高于DEBUG的日志内容都会输出
        """
        #创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(loglevel)

        #创建一个handler，用于写入日子文件
        fh = logging.FileHandler(logname)
        fh.setLevel(loglevel)

        #再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(loglevel)

        #定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(levelname) s - %(module)s - %(funcName)s - %(lineno)s - %(message)s")
        fmt = logging.Formatter("%(asctime)s - %(levelname) s - %(module)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(fmt)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

if __name__ == "__main__":
    logger = Logger("product.log", logging.DEBUG).getlog()
    logger.info("info message")
    logger.info(u"测试开始")
    logger.info(u"测试结束")
    logger.error("error message")
    logger.warn("warn message")
    logger.critical("critical message")