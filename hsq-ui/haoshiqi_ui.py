from appium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from appium.webdriver.common.touch_action import TouchAction
import os
from HTMLTestRunner_PY3 import HTMLTestRunner
import subprocess

current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
print(current_time)

class Test(unittest.TestCase):
        @classmethod
        def setUpClass(self):
                # 启动appium
                cmd = ['appium','-g','01.log']
                subprocess.Popen(cmd,shell=True)
                time.sleep(3)
                #连接设备参数
                desired_caps = {'platformName': 'Android',
                                'platformVersion': '9',
                                'deviceName': 'HUAWEI P20',
                                'automationName': 'uiautomator2',
                                'app': "C:\\Users\\dwdtwster\\Desktop\\app-beta-release.apk",
                                # "appPackage": "com.doweidu.android.haoshiqi/.main.view.MainActivity",
                                # "appActivity": ".main.view.MainActivity"
                                }
                                
                self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
                time.sleep(2)


                print(self.driver.get_window_size())
                self.x1 = self.driver.get_window_size()['width']
                self.y1 = self.driver.get_window_size()['height']

                self.driver.find_element_by_android_uiautomator("text(\"始终允许\")").click()
                self.driver.find_element_by_android_uiautomator("text(\"始终允许\")").click()
                for i in range(2):
                        self.driver.swipe(9/10*self.x1, 1/2*self.y1, 1/10*self.x1, 1/2*self.y1, 300)
                        time.sleep(1)
                # self.driver.find_element_by_android_uiautomator("text(\"立即体验\")").click()
                x = self.x1
                y = self.y1
                a = 560/1080
                b = 1980/2244
                self.driver.tap([(a*x, b*y)],2) 
                time.sleep(2)                
        def test_login(self):
                driver = self.driver
                driver.find_element_by_android_uiautomator("text(\"我的\")").click()
                driver.find_element_by_android_uiautomator("text(\"未登录\")").click()
                driver.find_element_by_android_uiautomator("text(\"账号密码登录\")").click()
                time.sleep(1)
                driver.find_element_by_id("com.doweidu.android.haoshiqi:id/et_phone").send_keys('15261875682')
                driver.find_element_by_id("com.doweidu.android.haoshiqi:id/et_pwd").send_keys('123456')
                driver.find_element_by_id("com.doweidu.android.haoshiqi:id/btn_login").click()
                time.sleep(2)
        def test_pagedview(self):
                x = self.x1
                y = self.y1
                driver = self.driver
                driver.find_element_by_android_uiautomator("text(\"首页\")").click()
                for i in range(3):
                        self.driver.swipe(9/10*x, 1/2*y, 1/10*x, 1/2*y, 300)
                        time.sleep(1)
                for i in range(3):
                        self.driver.swipe(1/10*x, 1/2*y, 9/10*x, 1/2*y, 300)
                        time.sleep(1)    
                # for i in range(4):
                #         driver.swipe(1/7*x, 1/2*y, 5/7*x, 1/2*y, 300)
                #         time.sleep(1)
        def test_banner(self):
                x = self.x1
                y = self.y1
                driver = self.driver
                # driver.find_element_by_android_uiautomator("text(\"首页\")").click()
                #banner
                a = 500/1080
                b = 600/2244
                driver.tap([(a*x, b*y)],2) 
                #返回
                a = 80/1080
                b = 150/2244
                driver.tap([(a*x, b*y)],2) 
        def test_belowButton(self):
                x = self.x1
                y = self.y1
                driver = self.driver
                driver.find_element_by_android_uiautomator("text(\"新品推荐\")").click()
                driver.find_element_by_android_uiautomator("text(\"购物车\")").click()   
                driver.find_element_by_android_uiautomator("text(\"分类\")").click()  
        def test_verticalButton(self):
                x = self.x1
                y = self.y1
                driver = self.driver
                a = 100/1080
                b = 300/2244
                driver.tap([(a*x, b*y)],2) 
                a = 100/1080
                b = 500/2244
                driver.tap([(a*x, b*y)],2) 
                a = 100/1080
                b = 700/2244
                driver.tap([(a*x, b*y)],2)   
                # driver.find_element_by_android_uiautomator("text(\"呵呵呵\")").click()
                # driver.find_element_by_android_uiautomator("text(\"精选推荐0001\")").click()
        def test_goods(self):
                x = self.x1
                y = self.y1
                driver = self.driver
                a = 400/1080
                b = 450/2244
                driver.tap([(a*x, b*y)],2) 
                #返回
                a = 80/1080
                b = 150/2244
                driver.tap([(a*x, b*y)],2) 
                # driver.find_element_by_android_uiautomator("text(\"威化饼干\")").click()

        def test_searchActivity(self):
                x = self.x1
                y = self.y1
                driver = self.driver
                driver.find_element_by_android_uiautomator("text(\"首页\")").click()
                time.sleep(1)
                driver.swipe(1/2*x, 1/2*y, 1/2*x, 1/3*y, 200)
                i=0
                while i < 5:
                        try:
                                driver.find_element_by_android_uiautomator("text(\"多件优惠-付钱 多件优惠付钱-3，4，5\")").click()#尝试点击元素
                                break
                        except Exception as e:
                                driver.swipe(x/2,y*0.8,x/2,y*0.2)#滑动屏幕
                # self.assertEqual(driver.find_element_by_id('com.doweidu.android.haoshiqi:id/tv_title').text,u'营销活动','找不到【营销活动多件 营销活动打折】活动')
                # driver.find_element_by_android_uiautomator("text(\"营销活动多件 营销活动付钱\")").click()
                time.sleep(2)
        def test_shoppingCart(self):
                driver = self.driver
                driver.find_element_by_android_uiautomator("text(\"加入购物车\")").click()
                driver.find_element_by_android_uiautomator("text(\"确认\")").click()
        def test_order(self):
                driver = self.driver  
                x = self.x1
                y = self.y1   
                driver.find_element_by_id("com.doweidu.android.haoshiqi:id/btn_fastbuy").click()
                time.sleep(2)
                driver.find_element_by_android_uiautomator("text(\"确认\")").click()
                time.sleep(2)
                driver.find_element_by_id("com.doweidu.android.haoshiqi:id/btn_submit").click()
                driver.find_element_by_id("com.doweidu.android.haoshiqi:id/btn_ok").click()
                a = 80/1080
                b = 150/2244
                driver.tap([(a*x, b*y)],2) 
                a = 80/1080
                b = 150/2244
                driver.tap([(a*x, b*y)],2) 
                a = 80/1080
                b = 150/2244
                driver.tap([(a*x, b*y)],2) 
        def test_search(self):
                x = self.x1
                y = self.y1   
                driver = self.driver
                driver.find_element_by_id("com.doweidu.android.haoshiqi:id/tv_search").click()
                time.sleep(1)
                driver.find_element_by_id("com.doweidu.android.haoshiqi:id/et_search").send_keys('流程测试')
                time.sleep(2)
                # 点击搜索按钮 
                driver.keyevent(66)
                driver.press_keycode(66)
                time.sleep(2)
                # #返回
                a = 80/1080
                b = 150/2244
                driver.tap([(a*x, b*y)],2) 
                #取消
                a = 1000/1080
                b = 150/2244
                driver.tap([(a*x, b*y)],2) 
                driver.find_element_by_id("com.doweidu.android.haoshiqi:id/btn_cancel").click()
          
        @classmethod
        def tearDownClass(cls):
                # appium 关闭
                cmd = ['taskkill', '/f', '/t', '/im', 'node.exe']
                subprocess.run(cmd)

if __name__ == "__main__":
        # unittest.main()
        testcase=unittest.TestSuite()                                                                               #实例化对象，创建一个测试集
        testcase.addTests([
        Test('test_login')
        ,Test('test_pagedview')
        ,Test('test_banner'),
        Test('test_belowButton')
        ,Test('test_verticalButton')
        ,Test('test_goods'),
        Test('test_searchActivity')
        ,Test('test_shoppingCart')
        ,Test('test_order'),
        Test('test_search')
        ])    #添加测试用例列表
        # testcase.addTests(unittest.TestLoader().loadTestsFromTestCase())
        f=open(r"C:\Users\dwdtwster\Desktop\Test.html",'wb')                                                        #定义报告生成的路径
        runner=HTMLTestRunner(stream=f,title='好食期ui自动化测试报告',description='简单描述')
        runner.run(testcase)




# class Test(unittest.TestCase):
#     def test_login(self):
        
        # time.sleep(2)
        
        
# if __name__ == "__main__":
#     unittest.main()
    

