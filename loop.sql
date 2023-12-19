DO $$ 
DECLARE
    i INT := 1;
BEGIN
    LOOP
        EXIT WHEN i > 5; -- Зупинка після вставки 5 рядків
        INSERT INTO Platform (platform_id, Platform_Name) VALUES (i, 'Platform ' || i);
        i := i + 1;
    END LOOP;
END $$;
