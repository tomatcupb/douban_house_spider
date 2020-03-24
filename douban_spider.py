# -*- coding: utf-8 -*-
# module douban_spider
# Created on 2020/3/24 10:23

import re
import random
import json
from conf import *
from util import *
from selenium import webdriver
from db_util import DBUtil
from constants import keywords

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Chrome()
db = DBUtil(DB_CONF)

start_time = time.time()
house_list = []

for i in range(START_PAGE, END_PAGE):
    driver.get(BASE_URL % (i * 25))
    # 此处的xpath解析与一般的似乎不同，只能解析标签，标签内部的属性需要用 .text，.get_attribute('href')获取
    title = driver.find_elements_by_xpath("//td[@class='title']/a")
    url = driver.find_elements_by_xpath("//td[@class='title']/a")
    comments_num = driver.find_elements_by_xpath("//td[@class='']")
    time_pub = driver.find_elements_by_xpath("//td[@class='time']")

    for j in range(len(title)):
        for k in keywords:
            t = str(title[j].get_attribute('title'))
            if re.findall(k, t):
                # 插入数据库字段：title, url, md5, comments_num, publish_time, keyword, create_time, update_time
                url_md5 = get_md5(str(url[j].get_attribute('href')))
                house_list.append((
                    '%s' % str(title[j].get_attribute('title')), '%s' % str(url[j].get_attribute('href')),
                    '%s' % url_md5, '%s' % str(comments_num[j].text) if str(comments_num[j].text) else '0',
                    '%s' % str(time_pub[j].text), '%s' % k, '%s' % now_time('%Y-%m-%d %H:%M:%S'),
                    '%s' % now_time('%Y-%m-%d %H:%M:%S')))
                break

    time.sleep(random.random() * 2)

# 写入本地文件
house_list_str = json.dumps(house_list, indent=2, ensure_ascii=False)
with open(OUTPUT_PATH, 'a') as f:
    f.write(house_list_str)

# 写入mysql数据库
for house in house_list:
    sql_insert = INSERT_SQL % (
        house[0], house[1], house[2], house[3], house[4], house[5], house[6], house[7]
        )
    try:
        db.execute(sql_insert)
    except Exception:
        print("插入失败！"+house[1])

end_time = time.time()
duration = end_time - start_time

print(duration)
print(len(house_list))

driver.quit()
