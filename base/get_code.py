
from PIL import Image
import pytesseract
from selenium.webdriver.common.by import By

class GetCode(object):
    def __init__(self,driver):
        self.driver = driver

    '''
    获取验证码图片
    '''
    def get_code_image(self,file_name):
        #1、 截图首页
        self.driver.save_screenshot(file_name)
        # 2、获取验证码坐标
        code_element= self.driver.find_element(By.CLASS_NAME,"ant-col-offset-1")
        left=code_element.location['x']*1.25
        top=code_element.location['y']*1.25
        right=code_element.size['width']*1.25+left
        height=code_element.size['height']*1.25+top
        im=Image.open(file_name)
        img=im.crop((left,top,right,height))
        # 3、保存截图的验证码
        img.save(file_name)

    '''
    解析图片，获取验证码
    '''
    def code_online(self,file_name):
        self.get_code_image(file_name)
        image=Image.open(file_name)
        pytesseract.pytesseract.tesseract_cmd = 'D://Program Files//Tesseract-OCR//tesseract.exe'
        testdata_dir_config = '--tessdata-dir "D://Program Files//Tesseract-OCR//tessdata"'
        text = pytesseract.image_to_string(image, lang = 'eng', config=testdata_dir_config)
        
        # text = pytesseract.image_to_string(Image.open(image),config=testdata_dir_config,lang='eng')
        # text=pytesseract.image_to_string(image)
        return text
