CREATE TABLE `house_table` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` text COMMENT '抓取页中的链接的title',
  `url` varchar(2000) NOT NULL COMMENT '链接的url',
  `md5` varchar(40) NOT NULL COMMENT '链接的MD5',
	`comments_num` varchar(40) NOT NULL COMMENT '评论数量',
  `publish_time` varchar(200) NOT NULL COMMENT '发布的时间',
  `keyword` varchar(200) NOT NULL COMMENT '分类关键词',
	`create_time` varchar(50) NOT NULL COMMENT '记录创建时间',
	`update_time` varchar(50) NOT NULL COMMENT '记录更新时间',
  PRIMARY KEY (`md5`),
  KEY `id` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;