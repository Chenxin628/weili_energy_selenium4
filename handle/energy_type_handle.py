#coding=utf-8
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
from log.log import CaseLog

action=ActionMethod()
class Energy_type_handle():
    def __init__(self):
        LoginTest()
        self.log = CaseLog()
        self.logger = self.log.get_log()
        #进入用能类型管理
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("用能类型管理","ant-menu-item")

    def add_energy(self,name_t):
        # 判断是否存在"仪表风"，存在则删除
        action.delete_data(name_t,"vxe-body--row","确 定","button")
        action.get_xpath_text(name_t)


        #添加能源
        action.get_xpath_element("新增")
        action.click_element("ant-select-selection__rendered",2)
        action.select_data(name_t,"ant-select-dropdown-menu-item")
        action.get_xpath_element("确 定",-1)
   
        action.read_text("ant-message-notice-content")  

        action.sleep_time(2)
        


        if action.get_xpath_text(name_t):
            self.logger.info("找到文本:"+name_t+",能源类型添加成功")
            # return True
        else:
            self.logger.info("未找到文本:"+name_t+",能源类型添加失败")
            # return False

        
