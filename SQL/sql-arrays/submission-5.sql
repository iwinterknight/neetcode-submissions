CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    items TEXT[],
    total_price INTEGER
);

-- Do not modify below this line --
-- INSERT INTO orders (id, items, total_price) 
--     VALUES (1, ARRAY['apple', 'banana'], 100),
--           (2, ARRAY['orange', 'grape'], 200),
--           (3, ARRAY['watermelon', 'pineapple'], 300);

INSERT INTO orders (items, total_price) 
    VALUES (ARRAY['apple', 'banana'], 100),
          (ARRAY['orange', 'grape'], 200),
          (ARRAY['watermelon', 'pineapple'], 300);


SELECT * FROM orders;
