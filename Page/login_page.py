from Base.Base import Base
import Page

class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_sy_login_btn(self):
        # 点击首页的登录按钮
        self.click_element(Page.sy_login_btn_XPATH)
    #
    # def click_login_sign_btn(self):
    #     # 点击个人中心登录按钮
    #     self.click_element(Page.perso_login_btn_id)
    def login_input_page(self, username, passwd):
        # 登陆操作
        # 输入用户名
        self.input_element(Page.login_user_ID, username)
        # 输入密码
        self.input_element(Page.login_password_ID, passwd)
        # 点击登陆按钮
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
        self.put_keypad(4)
    def logout_page(self):
        # 退出登录
        self.click_element(Page.unlogin_unlogin_XPATH)


