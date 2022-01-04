CREATE DATABASE IF NOT EXISTS `datarepresentation` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `datarepresentation`;

CREATE TABLE IF NOT EXISTS `loginprofile` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`username` varchar(50) NOT NULL,
`password` varchar(255) NOT NULL,
`email` varchar(100) NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `films` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`movie_name` varchar(50) NOT NULL,
`movie_gender` varchar(255) NOT NULL,
`movie_year` int(4) NOT NULL,
`movie_box_office` decimal(10,2) NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;