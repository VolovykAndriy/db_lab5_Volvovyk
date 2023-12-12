CREATE TABLE Platform
(
  platform_id INT NOT NULL,
  Platform_Name VARCHAR(50) NOT NULL,
  PRIMARY KEY (platform_id)
);

CREATE TABLE Publisher
(
  publisher_id INT NOT NULL,
  Publisher_Name VARCHAR(200) NOT NULL,
  PRIMARY KEY (publisher_id)
);

CREATE TABLE global_sales
(
  gs_id INT NOT NULL,
  sales FLOAT NOT NULL,
  year_of_update INT NOT NULL,
  PRIMARY KEY (gs_id)
);

CREATE TABLE Game
(
  game_id INT NOT NULL,
  Name VARCHAR(100) NOT NULL,
  Year INT NOT NULL,
  Genre VARCHAR(50) NOT NULL,
  platform_id INT NOT NULL,
  publisher_id INT NOT NULL,
  gs_id INT NOT NULL,  
  PRIMARY KEY (game_id),
  FOREIGN KEY (platform_id) REFERENCES Platform(platform_id),
  FOREIGN KEY (publisher_id) REFERENCES Publisher(publisher_id),
  FOREIGN KEY (gs_id) REFERENCES global_sales(gs_id)  
);

CREATE TABLE Platform_has_game
(
  game_id INT NOT NULL,
  platform_id INT NOT NULL,
  PRIMARY KEY (game_id, platform_id),
  FOREIGN KEY (game_id) REFERENCES Game(game_id),
  FOREIGN KEY (platform_id) REFERENCES Platform(platform_id)
);
