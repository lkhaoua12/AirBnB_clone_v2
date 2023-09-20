-- Create the database 'hbnb_test_db' if it doesn't exist
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create a new user 'hbnb_test' on localhost with a password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on 'hbnb_test_db' and select privilege on 'performance_schema'.
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply the new privileges for the user.
FLUSH PRIVILEGES;
