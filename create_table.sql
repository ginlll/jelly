drop database if exists test;
create database test;
use test;
drop table if exists tbl_level;
drop table if exists tbl_match;
create table tbl_level (
   level_id INT NOT NULL,
   start_grid VARCHAR(64) NOT NULL,
   PRIMARY KEY ( level_id )
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
create table tbl_match (
   id INT NOT NULL AUTO_INCREMENT,
   level_id INT NOT NULL,
   session_id VARCHAR(64) NOT NULL,
   current_grid VARCHAR(64) NOT NULL,
   PRIMARY KEY ( id ),
   UNIQUE KEY ( session_id )
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
