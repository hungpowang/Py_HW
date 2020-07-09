# 刪除資料庫(如果存在)
DROP DATABASE IF EXISTS MemberSys;

# 創建資料庫
create database MemberSys;

# 檢視資料庫資訊
use MemberSys;

# 建立資料表 members
create table members(
 id int AUTO_INCREMENT PRIMARY KEY, 
 name varchar(50),
 birthday date,
 address varchar(200)
);

# 新增資料 (insert into)
insert into members(name, birthday, address) values('John', '1990-01-31', 'Chiayi');
insert into members(name, birthday, address) values('Mary', '2013-05-17', 'Tainan');
insert into members(name, birthday, address) values('Brad', '1998-12-26', 'Chiayi');
# 不用寫明Column Name 也可新增資料
insert into members values(4, 'Hanry', '2017-08-30', 'Taipei');
insert into members values(5, 'Cindy', '2801-11-12', 'Tainan');
insert into members values(6, 'Larry', '2749-04-18', 'Taipei');

# 修改資料
UPDATE `members` SET `birthday`='2819-03-16',`name`='Michael' WHERE `id`=3;

# 刪除資料
DELETE FROM `members` WHERE `id`>=5;

# 查詢資料
SELECT * FROM `members` WHERE `name` LIKE '%hael';
SELECT * FROM `members`;
