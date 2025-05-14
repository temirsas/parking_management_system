
-- 1. Все занятые парковочные места
SELECT * FROM parking_slots WHERE is_occupied = 1;

-- 2. Все активные билеты
SELECT * FROM tickets WHERE exit_time IS NULL;

-- 3. Количество машин по типу
SELECT vehicle_type, COUNT(*) FROM vehicles GROUP BY vehicle_type;

-- 4. Самое долгое пребывание
SELECT *, 
       (julianday(COALESCE(exit_time, CURRENT_TIMESTAMP)) - julianday(entry_time)) * 1440 AS duration_minutes
FROM tickets
ORDER BY duration_minutes DESC
LIMIT 1;

-- 5. Выручка за текущий день (приблизительно)
SELECT 
    DATE(exit_time) as day,
    COUNT(*) as total_vehicles,
    SUM(10 + (julianday(exit_time) - julianday(entry_time)) * 1440 / 15 * 5) AS total_revenue
FROM tickets
WHERE exit_time IS NOT NULL AND DATE(exit_time) = DATE('now')
GROUP BY day;
