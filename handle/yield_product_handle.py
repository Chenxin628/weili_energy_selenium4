#coding=utf-8
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
from log.log import CaseLog

action=ActionMethod()
class Yield_handle():
    def __init__(self):
        LoginTest()
        self.log = CaseLog()
        self.logger = self.log.get_log()

        #进入生产层级信息
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("生产产品信息","ant-menu-item")


    def add_yield(self,name_t,num_t,company_t,benchmark,average,limit,admittance,advanced):
        
        # 判断是否存在"脚本测试新建产品"，存在则删除
        action.delete_data(name_t,"vxe-body--row","确 定","button")
        action.get_xpath_text(name_t)
        

        #添加产品
        action.click_element("anticon-plus")
        action.element_send_keys("ant-input",name_t,2)
        action.element_send_keys("ant-input",num_t,3)
        action.element_send_keys("ant-input",company_t,4)
        action.get_placeholder_element("请输入标杆值",benchmark)
        action.get_placeholder_element("请输入平均值",average)
        action.get_placeholder_element("请输入限定值",limit)
        action.get_placeholder_element("请输入准入值",admittance)
        action.get_placeholder_element("请输入先进值",advanced)
     
        action.select_data("确 定","ant-modal-footer","button")[-1].click()

        if action.get_xpath_text(name_t):
            self.logger.info("找到文本:"+name_t+",生产产品添加成功")
            return True
        else:
            self.logger.info("未找到文本:"+name_t+",生产产品添加失败")
            return False








