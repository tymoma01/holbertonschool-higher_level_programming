-- 1-create_user.sql
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Remove anything previously granted (including GRANT OPTION), safe even if nothing is set
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_1'@'localhost';

-- Grant full privileges on the server, WITHOUT grant option
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

FLUSH PRIVILEGES;
