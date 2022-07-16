# careers.name as Carreras, collegues.name as Universidad
SELECT * FROM collegues
LEFT JOIN careers_has_collegues
ON careers_has_collegues.career_id
JOIN careers
WHERE collegues.id = careers_has_collegues.collegue_id AND careers.id = careers_has_collegues.career_id AND collegues.id = 2;

SELECT * FROM careers;
SELECT * FROM users;
SELECT * FROM careers;
SELECT * FROM collegues;

SELECT posts.id as id_publicacion from users 
LEFT JOIN posts
ON posts.user_id
WHERE users.id = posts.user_id AND users.id = 4;

SELECT * FROM postcategories;
SELECT * FROM reactions_has_comments;
SELECT * FROM reactions_has_posts;
SELECT * FROM postcategories_has_posts;
SELECT * FROM posts;
SELECT * FROM comments;


DELETE FROM postcategories_has_posts
WHERE post_id = 32;