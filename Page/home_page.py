from Base.Base import Base
import Page
'''
首页操作
'''
class xx_course_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def for_click_sy_element(self):
        '''
        循环点击首页元素
        :return:
        '''
        self.click_elements(Page.sy_login_lsit_fun(),3)

    def click_sy_login_btn(self):
        '''
        点击登录
        :return:
        '''
        self.click_element(Page.sy_login_btn_XPATH)