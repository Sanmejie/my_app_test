from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from loguru import logger
from time import sleep
import sys,os
print(os.path.abspath(os.path.join(os.getcwd(), 'Log/')))
logger.add(sys.stderr, format='{time} {level} {message}', filter='my module', level='INFO')
logger.add(os.path.abspath(os.path.join(os.getcwd(), 'Log/'))+"\\file_{time}.log", encoding="utf-8", rotation="500 MB")
# 封装driver方法、定位元素或者很多元素的方法、点击方法、输入元素方法、获取消息方法

class Base:

    def __init__(self, driver):
        # 初始化driver -- 供find_element 和 find_elements使用
        self.driver = driver

    def search_element(self, loc, timeout=20, poll=1.0):
        """
        定位单个元素 - 显示等待
        :param loc: 元祖 (定位类型，类型属性值) 例子:(By.ID,"com.xx.xx")
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_elements(self, loc, timeout=15, poll=1):
        """
        定位多个元素 - 显示等待
        :param loc: 元祖 (定位类型，类型属性值) 例子:(By.ID,"com.xx.xx")
        :param timeout: 超时时间
        :param poll: 搜索间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        """
        点击元素
        :param loc:
        :return:
        """
        self.search_element(loc).click()

    def click_elements(self, loc, mins=0):
        '''
        点击元素后等待n秒返回
        :param loc: 定位元素列表
        :param mins: 时间 秒
        :return:
        '''
        for i in loc:
            self.search_element(i).click()
            sleep(mins)
            self.put_keypad(67)


    def input_element(self, loc, text):
        """
        输入内容
        :param loc:
        :param text: 输入的文本
        :return:
        """
        input_text = self.search_element(loc)
        input_text.clear()
        input_text.send_keys(text)

    def put_keypad(self,num):
        # 物理按键方法
        self.keyevent(num)

    def get_toast(self, message):
        # 获取提示消息
        try:
            xpath = "//*[contains(@text,'{}')]".format(message)
            toast_message = self.search_element((By.XPATH, xpath), timeout=10, poll=0.1)
            return toast_message.text
        except Exception as e:
            return False
