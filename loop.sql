DO $$
BEGIN
	FOR i in 1..30
		LOOP 
			INSERT INTO global_sales (gs_id, game_id, sales, year_of_update)
			VALUES (i, i*10, i * 1000000, 2020);
		END LOOP;
END;
$$
