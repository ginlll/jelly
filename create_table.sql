create table tbl_match (
   level_id INT NOT NULL AUTO_INCREMENT,
   session_id VARCHAR(64) NOT NULL,
   start_grid VARCHAR(64) NOT NULL,
   corrent_grid VARCHAR(64) NOT NULL,
   PRIMARY KEY ( level_id ),
   UNIQUE KEY ( session_id )
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
