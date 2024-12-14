-- creating a new database my_home with users being either landlord or renter for the house
create database if not exists my_home;
create user if not exists 'flavian2003'@'localhost' identified by 'FlavianLeona2003$';
grant all privileges on *.* to 'flavian2003'@'localhost' with grant option;
FLUSH privileges;
