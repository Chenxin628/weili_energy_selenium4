#coding=utf-8
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
from log.log import CaseLog

action=ActionMethod()
class Production_handle():
    def __init__(self):
        LoginTest()
        self.log = CaseLog()
        self.logger = self.log.get_log()
        #进入生产层级信息
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("生产层级信息","ant-menu-item")


    def add_level(self,level_name_t,level_num_t):
        
        # 判断是否存在90工序，存在查看是否存在90工序下的单元，存在则删除
        if action.select_data(level_num_t,"custom-tree-node"):
            action.show_wait("vxe-pager--total")
            action.sleep_time()
            while action.get_element("vxe-pager--total").text !="共 0 条记录":
                action.sleep_time()
                action.click_element("c-btn-danger",1)
                action.get_xpath_element("确 定")
                # action.delete_data("确定删除该工序单元吗？","ant-popover-inner","确 定","button")
                action.show_wait("anticon-check-circle")

            action.click_element("c-btn-danger")
            action.get_xpath_element("确 定")
        action.get_xpath_text(level_num_t)
        
 
        #添加90工序
        action.click_element("custom-tree-node",0)
        action.click_element("anticon-plus",0)
        action.element_send_keys("ant-input",level_name_t,1)
        action.element_send_keys("ant-input",level_num_t,2)
        action.select_data("确 定","ant-modal-footer","button")[-1].click()

        if action.get_xpath_text(level_num_t):
            self.logger.info("找到文本:"+level_name_t+",生产层级添加成功")
            return True
        else:
            self.logger.info("未找到文本:"+level_name_t+",生产层级添加失败")
            return False

        


    def add_Unit(self,level_num_t,name_t,unit_num_t,yield_t,date_t):
        #添加90下的工序单元
        action.select_data(level_num_t,"custom-tree-node")
        action.select_data("新增","table-operator","button")[0].click()
        action.element_send_keys("ant-input",name_t,1) 
        action.element_send_keys("ant-input",unit_num_t,2) 
        action.element_send_keys("ant-input",yield_t,3) 
        action.click_element("ant-input",4)
        action.element_send_keys("ant-calendar-input",date_t)
        action.select_data("确 定","ant-modal-footer","button")[-1].click()

        if action.get_xpath_text(name_t):
            self.logger.info("找到文本:"+name_t+",生产工序单元添加成功")
            return True
        else:
            self.logger.info("未找到文本:"+name_t+",生产工序单元添加失败")
            return False

        
        


