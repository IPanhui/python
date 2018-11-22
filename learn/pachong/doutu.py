import requests
import re
import pymysql

# 连接数据库
db = pymysql.connect(host = '127.0.0.1',port = 3306,
                     db='db', user = 'root', passwd = '',
                     charset = 'utf8')

cursor = db.cursor()
cursor.execute('select * form images')
print(cursor.fetchall())




# 小驼峰
# 获取图片列表
def getImagesList():
    # 获取斗图网源代码
    urls = 'https://www.doutula.com/article/list/'
    html = requests.get(urls).text
    # 正则表达式 通配符　.*?　匹配所有　分组匹配
    reg = r'data-original="(.*?)".*?alt="(.*?)"'

    #　增加匹配效率的　Ｓ:多行匹配
    reg = re.compile(reg,re.S)
    imagesList = re.findall(reg,html)
    for i in imagesList:
        image_url = i[0]
        image_title = i[1]



getImagesList()