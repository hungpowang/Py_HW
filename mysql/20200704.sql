SELECT * FROM `member`;
SELECT * FROM `tel`;
SELECT `id`,`tel` FROM `tel` WHERE `id`=13;

# 兩邊都存在時才會被INNER JOIN顯示
SELECT * FROM `member` AS `a` INNER JOIN `tel` as `b` on `a`.`id`=`b`.`member_id`;
SELECT `a`.*,`b`.`tel` FROM `member` AS `a` INNER JOIN `tel` AS `b` on `a`.`id`=`b`.`member_id`;

#
SELECT `a`.*,`b`.`tel` FROM `member` AS `a` LEFT JOIN `tel` AS `b` on `a`.`id`=`b`.`member_id`;

ALTER TABLE `tel` ADD CONSTRAINT `xxx` FOREIGN KEY (`member_id`) REFERENCES `member`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

SELECT CONCAT('[',`create_time`,']',`title`)