import pytest, sys, os

sys.path.append(os.getcwd())
from Page.login_page import Login_Page
from Base.init_driver import get_driver
from Base.read_data import Op_Data
from time import sleep
from loguru import logger


def get_data():
    # 读取返回数据
    data_list = []
    data = Op_Data("data.yml").read_yaml().get("Login_data")
    for i in data:
        for o in i.keys():
            data_list.append((o, i.get(o).get("phone"), i.get(o).get("passwd"),
                              i.get(o).get("get_mess"), i.get(o).get("expect_message"),
                              i.get(o).get("tag")))
    return data_list


class Test_Login:

    def setup_class(self):
        # 实例化登陆对象
        logger.info("调起同桌100")
        os.system('adb shell am broadcast -a com.baidu.duer.query -e q "打开同桌100"')
        # os.system('adb shell am broadcast -a com.baidu.duer.query -e q "退出"')
        os.system('adb shell am broadcast -a com.baidu.duer.query -e q "打开同桌100"')
        os.system('adb shell am broadcast -a com.baidu.duer.query -e q "打开同桌100"')
        self.LP_obj = Login_Page(get_driver())
        # 点击个人中心
        # sleep(5)
        # self.LP_obj.click_sy_login_btn()

    def teardown_class(self):
        self.LP_obj.driver.quit()

    @pytest.mark.parametrize("case_num, username, passwd,get_mess,expect_message, tag", get_data())
    def test_login_page(self, case_num, username, passwd, get_mess, expect_message, tag):
        """
        :param username: 用户名
        :param passwd: 密码
        :param get_mess: toast传参
        :param expect_message: 预期toast消息
        :param tag: 1 标记登陆成功用例   2 标记账号不存在   3标记登录失败
        :return:
        """
        # 点击登陆注册
        # logger.info("点击登录/注册")
        # self.LP_obj.click_sy_login_btn()
        # 登陆操作
        logger.info("登录相关操作")
        self.LP_obj.click_sy_login_btn()
        self.LP_obj.login_input_page(username, passwd)
        if tag == 1:
            try:
                # 获取登陆成功toast
                logger.info("正向登录用例")
                suc_msg = self.LP_obj.get_toast(get_mess)
                logger.debug("获取登录成功toast：{}".format(suc_msg))
                # 退出登录
                self.LP_obj.logout_page()
                assert suc_msg == expect_message
                logger.success("断言成功{}=={}".format(suc_msg, expect_message))

            except Exception as e:
                # 捕获异常信息+截图
                self.LP_obj.error_dispose(e)
                # 关闭登录信息输入页面
                self.LP_obj.login_back_page()
                assert False

        elif tag == 2:
            try:
                logger.debug("登录不存在的账号用例")
                # 获取登陆成功toast
                suc_msg = self.LP_obj.get_toast(get_mess)
                logger.debug("获取账号不存在toast：{}".format(suc_msg))
                # 退出登录
                self.LP_obj.login_close_page()
                assert suc_msg == expect_message
                logger.success("断言成功{}=={}".format(suc_msg, expect_message))

            except Exception as e:
                # 捕获异常信息+截图
                self.LP_obj.error_dispose(e)
                assert False
        elif tag == 3:
            logger.debug("账号或密码错误用例")
            try:
                # 获取登陆失败toast消息
                fail_msg = self.LP_obj.get_toast(get_mess)
                logger.debug("登录失败toast：{}".format(fail_msg))
                if fail_msg:
                    assert fail_msg == expect_message
                    logger.success("断言成功：{}=={}".format(fail_msg,expect_message))
                else:
                    assert False
                self.LP_obj.login_back_page()

            except Exception as e:
                # 捕获异常信息+截图
                self.LP_obj.error_dispose(e)
                sleep(3)
                assert False

'''
allure generate report/ -o report/html
'''