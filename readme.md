## 文档说明

本文档利用Python编写了一个简易的爬虫软件，将历年高考录取各个高校近五年录取的最低分和全省排名写入excel中，本文档只提供编写思想，下面以山西高考为例：

进入山西高考官网：[山西高考招生网](http://www.sxkszx.cn/index.html)：

![image-20210626231515554](https://github.com/zerogao/College_examination_information/blob/master/image-20210626231515554.png)

官网中有历年各个批次高校的最低录取分数，以2020年本科一批A类院校为例：[链接](http://www.sxkszx.cn/news/2020818/n8675106809.html)



![image-20210626231815812](https://github.com/zerogao/College_examination_information/blob/master/image-20210626231815812.png)

这里我们只爬取理科类院校;

![image-20210626232607325](https://github.com/zerogao/College_examination_information/blob/master/image-20210626232607325.png)

然后根据得到的最低分去匹配当年的一分一段表来获取全省排名：

![image-20210626232837963](https://github.com/zerogao/College_examination_information/blob/master/image-20210626232837963.png)





## 因每省情况不同，本项目只供参考！
