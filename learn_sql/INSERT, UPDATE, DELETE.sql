--SQL INSERT INTO Statement
--The INSERT INTO statement is used to insert new records in a table.
create table Consumers(
	ConsumerID varchar(10),
	COnsumerName varchar(50),
	Address varchar(100)
);

insert into Consumers(ConsumerID,COnsumerName,Address)
values('01','Balavanth','hesaraghatta');

INSERT INTO Consumers (ConsumerID, COnsumerName, Address)
VALUES
('02', 'Emma', 'Yelahanka'),
('03', 'Liam', 'Hebbal'),
('04', 'Olivia', 'Tirumalapura'),
('05', 'Noah', 'Circle');



select * from Consumers

--ALTER TABLE
alter table Consumers
add Pincode int;


--SQL UPDATE Statement
--The UPDATE statement is used to modify the existing records in a table.
update Consumers
set Pincode = 560088 where ConsumerID = '01';

update Consumers
set Pincode = 100200 where COnsumerName = 'Liam'

--SQL DELETE Statement
--The DELETE statement is used to delete existing records in a table.
delete from Consumers where Pincode = 560088

--Delete All Records
--DELETE FROM table_name;

--Delete a Table
--DROP TABLE Customers;





