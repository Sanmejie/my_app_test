from appium import webdriver
import os
from loguru import logger


def get_driver():
    """
    :param pac: 包名
    :param act: 启动名
    :return:
    """
    desired_caps = {}
    # 平台 - 必填
    desired_caps['platformName'] = 'Android'
    # 系统版本 - 非必填，填写就必须正确
    # desired_caps['platformVersion'] = '6.0.1'
    # 设备名称
    desired_caps['deviceName'] = '小度设备'
    # 设置收到下一条命令的等待时间。超时appium会关闭
    desired_caps['newCommandTimeout'] = '300'
    # 获取toast支持
    # desired_caps['automationName'] = 'Uiautomator2'
    # desired_caps['app'] = 'apk绝对路径'
    # # app包名
    desired_caps['appPackage'] = 'com.deskmateones'
    # app启动名
    desired_caps['appActivity'] = '.ui.activity.SplashActivity'
    # 不重置app
    desired_caps["noReset"] = True
    # 设置中文输入
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True

    # 声明driver驱动 - session ？？？
    # 接口地址：http://127.0.0.1:4723/wd/hub  POST
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    return driver