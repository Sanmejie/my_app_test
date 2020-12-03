from Base.Base import Base
import Page
'''
小学课程操作
'''
class xx_course_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def for_click_xx_course_versions_element(self):
        '''
        循环点击小学版本
        :return:
        '''
        self.click_elements(Page.xx_course_versions_lsit_fun(),3)

    def for_click_xx_course_grade_element(self):
        '''     业务中可能有问题 ？？？返回会返回到首级
        循环点击小学年级
        :return:
        '''
        self.click_elements(Page.xx_course_grade_lsit_fun(),3)


