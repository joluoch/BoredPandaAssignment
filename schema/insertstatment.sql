insert into video(idvideo,video_url,video_duration,publish_date) values
(1,'https://www.youtube.com/watch?v=aJlPWbvUBYs&t=467s',45,'2022-1-1'),
(2,'https://www.youtube.com/watch?v=96c-acK67_s',45,'2022-1-2'),
(3,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',40,'2022-1-13'),
(4,'https://www.youtube.com/watch?v=hMXiqeTxb8Y',50,'2022-1-24'),
(5,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',45,'2022-1-30'),
(6,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',40,'2022-2-3'),
(7,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',30,'2022-2-13'),
(8,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',40,'2022-2-23'),
(9,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',53,'2022-2-28'),
(10,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',42,'2022-3-5'),
(11,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',40,'2022-3-15'),
(12,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',43,'2022-3-25'),
(13,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',45,'2022-3-30'),
(14,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',40,'2022-4-2'),
(15,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',48,'2022-4-12'),
(16,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',90,'2022-4-22'),
(17,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',40,'2022-4-28'),
(18,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',45,'2022-4-30'),
(19,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',47,'2022-5-3'),
(20,'https://www.youtube.com/watch?v=7Fi7F2M4KHY',40,'2022-5-13')
;

insert into  category(idcategory,category_name) values (1,'construction'),
(2,'fashion'),
(3,'food'),
(4,'music'),
(5,'art'),
(6,'relationship');
insert into subcategory (idsubcat,subcategory_name,idcategory) values (1,'woodwork',1),
(2,'malewear',2),
(3,'recipe',3),
(4,'hiphop',4),
(5,'streetart',5),
(6,'lgtbq',6),
(7,'welding',1),
(8,'ladieswear',2),
(9,'junkfood',3);

insert into vidcat (idvideo,idsubcat) values 
(1,2),
(1,1),
(1,5),
(2,1),
(2,5),
(2,2),
(3,1),
(3,1),
(3,7),
(4,5),
(4,3),
(4,6),
(5,1),
(5,3),
(5,6),
(5,5),
(5,3),
(5,3),
(6,5),
(7,5),
(7,8),
(8,5),
(9,8),
(9,3),
(10,7),
(10,8),
(11,2),
(11,7),
(11,4),
(12,6),
(12,7),
(13,7),
(14,9),
(14,4),
(15,9),
(16,2),
(17,8),
(18,9),
(19,3),
(20,3)
;

