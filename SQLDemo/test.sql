show variables like '%log%';
set global long_query_time = 2;
set global slow_query_log = false;
set global log_queries_not_using_indexes = false;
show tables;
explain select max(password_last_changed) from user;

# mysql 定时任务
SELECT @@event_scheduler;
SHOW VARIABLES LIKE 'event%';
set global EVENT_SCHEDULER = 1;

drop procedure if exists update_dayhit;
create procedure update_dayhhit() # 创建存储过程
BEGIN
  update duomi_data SET v_dayhit = 0;
END;

drop event if exists update_dayhit;
create event update_dayhit
on schedule every 1 day starts timestamp '2018-06-13 00:00:00'
on completion preserve
do
begin
  call update_dayhit();
end;

# 创建视频数据库
create database if not exists video;
use video;

create table if not exists videos(
  v_id varchar(32) primary key,
  video_origin varchar(10),
  list_type varchar(10),
  video_des text,
  video_name varchar(40),
  spell_name varchar(200),
  video_addr varchar(10),
  video_type varchar(100),
  video_time varchar(10),
  video_actor varchar(200),
  video_director varchar(40),
  video_language varchar(10),
  front_image_url varchar(100),
  crawl_time datetime,
  crawl_update_time datetime,
  is_ic tinyint default 0
)engine = InnoDB default charset = utf8;

create table if not exists episodes(
  video_id varchar(32),
  v_id_pre varchar(32),
  episode int,
  video_url varchar(100) unique key
)engine = InnoDB default charset = utf8;
alter table episodes add v_id_pre varchar(32) after video_id;

# 创建错误信息记录数据库
create database if not exists errors;
use errors;

create table if not exists errvideos(
  list_type varchar(20),
  video_url varchar(200) unique key,
  reason text,
  video_name varchar(80),
  r_time datetime
)engine = InnoDB default charset = utf8;

create table if not exists errgrammers(
  info text,
  insert_sql text,
  param text,
  video_name varchar(80)
)engine = InnoDB default charset = utf8;

# 创建scrapy爬取信息数据库
create database if not exists crawlinfo;
use crawlinfo;

create table if not exists info(
  crawl_name varchar(10),
  start_time datetime,
  end_time datetime,
  spend_time int,
  crawling int,
  crawled int,
  crawlerr int
)engine = InnoDB default charset = utf8;


# ip
create table if not exists ips(
  ip char(15) unique,
  port char(5),
  proxy_type char(5),
  speed float
)engine = InnoDB default charset = utf8;
create unique index uq_ip on ips(ip);


# 测试表
create database if not exists test;
use test;

create table if not exists videos(
  video_id char(32) primary key,
  is_ic int default 0,
  video_origin varchar(10),
  list_type varchar(10),
  video_des text,
  video_name varchar(40),
  spell_name varchar(200),
  video_addr varchar(10),
  video_type varchar(100),
  video_time varchar(10),
  video_actor varchar(200),
  video_director varchar(40),
  video_language varchar(10),
  front_image_url varchar(100),
  crawl_time datetime,
  crawl_update_time datetime
)engine = InnoDB default charset = utf8;

create table if not exists episodes(
  video_id varchar(32),
  episode int,
  video_url varchar(100) unique key
)engine = InnoDB default charset = utf8;

create table if not exists errvideos(
  list_type varchar(10),
  video_url varchar(100),
  video_name varchar(40)
)engine = InnoDB default charset = utf8;

create table if not exists errgrammers(
  err_time datetime,
  grammer text,
  insert_sql text,
  param longtext,
  video_name varchar(80)
)engine = InnoDB default charset = utf8;


# 视频数据库
create database if not exists wanshi;
use wanshi;

-- phpMyAdmin SQL Dump
-- version 3.4.8
-- http://www.phpmyadmin.net
--
-- 主机: sql.w86.vhostgo.com
-- 生成日期: 2018 年 05 月 30 日 14:29
-- 服务器版本: 5.1.65
-- PHP 版本: 5.2.17

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `xiangadmin`
--

-- --------------------------------------------------------
# session存储表
create table if not exists wanshi_session(
  sess_id varchar(30) primary key,
  sess_data mediumtext,
  sess_time int(10)
)engine = InnoDB default charset = utf8;

# 视频播放记录表
create table if not exists wanshi_play_history(
  u_name varchar(20),
  u_sys varchar(15),
  p_info varchar(80),
  p_time int(10),
  p_url varchar(30)
)engine = InnoDB default charset = utf8;

# 用户登录记录表
create table if not exists wanshi_login_info(
  l_id int(10) primary key auto_increment,
  u_name varchar(20),
  l_ip varchar(16),
  l_time int(10),
  l_sys varchar(15)
)engine = InnoDB default charset = utf8;

--
-- 表的结构 `admin`
--

