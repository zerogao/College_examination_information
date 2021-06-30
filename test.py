
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
from xlsxwriter import Workbook
import  pandas  as pd
work_content=[]


def get_work(driver):
    try:
        
        i=1
        name=driver.find_element_by_xpath("//*[@id='NewsTitle']").text
        for num in range(1,167):
            # 根据属性选择器查找
            print("第{}条".format(i))
            n=1
            string="//*[@id='newsbody_class']/div[8]/table/tbody/tr["+str((num+1))+"]/td["+str(n)+"]/div/span"
            code = driver.find_element_by_xpath(string).text
            
            #print(code)
            
            n=n+1
            string="//*[@id='newsbody_class']/div[8]/table/tbody/tr["+str((num+1))+"]/td["+str(n)+"]/div/span"
        
            school = driver.find_element_by_xpath(string).text
            n=n+1
            
            string="//*[@id='newsbody_class']/div[8]/table/tbody/tr["+str((num+1))+"]/td["+str(n)+"]/div/span"
            
            type = driver.find_element_by_xpath(string).text
            n=n+2
            string="//*[@id='newsbody_class']/div[8]/table/tbody/tr["+str((num+1))+"]/td["+str(n)+"]/div/span"
            grade = driver.find_element_by_xpath(string).text

            work_content.append({"学校代码": code, "学校": school, "类型":type, "最低分":grade})
            i=i+1

    finally:
        driver.close()
        players = work_content
        ordered_list = ["学校代码", "学校", "类型", "最低分",]

        wb = Workbook("./%s.xlsx" % name)
        ws = wb.add_worksheet(name)

        first_row = 0
        for header in ordered_list:
          col = ordered_list.index(header)
          ws.write(first_row, col, header)

        row = 1
        for player in players:
          for _key, _value in player.items():
             col = ordered_list.index(_key)
             ws.write(row, col, _value)
          row += 1
        wb.close()



if __name__ == '__main__':


    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.sxkszx.cn/news/2020818/n8675106809.html')#输入链接

    time.sleep(2)
   
    get_work(driver)