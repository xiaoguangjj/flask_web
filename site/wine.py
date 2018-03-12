import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    #reg = r'src="(.+?\.jpg@200w_200h)" '
    reg = r'src="https.*?jpg@200w_200h"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)  #html匹配按照imgre规则匹配
    #imglist = 'https://hmres.huimin100.cn//Upload/HMProductImg/0/0/0/10569/1.JPG@400w_400h'
    return imglist      

html = getHtml("https://pcshop.huimin100.cn/index.php/home/index/categorylist/cateid/1/pid/1.html")

print getImg(html)