CREATE TABLE IF NOT EXISTS `admin` (
  `idadmin` int(11) NOT NULL AUTO_INCREMENT COMMENT '管理员id',
  `adminuser` varchar(45) NOT NULL COMMENT '管理员登录名',
  `adminpwd` varchar(45) NOT NULL COMMENT '管理员密码',
  `adminLately` varchar(45) NOT NULL COMMENT '最近登陆',
  `status` int(1) DEFAULT '1' COMMENT '状态，0表示停用，1表示正常使用',
  `admincol` varchar(45) DEFAULT NULL,
  `adminpower` int(1) DEFAULT '2' COMMENT '管理员权限，1为超级管理员，2为普通管理员',
  PRIMARY KEY (`idadmin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='管理员表' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `commodity`
--

CREATE TABLE IF NOT EXISTS `commodity` (
  `idcommodity` int(11) NOT NULL AUTO_INCREMENT COMMENT '商品表id',
  `commoditycol` varchar(45) DEFAULT NULL,
  `commodityname` varchar(45) NOT NULL COMMENT '商品分类名',
  PRIMARY KEY (`idcommodity`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_admin`
--

CREATE TABLE IF NOT EXISTS `duomi_admin` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL DEFAULT '',
  `password` varchar(32) NOT NULL DEFAULT '',
  `logincount` smallint(6) NOT NULL DEFAULT '0',
  `loginip` varchar(16) NOT NULL DEFAULT '',
  `logintime` int(10) NOT NULL DEFAULT '0',
  `groupid` smallint(4) NOT NULL,
  `state` smallint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_arcrank`
--

CREATE TABLE IF NOT EXISTS `duomi_arcrank` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `rank` smallint(6) NOT NULL DEFAULT '0',
  `membername` char(20) NOT NULL DEFAULT '',
  `adminrank` smallint(6) NOT NULL DEFAULT '0',
  `money` smallint(8) unsigned NOT NULL DEFAULT '500',
  `scores` mediumint(8) NOT NULL DEFAULT '0',
  `purviews` mediumtext,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_buy`
--

CREATE TABLE IF NOT EXISTS `duomi_buy` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL DEFAULT '0',
  `vid` int(11) NOT NULL DEFAULT '0',
  `kptime` int(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_card`
--

CREATE TABLE IF NOT EXISTS `duomi_card` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ckey` varchar(80) NOT NULL,
  `cpwd` varchar(80) NOT NULL,
  `climit` int(11) NOT NULL,
  `maketime` timestamp NULL DEFAULT NULL,
  `usetime` timestamp NULL DEFAULT NULL,
  `uname` varchar(20) DEFAULT NULL,
  `status` varchar(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_comment`
--

CREATE TABLE IF NOT EXISTS `duomi_comment` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uid` mediumint(8) unsigned NOT NULL DEFAULT '0',
  `v_id` mediumint(8) unsigned NOT NULL DEFAULT '0',
  `typeid` smallint(5) unsigned NOT NULL DEFAULT '0',
  `username` char(20) NOT NULL DEFAULT '',
  `ip` char(15) NOT NULL DEFAULT '',
  `ischeck` smallint(6) NOT NULL DEFAULT '0',
  `dtime` int(10) unsigned NOT NULL DEFAULT '0',
  `msg` text,
  `m_type` int(6) unsigned NOT NULL DEFAULT '0',
  `reply` int(6) unsigned NOT NULL DEFAULT '0',
  `agree` int(6) unsigned NOT NULL DEFAULT '0',
  `anti` int(6) unsigned NOT NULL DEFAULT '0',
  `pic` char(255) NOT NULL DEFAULT '',
  `vote` int(6) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `v_id` (`v_id`,`ischeck`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_content`
--

CREATE TABLE IF NOT EXISTS `duomi_content` (
  `v_id` mediumint(8) NOT NULL DEFAULT '0',
  `tid` smallint(8) unsigned NOT NULL DEFAULT '0',
  `body` mediumtext,
  PRIMARY KEY (`v_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_count`
--

CREATE TABLE IF NOT EXISTS `duomi_count` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userip` varchar(16) DEFAULT NULL,
  `serverurl` varchar(255) DEFAULT NULL,
  `updatetime` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_co_cls`
--

CREATE TABLE IF NOT EXISTS `duomi_co_cls` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `clsname` varchar(50) NOT NULL DEFAULT '',
  `sysclsid` smallint(5) unsigned NOT NULL DEFAULT '0',
  `cotype` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `sysclsid` (`sysclsid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=9 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_co_config`
--

CREATE TABLE IF NOT EXISTS `duomi_co_config` (
  `cid` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `cname` varchar(50) NOT NULL DEFAULT '',
  `getlistnum` int(10) NOT NULL DEFAULT '0',
  `getconnum` int(10) NOT NULL DEFAULT '0',
  `cotype` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`cid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_co_data`
--

CREATE TABLE IF NOT EXISTS `duomi_co_data` (
  `v_id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `tid` smallint(8) unsigned NOT NULL DEFAULT '0',
  `tname` char(60) NOT NULL DEFAULT '',
  `v_name` char(60) NOT NULL DEFAULT '',
  `v_state` int(10) unsigned NOT NULL DEFAULT '0',
  `v_pic` char(100) NOT NULL DEFAULT '',
  `v_hit` mediumint(8) unsigned NOT NULL DEFAULT '0',
  `v_money` smallint(6) NOT NULL DEFAULT '0',
  `v_rank` smallint(6) NOT NULL DEFAULT '0',
  `v_digg` smallint(6) NOT NULL DEFAULT '0',
  `v_tread` smallint(6) NOT NULL DEFAULT '0',
  `v_commend` smallint(6) NOT NULL DEFAULT '0',
  `v_wrong` smallint(8) unsigned NOT NULL DEFAULT '0',
  `v_director` varchar(200) NOT NULL DEFAULT '',
  `v_enname` varchar(200) NOT NULL DEFAULT '',
  `v_lang` varchar(200) NOT NULL DEFAULT '',
  `v_actor` varchar(200) NOT NULL DEFAULT '',
  `v_color` char(7) NOT NULL DEFAULT '',
  `v_publishyear` char(20) NOT NULL DEFAULT '0',
  `v_publisharea` char(20) NOT NULL DEFAULT '',
  `v_addtime` int(10) unsigned NOT NULL DEFAULT '0',
  `v_topic` mediumint(8) unsigned NOT NULL DEFAULT '0',
  `v_note` char(30) NOT NULL DEFAULT '',
  `v_tags` char(30) NOT NULL DEFAULT '',
  `v_letter` char(3) NOT NULL DEFAULT '',
  `v_from` char(255) NOT NULL DEFAULT '',
  `v_inbase` enum('0','1') NOT NULL DEFAULT '0',
  `v_des` text,
  `v_playdata` text,
  `v_downdata` text,
  PRIMARY KEY (`v_id`),
  KEY `tid` (`v_rank`,`tid`,`v_commend`,`v_hit`),
  KEY `v_addtime` (`v_addtime`,`v_digg`,`v_tread`,`v_inbase`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_co_filters`
--

CREATE TABLE IF NOT EXISTS `duomi_co_filters` (
  `ID` mediumint(8) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `rColumn` tinyint(1) NOT NULL,
  `uesMode` tinyint(1) NOT NULL,
  `sFind` varchar(255) NOT NULL,
  `sStart` varchar(255) NOT NULL,
  `sEnd` varchar(255) NOT NULL,
  `sReplace` varchar(255) NOT NULL,
  `Flag` tinyint(1) NOT NULL,
  `cotype` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_co_news`
--

CREATE TABLE IF NOT EXISTS `duomi_co_news` (
  `n_id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `tid` smallint(8) unsigned NOT NULL DEFAULT '0',
  `n_title` char(60) NOT NULL DEFAULT '',
  `n_keyword` varchar(80) DEFAULT NULL,
  `n_pic` char(255) NOT NULL DEFAULT '',
  `n_hit` mediumint(8) unsigned NOT NULL DEFAULT '0',
  `n_author` varchar(80) DEFAULT NULL,
  `n_addtime` int(10) NOT NULL DEFAULT '0',
  `n_letter` char(3) NOT NULL DEFAULT '',
  `n_content` mediumtext,
  `n_outline` char(255) DEFAULT NULL,
  `tname` char(60) NOT NULL DEFAULT '',
  `n_from` char(50) NOT NULL DEFAULT '',
  `n_inbase` enum('0','1') NOT NULL DEFAULT '0',
  `n_entitle` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`n_id`),
  KEY `tid` (`tid`,`n_hit`),
  KEY `v_addtime` (`n_inbase`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_co_type`
--

CREATE TABLE IF NOT EXISTS `duomi_co_type` (
  `tid` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `cid` smallint(5) unsigned NOT NULL DEFAULT '0',
  `tname` varchar(50) NOT NULL DEFAULT '',
  `siteurl` char(200) NOT NULL DEFAULT '',
  `getherday` smallint(5) unsigned NOT NULL DEFAULT '0',
  `playfrom` varchar(50) NOT NULL DEFAULT '',
  `autocls` enum('0','1') NOT NULL DEFAULT '0',
  `classid` smallint(5) unsigned NOT NULL DEFAULT '0',
  `coding` varchar(10) NOT NULL DEFAULT 'gb2312',
  `sock` enum('0','1') NOT NULL DEFAULT '0',
  `addtime` int(10) unsigned NOT NULL DEFAULT '0',
  `cjtime` int(10) unsigned NOT NULL DEFAULT '0',
  `listconfig` text,
  `itemconfig` text,
  `isok` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `cotype` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tid`),
  KEY `cid` (`cid`,`classid`),
  KEY `addtime` (`addtime`,`cjtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_co_url`
--

CREATE TABLE IF NOT EXISTS `duomi_co_url` (
  `uid` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `cid` smallint(5) unsigned NOT NULL DEFAULT '0',
  `tid` smallint(5) unsigned NOT NULL DEFAULT '0',
  `url` char(255) NOT NULL DEFAULT '',
  `pic` char(255) NOT NULL DEFAULT '',
  `succ` enum('0','1') NOT NULL DEFAULT '0',
  `err` int(5) NOT NULL DEFAULT '0',
  `cotype` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`uid`),
  KEY `cid` (`cid`,`tid`),
  KEY `succ` (`succ`,`err`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_crons`
--

CREATE TABLE IF NOT EXISTS `duomi_crons` (
  `cronid` smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  `available` tinyint(1) NOT NULL DEFAULT '0',
  `type` enum('user','system') NOT NULL DEFAULT 'user',
  `name` char(50) NOT NULL DEFAULT '',
  `filename` char(255) NOT NULL DEFAULT '',
  `lastrun` int(10) unsigned NOT NULL DEFAULT '0',
  `nextrun` int(10) unsigned NOT NULL DEFAULT '0',
  `weekday` tinyint(1) NOT NULL DEFAULT '0',
  `day` tinyint(2) NOT NULL DEFAULT '0',
  `hour` tinyint(2) NOT NULL DEFAULT '0',
  `minute` char(36) NOT NULL DEFAULT '',
  PRIMARY KEY (`cronid`),
  KEY `nextrun` (`available`,`nextrun`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_data`
--

CREATE TABLE IF NOT EXISTS `duomi_data` (
  `v_id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `tid` smallint(8) unsigned NOT NULL DEFAULT '0',
  `v_name` varchar(40) NOT NULL DEFAULT '',
  `v_state` int(10) unsigned NOT NULL DEFAULT '0',
  `v_pic` varchar(80) NOT NULL DEFAULT '',
  `v_hit` mediumint(8) unsigned NOT NULL DEFAULT '0',
  `v_money` smallint(6) NOT NULL DEFAULT '0',
  `v_rank` smallint(6) NOT NULL DEFAULT '0',
  `v_digg` smallint(6) NOT NULL DEFAULT '0',
  `v_tread` smallint(6) NOT NULL DEFAULT '0',
  `v_commend` smallint(6) NOT NULL DEFAULT '0',
  `v_wrong` smallint(8) unsigned NOT NULL DEFAULT '0',
  `v_ismake` smallint(1) unsigned NOT NULL DEFAULT '0',
  `v_actor` varchar(200) DEFAULT NULL,
  `v_color` char(7) NOT NULL DEFAULT '',
  `v_publishyear` char(20) NOT NULL DEFAULT '0',
  `v_publisharea` char(20) NOT NULL DEFAULT '',
  `v_addtime` int(10) unsigned NOT NULL DEFAULT '0',
  `v_topic` mediumint(8) unsigned NOT NULL DEFAULT '0',
  `v_note` char(30) NOT NULL DEFAULT '',
  `v_tags` char(30) NOT NULL DEFAULT '',
  `v_letter` char(3) NOT NULL DEFAULT '',
  `v_isunion` smallint(6) NOT NULL DEFAULT '0',
  `v_recycled` smallint(6) NOT NULL DEFAULT '0',
  `v_director` varchar(200) DEFAULT NULL,
  `v_enname` varchar(200) DEFAULT NULL,
  `v_lang` varchar(200) DEFAULT NULL,
  `v_score` bigint(10) DEFAULT '0',
  `v_scorenum` int(10) DEFAULT '0',
  `v_extratype` text,
  `v_jq` text,
  `v_nickname` char(60) DEFAULT NULL,
  `v_reweek` char(60) DEFAULT NULL,
  `v_douban` varchar(3) DEFAULT NULL,
  `v_mtime` varchar(3) DEFAULT NULL,
  `v_imdb` varchar(3) DEFAULT NULL,
  `v_tvs` char(60) DEFAULT NULL,
  `v_company` char(60) DEFAULT NULL,
  `v_dayhit` int(10) DEFAULT NULL,
  `v_weekhit` int(10) DEFAULT NULL,
  `v_monthhit` int(10) DEFAULT NULL,
  `v_daytime` int(10) DEFAULT NULL,
  `v_weektime` int(10) DEFAULT NULL,
  `v_monthtime` int(10) DEFAULT NULL,
  `v_len` varchar(6) DEFAULT NULL,
  `v_total` varchar(6) DEFAULT NULL,
  `v_ver` varchar(20) DEFAULT NULL,
  `v_origin` varchar(10) DEFAULT '',
  `p_id` varchar(32) NOT NULL,
  PRIMARY KEY (`v_id`),
  UNIQUE KEY `pic_unique` (`p_id`),
  KEY `idx_tid` (`tid`,`v_recycled`,`v_addtime`),
  KEY `idx_addtime` (`v_addtime`),
  KEY `idx_name` (`v_name`,`tid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=31187 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_erradd`
--

CREATE TABLE IF NOT EXISTS `duomi_erradd` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `vid` mediumint(8) unsigned NOT NULL,
  `author` char(60) NOT NULL DEFAULT '',
  `ip` char(15) NOT NULL DEFAULT '',
  `errtxt` mediumtext,
  `sendtime` int(10) unsigned NOT NULL DEFAULT '0',
  KEY `id` (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_favorite`
--

CREATE TABLE IF NOT EXISTS `duomi_favorite` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL DEFAULT '0',
  `vid` int(11) NOT NULL DEFAULT '0',
  `kptime` int(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_flink`
--

CREATE TABLE IF NOT EXISTS `duomi_flink` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `sortrank` smallint(6) NOT NULL DEFAULT '0',
  `url` char(60) NOT NULL DEFAULT '',
  `webname` char(30) NOT NULL DEFAULT '',
  `msg` char(200) NOT NULL DEFAULT '',
  `email` char(50) NOT NULL DEFAULT '',
  `logo` char(60) NOT NULL DEFAULT '',
  `dtime` int(10) unsigned NOT NULL DEFAULT '0',
  `ischeck` smallint(6) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_guestbook`
--

CREATE TABLE IF NOT EXISTS `duomi_guestbook` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `uid` mediumint(8) unsigned NOT NULL DEFAULT '0',
  `title` varchar(60) NOT NULL DEFAULT '',
  `mid` mediumint(8) unsigned DEFAULT '0',
  `posttime` int(10) unsigned NOT NULL DEFAULT '0',
  `uname` varchar(30) NOT NULL DEFAULT '',
  `ip` varchar(20) NOT NULL DEFAULT '',
  `dtime` int(10) unsigned NOT NULL DEFAULT '0',
  `ischeck` smallint(6) NOT NULL DEFAULT '1',
  `msg` text,
  PRIMARY KEY (`id`),
  KEY `ischeck` (`ischeck`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_jqtype`
--

CREATE TABLE IF NOT EXISTS `duomi_jqtype` (
  `tid` smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  `tname` char(30) NOT NULL DEFAULT '',
  `ishidden` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_member`
--

CREATE TABLE IF NOT EXISTS `duomi_member` (
  `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL DEFAULT '',
  `nickname` varchar(20) NOT NULL DEFAULT '',
  `password` varchar(32) NOT NULL DEFAULT '',
  `email` char(255) NOT NULL DEFAULT '',
  `logintime` int(10) NOT NULL DEFAULT '0',
  `logingip` varchar(16) NOT NULL DEFAULT '',
  `regtime` int(10) NOT NULL DEFAULT '0',
  `gid` smallint(4) NOT NULL,
  `points` int(10) NOT NULL DEFAULT '0',
  `state` smallint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_member_group`
--

CREATE TABLE IF NOT EXISTS `duomi_member_group` (
  `gid` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `gname` varchar(32) NOT NULL DEFAULT '',
  `gtype` varchar(255) NOT NULL DEFAULT '',
  `g_auth` varchar(32) NOT NULL DEFAULT '',
  `g_upgrade` int(11) NOT NULL DEFAULT '0',
  `g_authvalue` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`gid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_myad`
--

CREATE TABLE IF NOT EXISTS `duomi_myad` (
  `aid` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `adname` varchar(100) NOT NULL DEFAULT '',
  `adenname` varchar(60) NOT NULL DEFAULT '',
  `timeset` int(10) unsigned NOT NULL DEFAULT '0',
  `intro` char(255) NOT NULL DEFAULT '',
  `adsbody` text,
  PRIMARY KEY (`aid`),
  KEY `timeset` (`timeset`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_mytag`
--

CREATE TABLE IF NOT EXISTS `duomi_mytag` (
  `aid` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `tagname` varchar(30) NOT NULL DEFAULT '',
  `tagdes` varchar(50) NOT NULL DEFAULT '0',
  `addtime` int(10) unsigned NOT NULL DEFAULT '0',
  `tagcontent` text,
  PRIMARY KEY (`aid`),
  KEY `tagname` (`tagname`,`addtime`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_news`
--

CREATE TABLE IF NOT EXISTS `duomi_news` (
  `n_id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `tid` smallint(8) unsigned NOT NULL DEFAULT '0',
  `n_title` char(60) NOT NULL DEFAULT '',
  `n_pic` char(100) NOT NULL DEFAULT '',
  `n_hit` mediumint(8) unsigned NOT NULL DEFAULT '0',
  `n_money` smallint(6) NOT NULL DEFAULT '0',
  `n_rank` smallint(6) NOT NULL DEFAULT '0',
  `n_digg` smallint(6) NOT NULL DEFAULT '0',
  `n_tread` smallint(6) NOT NULL DEFAULT '0',
  `n_commend` smallint(6) NOT NULL DEFAULT '0',
  `n_author` varchar(80) DEFAULT NULL,
  `n_color` char(7) NOT NULL DEFAULT '',
  `n_addtime` int(10) unsigned NOT NULL DEFAULT '0',
  `n_note` smallint(6) NOT NULL DEFAULT '0',
  `n_letter` char(3) NOT NULL DEFAULT '',
  `n_isunion` smallint(6) NOT NULL DEFAULT '0',
  `n_recycled` smallint(6) NOT NULL DEFAULT '0',
  `n_entitle` varchar(200) DEFAULT NULL,
  `n_outline` varchar(255) DEFAULT NULL,
  `n_keyword` varchar(80) DEFAULT NULL,
  `n_from` varchar(50) DEFAULT NULL,
  `n_score` bigint(10) DEFAULT '0',
  `n_scorenum` int(10) DEFAULT '0',
  `n_content` mediumtext,
  PRIMARY KEY (`n_id`),
  KEY `tid` (`n_rank`,`tid`,`n_commend`,`n_hit`),
  KEY `v_addtime` (`n_addtime`,`n_digg`,`n_tread`,`n_isunion`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_playdata`
--

CREATE TABLE IF NOT EXISTS `duomi_playdata` (
  `v_id` mediumint(8) NOT NULL DEFAULT '0',
  `tid` smallint(8) unsigned NOT NULL DEFAULT '0',
  `body` mediumtext,
  `body1` mediumtext,
  PRIMARY KEY (`v_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_search_keywords`
--

CREATE TABLE IF NOT EXISTS `duomi_search_keywords` (
  `aid` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `keyword` char(30) NOT NULL DEFAULT '',
  `spwords` char(50) NOT NULL DEFAULT '',
  `count` mediumint(8) unsigned NOT NULL DEFAULT '1',
  `result` mediumint(8) unsigned NOT NULL DEFAULT '0',
  `lasttime` int(10) unsigned NOT NULL DEFAULT '0',
  `tid` smallint(5) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`aid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_slide`
--

CREATE TABLE IF NOT EXISTS `duomi_slide` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `sortrank` smallint(6) NOT NULL DEFAULT '0',
  `url` char(60) NOT NULL DEFAULT '',
  `webname` char(30) NOT NULL DEFAULT '',
  `msg` char(200) NOT NULL DEFAULT '',
  `email` char(50) NOT NULL DEFAULT '',
  `v_pic` char(60) NOT NULL DEFAULT '',
  `dtime` int(10) unsigned NOT NULL DEFAULT '0',
  `ischeck` smallint(6) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_tags`
--

CREATE TABLE IF NOT EXISTS `duomi_tags` (
  `tagid` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `tag` char(30) NOT NULL DEFAULT '',
  `usenum` mediumint(6) unsigned NOT NULL DEFAULT '0',
  `vids` text NOT NULL,
  PRIMARY KEY (`tagid`),
  KEY `usenum` (`usenum`),
  KEY `tag` (`tag`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_temp`
--

CREATE TABLE IF NOT EXISTS `duomi_temp` (
  `v_id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `tid` smallint(8) unsigned NOT NULL DEFAULT '0',
  `v_name` char(60) NOT NULL DEFAULT '',
  `v_state` int(10) unsigned NOT NULL DEFAULT '0',
  `v_pic` char(100) NOT NULL DEFAULT '',
  `v_actor` varchar(200) DEFAULT NULL,
  `v_publishyear` char(20) NOT NULL DEFAULT '0',
  `v_publisharea` char(20) NOT NULL DEFAULT '',
  `v_addtime` int(10) unsigned NOT NULL DEFAULT '0',
  `v_note` char(30) NOT NULL DEFAULT '',
  `v_letter` char(3) NOT NULL DEFAULT '',
  `v_playdata` mediumtext,
  `v_des` mediumtext,
  `v_director` varchar(200) DEFAULT NULL,
  `v_enname` varchar(200) DEFAULT NULL,
  `v_lang` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`v_id`),
  KEY `tid` (`tid`),
  KEY `v_addtime` (`v_addtime`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_topic`
--

CREATE TABLE IF NOT EXISTS `duomi_topic` (
  `id` smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` char(30) NOT NULL DEFAULT '',
  `enname` char(60) NOT NULL DEFAULT '',
  `sort` int(11) NOT NULL DEFAULT '0',
  `template` char(50) NOT NULL DEFAULT '',
  `pic` char(80) NOT NULL DEFAULT '',
  `des` text,
  `vod` text NOT NULL,
  `keyword` text,
  PRIMARY KEY (`id`),
  KEY `sort` (`sort`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_type`
--

CREATE TABLE IF NOT EXISTS `duomi_type` (
  `tid` smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  `upid` tinyint(6) unsigned NOT NULL DEFAULT '0',
  `tname` char(30) NOT NULL DEFAULT '',
  `tenname` char(60) NOT NULL DEFAULT '',
  `torder` int(11) NOT NULL DEFAULT '0',
  `templist` char(50) NOT NULL DEFAULT '',
  `templist_1` char(50) NOT NULL DEFAULT '',
  `title` char(50) NOT NULL DEFAULT '',
  `keyword` char(50) NOT NULL DEFAULT '',
  `description` char(50) NOT NULL DEFAULT '',
  `ishidden` smallint(6) NOT NULL DEFAULT '0',
  `unionid` mediumtext,
  `tptype` smallint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tid`),
  KEY `upid` (`upid`,`ishidden`),
  KEY `torder` (`torder`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=18 ;

-- --------------------------------------------------------

--
-- 表的结构 `duomi_zyk`
--

CREATE TABLE IF NOT EXISTS `duomi_zyk` (
  `zid` int(6) NOT NULL AUTO_INCREMENT,
  `zname` varchar(60) NOT NULL,
  `zapi` varchar(255) NOT NULL,
  `zinfo` varchar(255) NOT NULL DEFAULT '暂无',
  PRIMARY KEY (`zid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `ly_admin_access`
--

CREATE TABLE IF NOT EXISTS `ly_admin_access` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '管理员ID',
  `uid` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '用户ID',
  `group` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '管理员用户组',
  `create_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',
  `sort` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '排序',
  `status` tinyint(3) NOT NULL DEFAULT '0' COMMENT '状态',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='后台管理员与用户组对应关系表' AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- 表的结构 `ly_admin_addon`
--

CREATE TABLE IF NOT EXISTS `ly_admin_addon` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(32) DEFAULT NULL COMMENT '插件名或标识',
  `title` varchar(32) NOT NULL DEFAULT '' COMMENT '中文名',
  `description` text NOT NULL COMMENT '插件描述',
  `logo` varchar(63) NOT NULL DEFAULT '' COMMENT '图片图标',
  `icon` varchar(31) NOT NULL DEFAULT '' COMMENT '图标',
  `icon_color` varchar(7) NOT NULL DEFAULT '' COMMENT '图标颜色',
  `config` text COMMENT '配置',
  `author` varchar(32) NOT NULL DEFAULT '' COMMENT '作者',
  `version` varchar(8) NOT NULL DEFAULT '' COMMENT '版本号',
  `adminlist` tinyint(4) unsigned NOT NULL DEFAULT '0' COMMENT '是否有后台列表',
  `type` tinyint(4) unsigned NOT NULL DEFAULT '0' COMMENT '插件类型',
  `create_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '安装时间',
  `update_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '修改时间',
  `sort` tinyint(4) unsigned NOT NULL DEFAULT '0' COMMENT '排序',
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '状态',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='插件表' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `ly_admin_config`
--

CREATE TABLE IF NOT EXISTS `ly_admin_config` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '配置ID',
  `title` varchar(32) NOT NULL DEFAULT '' COMMENT '配置标题',
  `name` varchar(32) DEFAULT NULL COMMENT '配置名称',
  `value` text NOT NULL COMMENT '配置值',
  `group` tinyint(4) unsigned NOT NULL DEFAULT '0' COMMENT '配置分组',
  `type` varchar(16) NOT NULL DEFAULT '' COMMENT '配置类型',
  `options` varchar(255) NOT NULL DEFAULT '' COMMENT '配置额外值',
  `tip` varchar(100) NOT NULL DEFAULT '' COMMENT '配置说明',
  `is_dev` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否开发模式才显示',
  `is_system` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否系统配置',
  `create_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',
  `sort` tinyint(4) unsigned NOT NULL DEFAULT '0' COMMENT '排序',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '状态',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='系统配置表' AUTO_INCREMENT=45 ;

-- --------------------------------------------------------

--
-- 表的结构 `ly_admin_group`
--

CREATE TABLE IF NOT EXISTS `ly_admin_group` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '部门ID',
  `pid` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '上级部门ID',
  `title` varchar(31) NOT NULL DEFAULT '' COMMENT '部门名称',
  `icon` varchar(31) NOT NULL DEFAULT '' COMMENT '图标',
  `menu_auth` text NOT NULL COMMENT '权限列表',
  `create_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '修改时间',
  `sort` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '排序（同级有效）',
  `status` tinyint(3) NOT NULL DEFAULT '0' COMMENT '状态',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='部门信息表' AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- 表的结构 `ly_admin_hook`
--

CREATE TABLE IF NOT EXISTS `ly_admin_hook` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '钩子ID',
  `name` varchar(32) DEFAULT NULL COMMENT '钩子名称',
  `description` text NOT NULL COMMENT '描述',
  `addons` varchar(255) NOT NULL DEFAULT '' COMMENT '钩子挂载的插件',
  `type` tinyint(4) unsigned NOT NULL DEFAULT '1' COMMENT '类型',
  `create_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '状态',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='钩子表' AUTO_INCREMENT=7 ;

-- --------------------------------------------------------

--
-- 表的结构 `ly_admin_module`
--

CREATE TABLE IF NOT EXISTS `ly_admin_module` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `name` varchar(31) DEFAULT NULL COMMENT '名称',
  `title` varchar(63) NOT NULL DEFAULT '' COMMENT '标题',
  `logo` varchar(63) NOT NULL DEFAULT '' COMMENT '图片图标',
  `icon` varchar(31) NOT NULL DEFAULT '' COMMENT '字体图标',
  `icon_color` varchar(7) NOT NULL DEFAULT '' COMMENT '字体图标颜色',
  `description` varchar(127) NOT NULL DEFAULT '' COMMENT '描述',
  `developer` varchar(31) NOT NULL DEFAULT '' COMMENT '开发者',
  `version` varchar(7) NOT NULL DEFAULT '' COMMENT '版本',
  `user_nav` text NOT NULL COMMENT '个人中心导航',
  `home_nav` text COMMENT '个人主页导航',
  `config` text NOT NULL COMMENT '配置',
  `admin_menu` text NOT NULL COMMENT '菜单节点',
  `router` text COMMENT '路由规则',
  `is_system` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否允许卸载',
  `create_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',
  `sort` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '排序',
  `status` tinyint(3) NOT NULL DEFAULT '0' COMMENT '状态',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='模块功能表' AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- 表的结构 `ly_admin_nav`
--

CREATE TABLE IF NOT EXISTS `ly_admin_nav` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `group` varchar(11) NOT NULL DEFAULT '' COMMENT '分组',
  `pid` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '父ID',
  `title` varchar(31) NOT NULL DEFAULT '' COMMENT '导航标题',
  `type` varchar(15) NOT NULL DEFAULT '' COMMENT '导航类型',
  `value` text COMMENT '导航值',
  `api_route` varchar(255) NOT NULL DEFAULT '' COMMENT 'API路由',
  `target` varchar(11) NOT NULL DEFAULT '' COMMENT '打开方式',
  `icon` varchar(32) NOT NULL DEFAULT '' COMMENT '图标',
  `cover` varchar(255) NOT NULL DEFAULT '' COMMENT '封面图标',
  `lists_template` varchar(63) NOT NULL DEFAULT '' COMMENT '列表页模板',
  `detail_template` varchar(63) NOT NULL DEFAULT '' COMMENT '详情页模板',
  `create_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '修改时间',
  `sort` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '排序',
  `status` tinyint(3) NOT NULL DEFAULT '0' COMMENT '状态',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='前台导航表' AUTO_INCREMENT=19 ;

-- --------------------------------------------------------

--
-- 表的结构 `ly_admin_post`
--

CREATE TABLE IF NOT EXISTS `ly_admin_post` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `cid` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '分类ID',
  `title` varchar(127) NOT NULL DEFAULT '' COMMENT '标题',
  `cover` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '封面',
  `abstract` varchar(255) DEFAULT '' COMMENT '摘要',
  `content` text COMMENT '内容',
  `view_count` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '阅读',
  `create_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '修改时间',
  `sort` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '排序',
  `status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '状态',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文章列表' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `ly_admin_upload`
--

CREATE TABLE IF NOT EXISTS `ly_admin_upload` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `uid` int(11) unsigned NOT NULL DEFAULT '0' COMMENT 'UID',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '文件名',
  `path` varchar(255) NOT NULL DEFAULT '' COMMENT '文件路径',
  `url` varchar(255) DEFAULT '' COMMENT '文件链接',
  `ext` char(4) NOT NULL DEFAULT '' COMMENT '文件类型',
  `size` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '文件大小',
  `md5` char(32) DEFAULT '' COMMENT '文件md5',
  `sha1` char(40) DEFAULT '' COMMENT '文件sha1编码',
  `location` varchar(15) NOT NULL DEFAULT '' COMMENT '文件存储位置',
  `download` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '下载次数',
  `create_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '上传时间',
  `update_time` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '修改时间',
  `sort` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '排序',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '状态',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文件上传表' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `ordertable`
--

CREATE TABLE IF NOT EXISTS `ordertable` (
  `idOrder` int(11) NOT NULL AUTO_INCREMENT COMMENT '订单id',
  `Ordercommodity` varchar(45) DEFAULT NULL COMMENT '订单的商品',
  `commodityPrice` double DEFAULT NULL COMMENT '订单价格，不包含运费',
  `Orderpostage` double DEFAULT NULL COMMENT '订单邮费',
  `Commoditycolor` varchar(45) DEFAULT NULL COMMENT '商品颜色',
  `seller` varchar(45) DEFAULT NULL COMMENT '卖家',
  `Buyer` varchar(45) DEFAULT NULL COMMENT '买家',
  `Commoditystate` int(2) DEFAULT NULL COMMENT '商品状态，1表示未发货，2表示已发货等待签收，3表示已签收等待确认，4代表已签收已确认交易成功,5已签收正在退货，6买家卖家确认退款金额，7等待邮寄退回卖家，8退款邮寄中，9卖家收货确认，10退回金额',
  PRIMARY KEY (`idOrder`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `table_user`
--

CREATE TABLE IF NOT EXISTS `table_user` (
  `userid` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `userphone` varchar(45) NOT NULL COMMENT '用户手机号',
  `useremaile` varchar(45) DEFAULT NULL COMMENT '用户邮箱',
  `username` varchar(45) DEFAULT NULL COMMENT '用户昵称',
  `useraddress` varchar(45) DEFAULT NULL COMMENT '用户地址',
  `usersex` varchar(45) DEFAULT '3' COMMENT '用户性别，1是男生，2是女生，3是未知',
  `userBirthday` datetime DEFAULT NULL COMMENT '用户生日',
  `userremind` varchar(45) DEFAULT NULL COMMENT '设置提醒的商品，买卖开始提醒我',
  `userBeingauctioned` varchar(45) DEFAULT NULL COMMENT '已参加拍卖的商品id',
  `usercreditmoney` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
