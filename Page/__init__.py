# import sys,os
# sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By


"""
    首页
"""
# 首页登录列表
sy_login_list = ['登录/注册', '体验课程', '小学课程', '初中课程', '高中课程', '专题课程', '作业辅导', '模拟考试', '直播课堂', '订购/激活']


# sy_login_list_element=
def sy_login_list_fun():
    """
    :return: 首页登录xpath定位列表
    """
    sy_login_list_element = []
    for i in sy_login_list:
        sy_login_list_element.append((By.XPATH,
                                      "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top' and "
                                      "@text=" + str(
                                          i) + "]"))
    return sy_login_list_element


# 首页登录按钮
sy_login_btn_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top' and @text='登录/注册']")
# 个人中心
sy_personal_btn_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top' and @text='个人中心']")
# 体验课程
sy_tycourse_btn_XPTH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top' and @text='体验课程']")
# 小学课程
sy_xxcourse_btn_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top' and @text='小学课程']")
# 初中课程
sy_czcourse_btn_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top' and @text='初中课程']")
# 高中课程
sy_gzcourse_btn_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top' and @text='高中课程']")
# 专题课程
sy_ztcourse_btn_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top_one' and @text='专题课程']")
# 作业辅导
sy_homework_help_btn_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top_one' and @text='作业辅导']")
# 模拟考试
sy_practice_test_btn_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top_one' and @text='模拟考试']")
# 直播课堂
sy_Live_classroom_btn_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top_one' and @text='直播课堂']")
# 订购/激活
sy__btn_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top_one' and @text='订购/激活']")

"""
体验课程
"""

# 同步课程
ty_tbcourse_btn_XPATH = (By.XPATH, "//android.widget.TextView[@text='同步课程']")
# 作业辅导
ty_zyfd_btn_XPATH = (By.XPATH, "//android.widget.TextView[@text='作业辅导']")
# 国学
ty_gx_btn_XPATH = (By.XPATH, "//android.widget.TextView[@text='国学']")

'''
小学课程--版本
'''
xx_course_versions_list = ['人教版', '苏教版', '鲁教版', '北师大', '浙教版', '湘教版', '冀教版', '鄂教版', '西师大', '外研社', '语文S版', '沪教版', '教科版',
                           '青岛版', '青岛(五四)', '人教(五四)']


def xx_course_versions_lsit_fun():
    """
    循环操作小学课程版本
    :return:
    """
    xx_course_lsit_versions_element = []
    for i in xx_course_grade_list:
        xx_course_lsit_versions_element.append((By.XPATH,
                                                "//android.widget.TextView["
                                                "@resource-id='com.deskmateones:id/tv_versions' and @text=" + str(
                                                    i) + "]"))
    return xx_course_lsit_versions_element


# 人教版
xx_course_versions_rj_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='人教版']")
# 苏教版
xx_course_versions_sj_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='苏教版']")
# 鲁教版
xx_course_versions_lj_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='鲁教版']")
# 北师大
xx_course_versions_bsd_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='北师大']")
# 浙教版
xx_course_versions_zj_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='浙教版']")
# 湘教版
xx_course_versions_xj_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='湘教版']")
# 冀教版
xx_course_versions_jj_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='冀教版']")
# 鄂教版
xx_course_versions_ej_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='鄂教版']")
# 西师大
xx_course_versions_xs_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='西师大']")
# 外研社
xx_course_versions_wys_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='外研社']")
# 语文s版
xx_course_versions_yws_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='语文S版']")
# 沪教版
xx_course_versions_hj_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='沪教版']")
# 教科版
xx_course_versions_jk_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='教科版']")
# 青岛版
xx_course_versions_qd_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='青岛版']")
# 青岛(五四)
xx_course_versions_qdws_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='青岛(五四)']")
# 人教(五四)
xx_course_versions_rjws_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='人教(五四)']")
'''
小学课程--选择年级
'''
# 小学课程-年级列表
xx_course_grade_list = ['一年级', '二年级', '三年级', '四年级', '五年级', '六年级']


