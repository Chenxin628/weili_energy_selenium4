#coding=utf-8
from selenium import webdriver
import os
from base.get_code import GetCode
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
import HTMLTestReportCN
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from log.log import CaseLog




#打开浏览器
chrome_options = Options()
chrome_options.add_argument('-ignore-certificate-errors')
chrome_options.add_argument('-ignore -ssl-errors')
chrome_options.add_argument(r'--user-data-dir=C://Users//老男神//AppData//Local//Google//Chrome//User Data\Default')
driver = webdriver.Chrome(options=chrome_options, executable_path="D:\Program Files\Python\chromedriver")
# driver = webdriver.Chrome()
driver.maximize_window()

class ActionMethod:
    def __init__(self):
        self.log = CaseLog()
        self.logger = self.log.get_log()

    '''输入地址'''
    def get_url(self,url):
        driver.get(url)
        driver.implicitly_wait(2)

    '''截图'''
    def save_img(self,file_path):
        driver.save_screenshot(file_path)
        
    '''刷新'''
    def refresh(self):
        driver.refresh()

    '''通过xpath文本进行定位点击'''
    def get_xpath_element(self,text,column=None):
        time.sleep(0.5)
        if column==None:
            # next_btn=driver.find_element_by_xpath(f'//*[contains(text(),"{text}")]')
           next_btn= driver.find_element(By.XPATH,f'//*[contains(text(),"{text}")]')
            
        else:
            # next_btn=driver.find_elements_by_xpath(f'//*[contains(text(),"{text}")]')[column]
            next_btn= driver.find_elements(By.XPATH,f'//*[contains(text(),"{text}")]')[column]

        driver.execute_script("arguments[0].click();", next_btn)
    
    """
        查找是否存在text
    """
    def get_xpath_text(self,text):
        time.sleep(0.5)
        try:
            # driver.find_element_by_xpath(f'//*[contains(text(),"{text}")]')
            driver.find_elements(By.XPATH,f'//*[contains(text(),"{text}")]')
            return True
        except:
            return False
            
    
    '''通过input的placeholder文本进行定位点击'''
    def get_placeholder_element(self,text,value,column=None):
        time.sleep(0.5)
        # element=driver.find_element_by_class_name("ant-modal-body")
        element=driver.find_element(By.CLASS_NAME,"ant-modal-body")

        if column==None:
            # element.find_element_by_xpath(f".//input[@placeholder='{text}']").send_keys(value)
            element.find_element(By.XPATH,f".//input[@placeholder='{text}']").send_keys(value)

        else:
            # element.find_elements_by_xpath(f'//input[@placeholder="{text}")]')[column].send_keys(value)
            element.find_elements(By.XPATH,f"//input[@placeholder='{text}']")[column].send_keys(value)


    '''定位元素'''
    def get_element(self,key,num=None):
        try:
            if(num!=None):
                if num=="null":
                    element=driver.find_element(By.CLASS_NAME,key)
                else:   
                    element=driver.find_elements(By.CLASS_NAME,key)[num]   

            else:
                element=driver.find_element(By.CLASS_NAME,key)   
                
            return element
        except:
            print("定位元素",key,"数值",num,"不存在")
            return False

    '''键盘事件'''
    def key_event(self,key,event,num=None):
        element =self.get_element(key,num)
        if event=='a':
            element.send_keys(Keys.CONTROL,'a')
        elif event=='c':
            element.send_keys(Keys.CONTROL,'c')
        elif event=='x':
            element.send_keys(Keys.CONTROL,'x')
        elif event=='v':
            element.send_keys(Keys.CONTROL,'v')
        elif event=='backSpace':
            element.send_keys(Keys.BACK_SPACE)
        elif event=='space':
            element.send_keys(Keys.SPACE)
        elif event=='tab':
            element.send_keys(Keys.TAB)
        elif event=='esc':
            element.send_keys(Keys.ESCAPE)
        elif event=='enter':
            element.send_keys(Keys.ENTER)

    '''输入元素'''
    def element_send_keys(self,key,value,num=None):
        self.key_event(key,num,"a")
        self.get_element(key,num).send_keys(value)
    
    '''点击元素'''
    def click_element(self,key,num=None):
        self.sleep_time()
        next_btn=self.get_element(key,num)
        driver.execute_script("arguments[0].click();", next_btn)
        time.sleep(0.5)
    
    '''等待'''
    def sleep_time(self,t=None):
        if t!=None:
            time.sleep(t)
        else:
            time.sleep(1)
    
    '''关闭浏览器'''
    def close_browser(self):
        time.sleep(2)
        driver.close()
    
    '''获取title'''
    def get_title(self):
        title = driver.title
        return title
    
    '''判断是否有下一页，有则点击下一页'''
    def click_next(self):
        self.sleep_time()
        while True:
            try:
                # driver.find_element_by_class_name("vxe-pager--next-btn.is--disabled")
                driver.find_element(By.CLASS_NAME,"vxe-pager--next-btn.is--disabled")

                print("最后一页")
                break
            except:
                print("下一页")
                self.show_wait("vxe-pager--next-btn")
                # driver.find_element_by_class_name("vxe-pager--next-btn").click()
                driver.find_element(By.CLASS_NAME,"vxe-pager--next-btn").click()


    '''
        通过列表查找元素

        text:需要查找的文本
        key:一整行的列表元素
        tag:用于行内的分割的tag

    '''
    def select_data(self,text,key,tag=None):
        time.sleep(0.5)
        # item=driver.find_elements_by_class_name(key)
        item=driver.find_elements(By.CLASS_NAME,key)

        for i in range(len(item)):
            result = str(text) in str(item[i].text)
            if result == True:
                # print("列表找到了文本:"+text)
                
                if tag!=None:
                    # element = item[i].find_elements_by_tag_name(tag)
                    element = item[i].find_elements(By.TAG_NAME,tag)

                    return element
                else:
                    # self.get_xpath_element(text)
                    item[i].click()
                    return item[i]         

    '''
        删除列表查找到的元素
        
        select_text:方法select_data中的text
        select_key:方法select_data中的key
        select_tag:方法select_data中的tag
        text:删除按钮的名称
        text1:删除按钮的名称1

    '''
    def delete_data(self,select_text,select_key,text,select_tag=None,text1=None):
        element=self.select_data(select_text,select_key,select_tag)
        if element:
            if text=="确 定":
                element[-1].click()
            else:
                element[-2].click()
            self.get_xpath_element(text)
            if text1!=None:
                self.get_xpath_element(text1)
            # print("执行删除操作，重新添加")
            self.logger.info("执行删除操作，尝试重新添加")


    """
        若保存失败则显示原因，并点击取消
    """
    def click_cancel(self,key,text):
        self.show_wait(key)
        try:
            # if '成功' not in driver.find_element_by_class_name(key).text:
            if '成功' not in driver.find_element(By.CLASS_NAME,key).text:
                message=driver.find_element(By.CLASS_NAME,key).text
                self.logger.warning(message)
                self.get_xpath_element(text)
            elif '成功' in driver.find_element(By.CLASS_NAME,key).text:
                message=driver.find_element(By.CLASS_NAME,key).text
                self.logger.info(message)
        except:
            # self.get_xpath_element(text)
            self.logger.warning("操作失败")
            print("未找到元素"+key)



    '''获取验证码'''
    def get_code(self,filename):
        self.sleep_time()
        self.get_code_text = GetCode(driver)
        text = self.get_code_text.code_online(filename)
        return text
        
    '''验证码错误时重新输入'''
    def is_success(self,file_name):
        self.sleep_time()
        while True: 
            try:
                driver.find_element(By.CLASS_NAME,"ant-avatar-circle")
                print("登陆成功")
                break
            except:
                print("验证码错误,重新输入")
                text=self.get_code(file_name)
                driver.find_elements(By.CLASS_NAME,"ant-input")[2].send_keys(text)
                driver.find_element(By.CLASS_NAME,"login-button").click()
    
    
    '''
        通过左侧表格查找右侧表格元素

        text:需要查找的文本
        left_key0:左侧表格的div元素
        rigth_key0:右侧表格的div元素
        form_key:表格的行元素
        column:控制输出第几列
        tag:用于行内的分割的tag
    '''
    def select_form_data(self,text,left_key0,rigth_key0,form_key,column,tag):
        time.sleep(0.5)
        # 左侧表格元素
        left_element0=driver.find_elements(By.CLASS_NAME,left_key0)
        left_element1=left_element0[1].find_elements(By.CLASS_NAME,form_key)
        # 右侧表格元素
        rigth_element0=driver.find_elements(By.CLASS_NAME,rigth_key0)
        rigth_element1=rigth_element0[1].find_elements(By.CLASS_NAME,form_key)

        # 遍历左侧表格元素,直到找到text所在的i，代入右侧表格的i
        for i in range(len(left_element1)):
            result = str(text) in str(left_element1[i].text)
            if result == True:
                print("列表找到了文本:"+text)
                # self.logger.info("列表找到了文本:"+text)
                
                list = rigth_element1[i]
                element1 = list.find_elements(By.TAG_NAME,tag)
                print(str(element1[column].text))

                return element1[column]
                    
    '''
        目前无效
    '''
    def dete(self):
        left_element0=driver.find_elements(By.CLASS_NAME,"fixed-right--wrapper")
        for i in range(len(left_element0)):
            element1 = left_element0[1].find_elements(By.TAG_NAME,"td")
            element1[-1].click()
            time.sleep(0.5)
            dd=driver.find_elements(By.CLASS_NAME,"ant-popover-buttons")
            dd1=dd.find_elements(By.TAG_NAME,"button")
            dd1[1].click()

    def get_ele_element(self,p_key,c_key):
        element=driver.find_element(By.CLASS_NAME,p_key)
        element.find_element(By.CLASS_NAME,c_key).click()
       

    '''
        输出测试报告
        case_name:case名称
        repory_name:报告名称
    '''
    def generate_report(self,case_name,repory_name):
        file_path = os.path.join(os.getcwd()+"\\report\\"+repory_name+".html")
        f = open(file_path,'wb')
        suite = unittest.TestLoader().loadTestsFromTestCase(case_name)
        runner = HTMLTestReportCN.HTMLTestRunner(stream=f,title=repory_name,description=u"测试报告",verbosity=2)
        runner.run(suite)
    
    '''显示等待'''
    def show_wait(self,key):
        try:
            wait = WebDriverWait(driver,20,0.5)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME,key)))
            # WebDriverWait(driver,10,poll_frequency=0.5,ignored_exceptions=None)
        except:
            print("未找到元素")

    '''读取text'''
    def read_text(self,key):
        if self.show_wait(key):
            t=driver.find_element(By.CLASS_NAME,key).text
            if t=="操作成功！":
                return True
            else:
                return False
        else:
            print("未找到元素："+key)
