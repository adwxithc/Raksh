/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.5.20-log : Database - als
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`als` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `als`;

/*Table structure for table `ambulance` */

DROP TABLE IF EXISTS `ambulance`;

CREATE TABLE `ambulance` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `Anumber` varchar(90) NOT NULL,
  `dname` varchar(90) NOT NULL,
  `phone` bigint(11) NOT NULL,
  `email` varchar(90) NOT NULL,
  `place` varchar(90) NOT NULL,
  `status` varchar(90) NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `ambulance` */

insert  into `ambulance`(`aid`,`lid`,`Anumber`,`dname`,`phone`,`email`,`place`,`status`) values (1,10,'KL13AQ7375','Swathin KTK',7994546435,'adwaithjanardhanan0@gmail.com','Thalassery ','active');

/*Table structure for table `emergency_no` */

DROP TABLE IF EXISTS `emergency_no`;

CREATE TABLE `emergency_no` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `number` bigint(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `emergency_no` */

insert  into `emergency_no`(`id`,`uid`,`number`) values (5,7,8136841963),(6,8,9446289847),(7,7,9037365996),(8,7,7902248441);

/*Table structure for table `hos_notification` */

DROP TABLE IF EXISTS `hos_notification`;

CREATE TABLE `hos_notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aid` int(90) NOT NULL,
  `hid` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `notificatin` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `hos_notification` */

insert  into `hos_notification`(`id`,`aid`,`hid`,`date`,`time`,`notificatin`) values (1,7,0,'2023-04-19','12:14:52','hw'),(2,7,0,'2023-04-19','12:14:52','hw'),(3,7,0,'2023-04-19','12:15:17','humilo'),(4,7,0,'2023-04-19','12:20:25','gkff'),(5,7,0,'2023-04-19','12:20:25','gkff'),(6,7,0,'2023-04-19','12:20:26','gkff');

/*Table structure for table `hospital` */

DROP TABLE IF EXISTS `hospital`;

CREATE TABLE `hospital` (
  `hid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `hname` varchar(90) NOT NULL,
  `place` varchar(90) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `post` varchar(90) DEFAULT NULL,
  `phno` bigint(20) NOT NULL,
  `email` varchar(90) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  PRIMARY KEY (`hid`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

/*Data for the table `hospital` */

insert  into `hospital`(`hid`,`lid`,`hname`,`place`,`pin`,`post`,`phno`,`email`,`latitude`,`longitude`) values (31,2,'GOVT. HOSPITAL KANNUR','THALUK',0,'123456',2147483647,'adwaith@gmail.com',1.90999,2.09),(32,3,'GOVT. HOSPITAL KOZHIKODE','SK NAGAR',0,'766657',2147483647,'maneeshkumar@gmail.com',11.2578,75.7845),(33,4,'GOVT. HOSPITAL TRIVANDRUM','VN NAGAR',0,'670098',9846123465,'jishnuraghavan@gmail.com',2.8922,3.37766),(34,5,'GOVT. HOSPITAL THALASSERY','THALSERRY ',670000,'CORPORATE HOSPITAL',7866787558,'mukundhanunni@gmail.com',11.2577,75.7845),(35,6,'mims','kozhikode',670073,'mankav',9867674534,'mims@gmail.com',11.45,12.45);

/*Table structure for table `hospital_notification` */

DROP TABLE IF EXISTS `hospital_notification`;

CREATE TABLE `hospital_notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aid` int(11) DEFAULT NULL,
  `hid` int(11) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `hospital_notification` */

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aid` int(11) NOT NULL,
  `longitude` varchar(30) DEFAULT NULL,
  `latitude` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`id`,`aid`,`longitude`,`latitude`) values (1,7,'75.78453333333333','11.257791666666666'),(2,10,'75.78454666666667','11.257778333333333');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(90) NOT NULL,
  `password` varchar(90) NOT NULL,
  `type` varchar(90) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values (1,'admin','admin','admin'),(2,'GOVTKANNUR','GOVTKANNUR','hospital'),(3,'123','123','hospital'),(4,'ahospital','ahospital','hospital'),(5,'bhospital','bhospital','hospital'),(6,'chospital','chospital','hospital'),(7,'adw@2002','adw@2002','user'),(10,'Amb1','Amb1','Ambulance');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(90) NOT NULL,
  `date` varchar(50) NOT NULL,
  `time` varchar(50) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`id`,`uid`,`date`,`time`,`latitude`,`longitude`,`status`) values (1,7,'2023-04-19','12:50:48','11.257821666666667','75.78454833333333','pending'),(2,10,'2023-04-19','12:57:43','11.257765','75.78455166666666','pending'),(3,10,'2023-04-19','12:57:43','11.257765','75.78455166666666','pending');

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(500) DEFAULT NULL,
  `amb_id` int(20) DEFAULT NULL,
  `uid` int(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `reply` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `report` */

insert  into `report`(`id`,`message`,`amb_id`,`uid`,`date`,`reply`) values (0,'False ',7,10,'2023-04-19','pending'),(2,'False ',7,10,'2023-04-19','pending'),(3,'5,03',7,10,'2023-04-19','pending'),(4,'5,03',7,10,'2023-04-19','pending'),(5,'5,03',7,10,'2023-04-19','pending'),(6,'5,03',7,10,'2023-04-19','pending'),(7,'5,03',7,10,'2023-04-19','pending'),(8,'5,03',7,10,'2023-04-19','pending'),(9,'5,03',7,10,'2023-04-19','pending'),(10,'5,03',7,10,'2023-04-19','pending'),(11,'5,03',7,10,'2023-04-19','pending'),(12,'5,03',7,10,'2023-04-19','pending'),(13,'5,03',7,10,'2023-04-19','pending'),(14,'5,03',7,10,'2023-04-19','pending'),(15,'5,03',7,10,'2023-04-19','pending'),(16,'5,03',7,10,'2023-04-19','pending'),(17,'5,03',7,10,'2023-04-19','pending'),(18,'5,03',7,10,'2023-04-19','pending'),(19,'hlo',7,10,'2023-04-19','pending'),(20,'hlo',10,7,'2023-04-19','pending');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `aid` int(11) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `status` varchar(90) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(40) NOT NULL,
  KEY `rid` (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`rid`,`uid`,`aid`,`latitude`,`longitude`,`status`,`date`,`time`) values (1,7,10,11.2578,75.7845,'accepted','2023-04-19','17:00:01'),(2,7,0,11.2578,75.7845,'pending','2023-04-19','17:02:05'),(3,7,0,11.2578,75.7846,'pending','2023-04-19','17:25:28'),(4,7,0,11.2578,75.7845,'pending','2023-04-19','17:32:40');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `fname` varchar(90) NOT NULL,
  `lname` varchar(90) NOT NULL,
  `place` varchar(90) DEFAULT NULL,
  `phone` bigint(11) NOT NULL,
  `email` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`uid`,`lid`,`fname`,`lname`,`place`,`phone`,`email`) values (1,7,'Adwaith','JN','Thalassery ',9846125621,'aromalkovilakathuparambil@gmail.com');

/*Table structure for table `workshop/pump` */

DROP TABLE IF EXISTS `workshop/pump`;

CREATE TABLE `workshop/pump` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(90) NOT NULL,
  `place` varchar(90) DEFAULT NULL,
  `phone` bigint(10) DEFAULT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `status` varchar(90) DEFAULT NULL,
  `type` varchar(90) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `workshop/pump` */

insert  into `workshop/pump`(`id`,`name`,`place`,`phone`,`latitude`,`longitude`,`status`,`type`) values (1,'ram','v illage',9457483647,11.2577,75.7845,'active','pump'),(3,'janardhanan paRA','fghjdfgf',6767483647,11.8765,75.3931,'inactive','workshop'),(4,'adwaith','kannur',9147483647,11.2577,75.7845,'active','workshop'),(5,'vishwanath','kozhikode',9878765467,11.875,75.3931,'active','pump');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