def xx_course_grade_lsit_fun():
    """
    循环操作小学年级
    :return:
    """
    xx_course_lsit_grade_element = []
    for i in xx_course_grade_list:
        xx_course_lsit_grade_element.append((By.XPATH,
                                             "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions"
                                             "' and @text=" + str(
                                                 i) + "]"))
    return xx_course_lsit_grade_element


# 一年级
xx_course_grade_one_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='一年级']")
# 二年级
xx_course_grade_two_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='二年级']")
# 三年级
xx_course_grade_three_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='三年级']")
# 四年级
xx_course_grade_four_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='四年级']")
# 五年级
xx_course_grade_five_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='五年级']")
# 六年级
xx_course_grade_six_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_versions' and @text='六年级']")

'''
登录页
'''
# 用户名
login_user_ID = (By.ID, "com.deskmateones:id/act_landing_name")
# 密码
login_password_ID = (By.ID, "com.deskmateones:id/et_landing_password")
# 登录
login_submit_ID = (By.ID, "com.deskmateones:id/bt_landing_submit")
# 忘记密码
login_wjmm_Id = (By.ID, "com.deskmateones:id/tv_landing_wjmm")
# 注册
login_register_ID = (By.ID, "com.deskmateones:id/tv_landing_zhuce")
# 百度一键登录
login_baidu_ID = (By.ID, "com.deskmateones:id/but_baidu")
# 右上角返回按钮
login_back_ID = (By.ID, "com.deskmateones:id/iv_title_back")

'''退出登录页'''
# 修改密码
unlogin_uppassword_XPATH = (
    By.XPATH, "//android.widget.Button[@resource-id='com.deskmateones:id/bt_back_pwd' and @text='修改密码']")
# 退出登录
unlogin_unlogin_XPATH = (
    By.XPATH, "//android.widget.Button[@resource-id='com.deskmateones:id/bt_back_login' and @text='退出登录']")
# 详情
unlog_details_ID = (By.ID, "com.deskmateones:id/tv_details")

# 确定
queding_XPATH = (
    By.XPATH, "//android.widget.Button[@resource-id='com.deskmateones:id/btn_one2one_positive' and @text='确定']")
# 取消
cancel_XPATH = (
    By.XPATH, "//android.widget.Button[@resource-id='com.deskmateones:id/btn_one2one_cancel' and @text='取消']")
# 注册
register_XPATH = (
    By.XPATH, "//android.widget.Button[@resource-id='com.deskmateones:id/btn_one2one_positive' and @text='注册']")

"""
专题课程
"""

zt_course_list = ['英语专区', '总复习课', '作文辅导', '应用题辅导', '书法辅导', '微课预习', '学习方法', '课文朗诵', '生字听写', '单词听写']

# 英语专区
zt_course_english_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top' and @text='英语专区']")
# 总复习课
zt_course_zfx_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top' and @text='总复习课']")
# 作文辅导
zt_course_zw_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top' and @text='作文辅导']")
# 应用题辅导
zt_course_yyt_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top' and @text='应用题辅导']")
# 书法辅导
zt_course_sffd_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top_one' and @text='书法辅导']")
# 微课预习
zt_course_wkyx_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top_one' and @text='微课预习']")
# 学习方法
zt_course_xxff_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top_one' and @text='学习方法']")
# 课文朗诵
zt_course_kwls_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top_one' and @text='课文朗诵']")
# 生字听写
zt_course_sztx_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top_one' and @text='生字听写']")
# 单词听写
zt_course_dctx_XPATH = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.deskmateones:id/tv_home_top_one' and @text='单词听写']")
# 返回
zt_course_back_ID = (By.ID, "com.deskmateones:id/iv_title_back")

# # 设置按钮
# person_setting_btn_id = (By.ID, "com.tpshop.malls:id/setting_btn")
# # 我的订单
# my_order_btn = (By.XPATH, "//*[contains(@text,'我的订单') and contains(@resource-id,'com.tpshop.malls:id/title_txtv')]")
# """
#     设置页面
# """
# # 安全退出按钮
# logout_btn_id = (By.ID, "com.tpshop.malls:id/exit_btn")
