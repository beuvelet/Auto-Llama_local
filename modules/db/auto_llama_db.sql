CREATE DATABASE IF NOT EXISTS auto_llama_db CHARACTER SET utf8 COLLATE utf8_general_ci;

USE auto_llama_db;

CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `files` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `path` varchar(255) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `files_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `web_searches` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `query` varchar(255) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `web_searches_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `codes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` text NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `codes_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Exemples de données pour la table 'users'
INSERT INTO users (username, email, password) VALUES
('john_doe', 'john@example.com', 'password123'),
('jane_smith', 'jane@example.com', 'abc@123'),
('alice', 'alice@example.com', 'qwerty');

-- Exemples de données pour la table 'projects'
INSERT INTO projects (user_id, name, description) VALUES
(1, 'Project A', 'Description of Project A'),
(2, 'Project B', 'Description of Project B'),
(3, 'Project C', 'Description of Project C');

-- Exemples de données pour la table 'files'
INSERT INTO files (name, path, project_id) VALUES
('File1.txt', '/path/to/File1.txt', 1),
('File2.txt', '/path/to/File2.txt', 1),
('File3.txt', '/path/to/File3.txt', 2);

-- Exemples de données pour la table 'web_searches'
INSERT INTO web_searches (query, project_id) VALUES
('Search term 1', 1),
('Search term 2', 2),
('Search term 3', 3);

-- Exemples de données pour la table 'codes'
INSERT INTO codes (code, project_id) VALUES
('Code snippet 1', 1),
('Code snippet 2', 2),
('Code snippet 3', 3);
