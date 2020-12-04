from Base.Base import Base
from loguru import logger
from time import sleep
import Page


class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_sy_login_btn(self):
        # 点击首页的登录按钮
        logger.debug("首页的登录按钮")
        self.click_element(Page.sy_login_btn_XPATH)
    #
    # def click_login_sign_btn(self):
    #     # 点击个人中心登录按钮
    #     self.click_element(Page.perso_login_btn_id)
    def login_input_page(self, username, passwd):
        # 登陆操作
        # 输入用户名
        logger.debug("输入用户名{}".format(username))
        self.input_element(Page.login_user_ID, username)
        # 输入密码
        logger.debug("输入密码{}".format(passwd))
        self.input_element(Page.login_password_ID, passwd)

        # 点击登陆按钮
        logger.debug("点击登录")
        self.click_element(Page.login_submit_ID)

    # def if_tv_residue_status(self):
    #     # 判断学习卡剩余天数是否存在
    #     try:
    #         self.search_element(Page.perso_residue_btn_id)
    #         return True
    #     except Exception as e:
    #         return False

    def login_close_page(self):
        # 关闭登陆信息输入页
        # self.keyevent(4)
        logger.debug("点击取消按钮")
        # self.(put_keypad4)
        sleep(1)

        self.click_element(Page.cancel_XPATH)
        sleep(2) #
        self.click_element(Page.login_back_ID)

    def login_back_page(self):
        logger.debug("点击右上角后退按钮")
        self.click_element(Page.login_back_ID)

    def logout_page(self):
        # 从首页退出登录
        logger.debug("从首页退出登录")
        # 点击个人中心
        self.click_element(Page.sy_personal_btn_XPATH)
        # 点击退出登录
        self.click_element(Page.unlogin_unlogin_XPATH)
        # 点击确定按钮
        self.click_element(Page.queding_XPATH)
        # 点击右上角按钮
        sleep(2) #
        self.click_element(Page.login_back_ID)

    def error_dispose(self,e):
        '''

        :param e: 异常信息
        :return:
        '''
        logger.error(e)
        self.error_screenshot(e)