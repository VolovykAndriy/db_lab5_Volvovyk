-- Заповнення таблиці Platform
INSERT INTO Platform (platform_id, Platform_Name)
VALUES
  (1, 'Wii'),
  (2, 'NES'),
  (3, 'DS'),
  (4, 'GB'),
  (5, 'X360'),
  (6, 'PS3'),
  (7, 'PS2'),
  (8, 'SNES'),
  (9, 'GBA'),
  (10, 'PS'),
  (11, '3DS'),
  (12, 'N64');

-- Заповнення таблиці Publisher
INSERT INTO Publisher (publisher_id, Publisher_Name)
VALUES
  (1, 'Nintendo'),
  (2, 'Microsoft Game Studios'),
  (3, 'Take-Two Interactive'),
  (4, 'Sony Computer Entertainment'),
  (5, 'Activision');

-- Заповнення таблиці global_sales
INSERT INTO global_sales (gs_id, game_id, sales, year_of_update)
VALUES
  (1, 1, 82.74, 2006),
  (2, 2, 40.24, 1985),
  (3, 3, 35.82, 2008),
  (4, 4, 33, 2009),
  (5, 5, 31.37, 1996),
  (6, 6, 30.26, 1989),
  (7, 7, 30.01, 2006),
  (8, 8, 29.02, 2006),
  (9, 9, 28.62, 2009),
  (10, 10, 28.31, 1984),
  (11, 11, 24.76, 2005),
  (12, 12, 23.42, 2005),
  (13, 13, 23.1, 1999),
  (14, 14, 22.72, 2007),
  (15, 15, 22, 2009);

-- Заповнення таблиці Game
INSERT INTO Game (game_id, Name, Year, Genre, platform_id, publisher_id)
VALUES
  (1, 'Wii Sports', 2006, 'Sports', 1, 1),
  (2, 'Super Mario Bros.', 1985, 'Platform', 2, 1),
  (3, 'Mario Kart Wii', 2008, 'Racing', 1, 1),
  (4, 'Wii Sports Resort', 2009, 'Sports', 1, 1),
  (5, 'Pokemon Red/Pokemon Blue', 1996, 'Role-Playing', 4, 1,),
  (6, 'Tetris', 1989, 'Puzzle', 4, 1),
  (7, 'New Super Mario Bros.', 2006, 'Platform', 3, 1),
  (8, 'Wii Play', 2006, 'Misc', 1, 1, 8),
  (9, 'New Super Mario Bros. Wii', 2009, 'Platform', 1, 1),
  (10, 'Duck Hunt', 1984, 'Shooter', 2, 1),
  (11, 'Nintendogs', 2005, 'Simulation', 3, 1),
  (12, 'Mario Kart DS', 2005, 'Racing', 3, 1),
  (13, 'Pokemon Gold/Pokemon Silver', 1999, 'Role-Playing', 4, 1),
  (14, 'Wii Fit', 2007, 'Sports', 1, 1),
  (15, 'Wii Fit Plus', 2009, 'Sports', 1, 1);
  
-- Заповнення таблиці Platform_has_game
INSERT INTO Platform_has_game (game_id, platform_id)
VALUES
  (1, 1),
  (2, 2),
  (3, 1),
  (4, 1),
  (5, 4),
  (6, 4),
  (7, 3),
  (8, 1),
  (9, 1),
  (10, 2),
  (11, 3),
  (12, 3),
  (13, 4),
  (14, 1),
  (15, 1);
