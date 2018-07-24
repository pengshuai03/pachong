import urllib.request
import re

i = 0
#驼峰命名    方法 小驼峰  类名  大驼峰
#获取小说内容
def getNovelContent():

    #获取主页源代码  HTTPResponse 对象
    html = urllib.request.urlopen('https://www.ybdu.com/xiaoshuo/10/10237/').read()
    html = html.decode('gbk')

    path = 'E:/Github爬虫项目/douluo'
    #获取超链接
    #正则表达式
    #通配符  匹配所有的链接    .*?  匹配所有   分组匹配
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    #增加匹配效率
    reg = re.compile(reg)
    urls = re.findall(reg, html)
    for i in urls:
        novel_url = i[0]
        novel_title = i[1]
        chapt = urllib.request.urlopen(novel_url).read()
        chapt_html = chapt.decode('gbk')
        #正则表达式
        reg = '</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'
        #S 多行匹配
        reg = re.compile(reg, re.S)
        chapt_content = re.findall(reg, chapt_html)
        #替换
        chapt_content = chapt_content[0].replace('&nbsp;&nbsp;&nbsp;&nbsp;',' ')
        chapt_content = chapt_content.replace('<br />',' ')


        #下载小说
        print('正在保存 %s'%novel_title)
        # w 读写模式  wb 二进制读写
        #f = open('{}.txt'.format(novel_title),'w')
        #f.write(chapt_content)
        #f.close()
        with open('/E:/Github爬虫项目/image.txt'.format(novel_title), 'w') as f:
            f.write(chapt_content)

        i += 1,


    getNovelContent()