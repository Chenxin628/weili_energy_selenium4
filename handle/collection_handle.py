#coding=utf-8
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
from log.log import CaseLog

action=ActionMethod()

class Collection_handle():
    def __init__(self):
        LoginTest()
        self.log = CaseLog()
        self.logger = self.log.get_log()
        # 进入采集源配置
        action.select_data("网闸网关","ant-menu-submenu-inline")
        action.select_data("采集源配置","ant-menu-item")

    def select_table(self,table_t):
        action.click_element("ant-dropdown-menu-item",1)
        action.click_element("ant-select-selection__rendered",1)
        action.select_data(table_t,"ant-select-dropdown-menu-item")
        action.click_element("ant-btn-primary",0)
        action.sleep_time()

    def add_collection(self,name_t,table_t,id_t,ip_t,port_t,byte_t,frequency_t=None):
        
        # 进入"脚本测试新增采集源"的"配置解析规则",判断是否存在热能表表计，存在则删除
        if action.select_data(name_t,"vxe-body--row"):
            action.delete_data(name_t,"vxe-body--row","配置解析规则","button")
            self.select_table(table_t)
            while action.get_element("vxe-pager--total").text!="共 0 条记录":
                action.click_element("ant-btn-link",2)
                action.get_xpath_element("确 定")
                action.sleep_time()
            action.select_data("采集源配置","ant-menu-item")
            
        # 判断是否有名称为"脚本测试新增采集源"的采集源，有则删除
        action.delete_data(name_t,"vxe-body--row","删除","button","确 定")
        # action.get_xpath_text(name_t)


        # 添加采集源
        # 点击添加按钮
        action.click_element("ant-btn",2)
        # 采集分类备注
        action.element_send_keys("ant-input",name_t,1)
        # ModBus服务ID
        action.element_send_keys("ant-input",id_t,2)
        # IP
        action.element_send_keys("ant-input",ip_t,3)
        # 端口
        action.element_send_keys("ant-input-number-input",port_t,0)
        # 字节大小端
        action.click_element("ant-select-selection__rendered",1)
        action.select_data(byte_t,"ant-select-dropdown-menu-item")
        # 采集频率（秒）
        if frequency_t!=None:
            action.element_send_keys("ant-input-number-input",frequency_t,1)
        # 点击提交
        action.get_xpath_element("提 交")
        action.sleep_time()
        if action.get_xpath_text(name_t):
            self.logger.info("找到文本:"+name_t+",采集源添加成功")
            return True
        else:
            self.logger.info("未找到文本:"+name_t+",采集源添加失败")
            return False

 


    def add_parameter(self,table_t,name_t):
        # 进去表参数配置的热能表
        action.click_element("ant-btn-primary",3)
        action.click_element("ant-select-arrow-icon")
        action.select_data(table_t,"ant-select-dropdown-menu-item")
        action.sleep_time(2)

        # 添加参数
        # action.get_xpath_element("添加")
        # action.get_element("ant-form-item-control","3").click
        action.get_ele_element("drag-wrap","ant-select-enabled")
  
        action.get_xpath_element(name_t)
        # action.get_element("ant-select-selection__placeholder","null")[-1].click()
        # action.select_data(name_t,"ant-select-dropdown-menu-item")
        action.get_xpath_element("保 存")

        action.click_cancel("ant-message-notice-content","取 消")

    def add_meter(self,collect_t,table_t,num_t,name_t,methon_t,address_t):
        # 进入"脚本测试新增采集源"的"配置解析规则"
        action.delete_data(collect_t,"vxe-body--row","配置解析规则","button")
        # 查找热能表的表计
        self.select_table(table_t)
        # 添加表计
        action.click_element("ant-btn-primary",2)
        action.element_send_keys("ant-input",num_t,2)
        action.element_send_keys("ant-input",name_t,3)
        action.click_element("ant-select-arrow-icon",2)
        action.select_data(methon_t,"ant-select-dropdown-menu-item")
        action.element_send_keys("ant-input-number-input",address_t)
        action.click_element("ant-btn-link",1)
        if action.get_xpath_text(num_t):
            self.logger.info("找到文本:"+num_t+",表计添加成功")
            return True
        else:
            self.logger.info("未找到文本:"+num_t+",表计添加失败")
            return False



