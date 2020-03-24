# -*- encoding: utf-8 -*-

# 数据库配置
DB_CONF = {'HOST': '127.0.0.1', 'USER': 'root', 'PASSWD': 'root', 'DB': 'douban_house', 'CHARSET': 'utf8',
           'PORT': 3306}

# 豆瓣找房主页
BASE_URL = "https://www.douban.com/group/beijingzufang/discussion?start=%s"

# 文件输出路径
OUTPUT_PATH = "C:\\Users\\SirAlex\\Desktop\\douban_house.json"

# 插入数据库sql
INSERT_SQL = "insert into house_table (`title`, `url`, `md5`, `comments_num`, `publish_time`, `keyword`," \
             "`create_time`, `update_time`) " \
             "values ('%s','%s','%s','%s','%s','%s','%s','%s') on DUPLICATE KEY UPDATE update_time=TIME(now())"


# 爬取的起始和结束页码
START_PAGE = 1
END_PAGE = 10
