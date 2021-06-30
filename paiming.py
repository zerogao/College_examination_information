
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
from xlsxwriter import Workbook
import  pandas  as pd
work_content=[]
chacters=[508,
514,
0,
515,
521,
535,
482,
508,
506,
0,
503,
505,
0,
0,
498,
481,
504,
489,
520,
493,
481,
0,
487,
488,
0,
482,
0,
483,
481,
481,
498,
481,
526,
481,
0,
484,
0,
485,
0,
0,
489,
516,
507,
0,
0,
0,
514,
497,
523,
524,
0,
0,
488,
504,
487,
492,
486,
0,
0,
494,
524,
523,
515,
505,
497,
0,
520,
0,
502,
481,
485,
481,
499,
496,
481,
490,
0,
485,
490,
481,
0,
0,
0,
509,
497,
494,
0,
500,
0,
0,
505,
494,
0,
0,
0,
486,
0,
498,
481,
485,
0,
492,
485,
482,
481,
494,
481,
481,
508,
483,
502,
516,
508,
535,
495,
0,
494,
0,
496,
0,
519,
0,
527,
510,
510,
481,
496,
483,
493,
0,
487,
0,
0,
0,
481,
487,
0,
0,
0,
0,
0,
506,
493,
497,
498,
487,
489,
0,
518,
517,
514,
0,
0,
0,
516,
0,
0,
481,
481,
481,
489,
0,
481,
484,
488,
0,

]//放置分数

         
def get_work(driver):
    try:
        
        i=1
        name=driver.find_element_by_xpath("//*[@id='NewsTitle']").text
        for chacter in chacters:
            print(chacter)
            print("第{}条".format(i))
           
            for num in range(1,250):
                # 根据属性选择器查找
                
                if str(chacter)=="0":
                    work_content.append({"排名": ""})
                    i=i+1
                    break
                string="//*[@id='newsbody_class']/div[6]/table/tbody/tr["+str((num+1))+"]/td[1]/div/span"
               
                code = driver.find_element_by_xpath(string).text
              
                if code==str(chacter):
                    
                    string2="//*[@id='newsbody_class']/div[6]/table/tbody/tr["+str((num+1))+"]/td[3]/div/span"
                    paiming=driver.find_element_by_xpath(string2).text
                    i=i+1
                    work_content.append({"排名": paiming})
                    break
                string1="//*[@id='newsbody_class']/div[6]/table/tbody/tr["+str((num+1))+"]/td[5]/div/span"
                code1 = driver.find_element_by_xpath(string1).text
                if code1==str(chacter):
                    string2="//*[@id='newsbody_class']/div[6]/table/tbody/tr["+str((num+1))+"]/td[7]/div/span"
                    paiming=driver.find_element_by_xpath(string2).text
                    i=i+1
                    work_content.append({"排名": paiming})
                    break

    finally:
        driver.close()
        players = work_content
        ordered_list = ["排名",]

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
    driver.get('http://www.sxkszx.cn/news/2020724/n8583104772.html')#对应网址

    time.sleep(2)
    get_work(driver)