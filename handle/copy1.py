#coding=utf-8
from base.actionMethod import ActionMethod

import os
class LoginTest1():
    def __init__(self) :
        #登入操作
        action_method1=ActionMethod()
        action_method1.get_url("http://172.16.2.210:8081/user/login")
        
        action_method1.show_wait("ant-layout-footer")
        
        #判断是否有登陆状态，有登陆态则跳过登陆步骤，没有则重新登陆
        if action_method1.get_element("ant-avatar-circle"):
            print("已有登陆状态，跳过登陆步骤")
        else:
            action_method1.sleep_time()
            if action_method1.get_element("ant-modal-confirm-btns"):
                # print("找到重新登陆按钮")
                action_method1.click_element("ant-btn-primary",1)
            print("没有登陆状态，重新登陆")
            filename=os.path.join(os.getcwd()+"\\img\\code.png")
            text=action_method1.get_code(filename)
            action_method1.element_send_keys("ant-input","admin",0)
            action_method1.element_send_keys("ant-input","123456",1)
            action_method1.element_send_keys("ant-input",text,2)
            action_method1.is_success(filename)

        if action_method1.get_element("anticon-menu-fold"):
            action_method1.click_element("anticon-menu-fold")
        
        #进入用能类型管理
        action_method1.select_data("企业信息","ant-menu-submenu-inline")
        action_method1.select_data("用能类型管理","ant-menu-item")

        # 判断是否存在"仪表风"，存在则删除
        action_method1.delete_data('其他风',"vxe-body--row","确 定","button")
        action_method1.get_xpath_text('其他风')


        #添加能源
        action_method1.get_xpath_element("新增")
        action_method1.click_element("ant-select-selection__rendered",2)
        action_method1.select_data('其他风',"ant-select-dropdown-menu-item")
        action_method1.get_xpath_element("确 定",-1)
        action_method1.sleep_time(4)
        t=action_method1.read_text("ant-message-notice-content")  
        print(t)
        # action_method1.close_browser()
  

if __name__ == '__main__':
    LoginTest1()
