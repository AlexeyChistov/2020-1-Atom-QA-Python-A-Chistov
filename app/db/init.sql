USE `technoatom`;

DROP TABLE IF EXISTS `test_users`;

CREATE TABLE `test_users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(16) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(64) NOT NULL,
  `access` smallint DEFAULT NULL,
  `active` smallint DEFAULT NULL,
  `start_active_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `ix_test_users_username` (`username`)
);

INSERT INTO test_users (username, password, email, access) VALUES ('super_user', 'super_pass', 'superuser@mail.ru', 1);