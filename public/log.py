# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/3/15 11:17
# @FileName     :log.py
#IDE            :PyCharm
#日志文件封装
import logging
import os
import time
#此为第一版写法
class logger(object):
    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:传入当前模块名字，便于分析日志
        """
        # 创建一个logger,初始化日志级别
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        #判断log目录是否存在，不存在则创建目录
        if not os.path.isdir("./log/"):
            os.mkdir("./log/")
        # 创建一个handler，用于写入日志文件
        now_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        log_path = './log/'
        log_name = log_path + now_time + '.log'
        file_log = logging.FileHandler(log_name,encoding='utf-8')
        #设置输出到目录默认日志级别
        file_log.setLevel(logging.INFO)
        # 再创建一个handler，用于输出到控制台
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - [%(name)s] - [msg]：%(message)s - %(lineno)d')
        file_log.setFormatter(formatter)
        console.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(console)
        self.logger.addHandler(file_log)
    def get_logger(self):
        return self.logger
#以下为比较完美的第二版,但是有点复杂
'''
class Logger(object):
    def __init__(self,log_name):
        #定义日志收集器的名字
        self.log_name=log_name
    def get_log(self,msg,level):
        # 创建一个logger
        logger=logging.getLogger(self.log_name)
        #设置日志的等级,包含INFO级别在内的以上日志
        logger.setLevel('DEBUG')
        #定义日志的输出格式
        formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s日志信息：%(message)s')
        #创建一个handler,将日志信息输出到控制台
        console=logging.StreamHandler()
        #设置输出控制台日志的等级,输出INFO以上的日志
        console.setLevel('DEBUG')
        #设置控制台输出日志的格式
        console.setFormatter(formatter)
        #获取当前时间
        local_time=time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
        #存放日志文件路径
        log_path = os.path.dirname(os.getcwd()) + '\\log\\'
        #定义日志名字,不加路径默认存放在当前目录下。
        file_name=log_path +local_time +'.log'
        #再创建一个handler,将日志信息输出到目录
        file_log=logging.FileHandler(file_name,encoding='utf-8')
        #设置输出目录日志的等级,输出INFO以上的日志
        file_log.setLevel('DEBUG')
        #设置目录日志的格式
        file_log.setFormatter(formatter)
        #添加多个规则，就可以让一个logger记录多个日志。
        logger.addHandler(console)
        logger.addHandler(file_log)
        #根据传入的等级调用。
        if level=='DEBUG':#详细信息,一般在调试问题时使用
            logger.debug(msg)
        elif level=='INFO':#证明事情按预期工作
            logger.info(msg)
        elif level=='WARNING':#譬如磁盘空间不足,产生的警告信息
            logger.warning(msg)
        elif level=='ERROR':#发生严重错误,不能往下执行功能
            logger.error(msg)
        elif level=='CRITICAL':#严重错误,整个IDE不能运行
            logger.critical(msg)
        #关闭日志记录器
        logger.removeHandler(console)
        logger.removeHandler(file_log)
    def debug(self,msg):
        #调用get_log函数
        self.get_log(msg,'DEBUG')
    def info(self,msg):
        self.get_log(msg,'INFO')
    def warning(self,msg):
        self.get_log(msg,'WARNING')
    def error(self,msg):
        self.get_log(msg,'ERROR')
    def critical(self,msg):
        self.get_log(msg,'CRITICAL')
# if __name__=='__main__':
#     # local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     # log_path = os.path.dirname(os.getcwd())
#     # path="test_api_"+local_time+".log"
#     rq = time.strftime('%Y-%m-%d %H%M', time.localtime(time.time()))
#     log_path = os.path.dirname(os.getcwd()) + '/log/'
#     log_name = log_path +'Meiye'+rq +'.log'
#     print(log_name)
'''


if __name__=='__main__':
    mylog = logger('excel').get_logger()
    mylog.info("#############初始化数据")
