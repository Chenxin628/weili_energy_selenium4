#coding=utf-8
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
from log.log import CaseLog

action=ActionMethod()

class Collect_data_handle():
    def __init__(self):
        LoginTest()
        self.log = CaseLog()
        self.logger = self.log.get_log()
        #进入采集数据项信息
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("采集数据项信息","ant-menu-item")
        # 列表更改为表结构
        action.click_element("ant-switch-inner")
        action.click_element("vxe-input--inner")
        action.get_xpath_element("100条/页")
        action.show_wait("vxe-pager--next-btn.is--disabled")
    
    def collect_data_parameter(self,name_t,range_t,product_t,product_unit_t,data_type_t,data_class_t,usage_code_t,frequency_t,max_t,data_source_t,formula_t,repor_t,equipment_t=None):
        # 采集项名称
        action.get_placeholder_element("请输入采集数据项指标名称",name_t)
        # 数据最大值
        action.get_placeholder_element("请输入数据最大值（空不预警）",max_t)
        # 范围
        action.click_element("ant-select-selection__placeholder",3)
        action.select_data(range_t,"ant-select-dropdown-menu-item")
        # 生产工序
        action.click_element("ant-select-selection__placeholder",4)
        action.select_data(product_t,"ant-select-dropdown-menu-item")
        # 生产工序单元
        action.click_element("ant-select-selection__placeholder",5)
        action.sleep_time()
        action.select_data(product_unit_t,"ant-select-dropdown-menu-item")

        if range_t=="重点耗能设备":
            # 重点用能设备
            action.click_element("ant-select-selection__placeholder",6)
            action.select_data(equipment_t,"ant-select-dropdown-menu-item")

        if data_type_t!="":
            # 采集数据类型
            action.click_element("ant-select-selection__placeholder",7)
            action.select_data(data_type_t,"ant-select-dropdown-menu-item")

        # 数据分类
        action.click_element("ant-select-selection__placeholder",8)
        action.select_data(data_class_t,"ant-select-dropdown-menu-item")

        # 用途编码
        action.click_element("ant-select-selection__placeholder",9)
        action.select_data(usage_code_t,"ant-select-dropdown-menu-item")

        # 采集频率
        action.click_element("ant-select-selection__placeholder",10)
        action.select_data(frequency_t,"ant-select-dropdown-menu-item")
      
        # 是否用能公式
        action.click_element("ant-select-selection__placeholder",11)
        action.select_data(formula_t,"ant-select-dropdown-menu-item")

        if data_source_t!="":
            # 数据采集来源
            action.click_element("ant-select-selection__placeholder",12)
            action.select_data(data_source_t,"ant-select-dropdown-menu-item")
            # 是否上报
            action.click_element("ant-select-selection__placeholder",13)
            action.select_data(repor_t,"ant-select-dropdown-menu-item")
        else:
            # 是否上报
            action.click_element("ant-select-selection__placeholder",12)
            action.select_data(repor_t,"ant-select-dropdown-menu-item")


    def add_collect_data(self,name_t,range_t,product_t,product_unit_t,data_type_t,data_class_t,usage_code_t,frequency_t,max_t,data_source_t,formula_t,repor_t,equipment_t=None):
       
        
        # 判断是否存在"脚本测试新建采集数据项"，存在则删除
        element=action.select_form_data(name_t,"body--wrapper","fixed-right--wrapper","vxe-body--row",-1,"button")
        if element:
            element.click()
            action.get_xpath_element("确 定")
        action.get_xpath_text(name_t)
        #添加采集项
        action.get_xpath_element("新增")
        action.sleep_time()
       
        self.collect_data_parameter(name_t,range_t,product_t,product_unit_t,data_type_t,data_class_t,usage_code_t,frequency_t,max_t,data_source_t,formula_t,repor_t,equipment_t)
       
        action.select_data("确 定","ant-modal-footer","button")[-1].click()

        action.click_cancel("ant-message-notice-content","关 闭")
        
        if action.get_xpath_text(name_t):
            self.logger.info("找到文本:"+name_t+",采集项添加成功")
            return True
        else:
            self.logger.info("未找到文本:"+name_t+",采集项添加失败")
            return False

 
