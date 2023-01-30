#coding=utf-8
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
from log.log import CaseLog


action=ActionMethod()
class Energy_report_handle():
    def __init__(self):
        LoginTest()
        self.log = CaseLog()
        self.logger = self.log.get_log()
        action.get_xpath_element("能效报告")
        #进去报告模板定义
        action.get_xpath_element("报告模板定义")

    def add_report(self,name_t):
        #添加报告
        action.delete_data(name_t,"custom-tree-node","确 定","a")
        action.get_xpath_text(name_t)

        action.click_element("anticon-plus-square")
        action.element_send_keys("ant-input",name_t,1)
        action.click_element("ant-btn-primary",1)

        if action.get_xpath_text(name_t):
            self.logger.info("找到文本:"+name_t+",能效报告添加成功")
            return True
        else:
            self.logger.info("未找到文本:"+name_t+",能效报告添加失败")
            return False



    def add_module(self,name_t):
        # 添加报告的模块
        action.select_data(name_t,"custom-tree-node")
        action.get_xpath_element("添加模块")
        action.click_element("ant-checkbox-input")
        action.click_element("ant-btn-primary",1)
        # if action.get_xpath_text(name_t):
        #     self.logger.info("找到文本:"+name_t+",报告参数添加成功")
        #     return True
        # else:
        #     self.logger.info("未找到文本:"+name_t+",报告参数添加失败")
        #     return False


       
