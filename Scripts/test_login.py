import pytest, sys, os
sys.path.append(os.getcwd())
from Page.login_page import Login_Page
from Base.init_driver import get_driver
from Base.read_data import Op_Data
from time import sleep
def get_data():
    # 读取返回数据
    data_list = []
    data = Op_Data("data.yml").read_yaml().get("Login_data")
    for i in data:
        for o in i.keys():
            data_list.append((o,i.get(o).get("phone"),i.get(o).get("passwd"),
                              i.get(o).get("get_mess"),i.get(o).get("expect_message"),
                              i.get(o).get("tag")))
    return data_list
class Test_Login:

    def setup_class(self):
        # 实例化登陆对象
        self.LP_obj = Login_Page(get_driver())
        # 点击个人中心
        sleep(5)
        self.LP_obj.click_sy_login_btn()

    def teardown_class(self):
        self.LP_obj.driver.quit()

    @pytest.mark.parametrize("case_num, username, passwd,get_mess,expect_message, tag", get_data())
    def test_login_page(self, case_num, username, passwd, get_mess, expect_message, tag):
        """
        :param username: 用户名
        :param passwd: 密码
        :param get_mess: toast传参
        :param expect_message: 预期toast消息
        :param tag: 1 标记登陆成功用例
        :return:
        """
        # 点击登陆注册
        self.LP_obj.click_sy_login_btn()
        # 登陆操作
        self.LP_obj.login_input_page(username, passwd)
        if tag:
            try:
                # 获取登陆成功toast
                suc_msg = self.LP_obj.get_toast(get_mess)
                # # 获取我的状态
                # order_status = self.LP_obj.if_my_order_status()
                # 退出登录
                self.LP_obj.logout_page()
                assert suc_msg == expect_message

            except Exception as e:
                print(e)
                # 关闭登陆信息输入页面
                self.LP_obj.login_close_page()
                assert False
        else:
            try:
                # 获取登陆失败toast消息
                fail_msg = self.LP_obj.get_toast(get_mess)
                if fail_msg:
                    assert fail_msg == expect_message
                else:
                    assert False
            finally:
                self.LP_obj.login_close_page()


