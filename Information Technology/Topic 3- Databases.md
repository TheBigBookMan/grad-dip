-  data is stored as set of documents usually like JSON or XML format
- Steps to database design
	1. Model the problem into an entity relationship diagram
	2. Convert ERD into a set of tables
	3. create tables into the database using SQL
	4. import the data
	5. create queries to extract information
## **DBMS**
-  storing and managing databases, is the inbetween end-user and database allows for create, read, update, delete data
	- data storage, retrieval and update- core functionality
	- supporting transactions and concurrency
	- facilities for recovering the database should it become damages
	- supporting authorisation of access and update of data
	- accessing support from remote locations
	- enforcing constraints to ensure data in the database abides by certain rules
- **Main Databases**-
	- **Relational database (RDB)**- data stored in interrelated tables (SQLite, MySQL, ORacle,)
		- Deals with data in tables- each table has rows (records, tuples) and colums (fuelds, attributes)
		- Tables can be joined together to retrieve requested data
		- SQLIte is a small, simplified relational database, doesnt requrire dedicated server to install on but has a wlot of features
		- Reduces **Data redundancy**- where data is repeated unnecessarily and can cause anomolies (the same value changes in one spot but not other causing data to be inconsistent)
		- Four steps for database design
			- Model the problem into an entity-relationship diagram ERD
			- Convert the ERD into a set of tables
			- Create the the tables in the database using SQL and import any data
			- Create queries to extract information
	- **Object-oriendted database (OODB)**- definition of objects which can be references or called later as a unit without having to go into its complexitities, usually used in apps with high performance, calculations and faster results- ObjectBox
	- **Network database 1st gen database model**- multiple member records or files can be linked to multiple owner files and vice versa- IMAGE
	- **Non-relationsal databases(NoSQL)**- can handle unstructured and messy data, good for big data- Cassandra, MongoDB
- **Model the problem**- simplified representation of the world
	- use entity-relationship diagrams (ERD) as basis for the model, its a structural diagram used for database design, contains different symbols and connectors that visualise two important pieces of info
		- major entities within the system scope that defines the extent of system design according to operational requirements
		- interrelationships among the entities
	- business objects  like people, roles( students), tangible business objects (prodiucts) and intangible business objets (logging)
	- Entity is rectangle and relationship is diamond (verb wording)
	- **attributes**- pieces of information about the entity- drawn as ovals
		- underline attribute is the primary key
		- never have spaces or symbols in the name- titlecase
	- **primary key**- one or more attributres that are unique
		- never can be two of a row that have the same uniqueId (primary key)
		- Enforced by the database itself and it will refuse to add a record if it violates the uniqueness of the primary key
		- **surrogate key**- making up a number to be the primary key
		- SQL processes number data types faster than string/char so having a number is a good surrogate key (like a student number)
		- **Universally unqieu identifiers (UUIDs)**- large randomly generated numbers- technical issues that need to be considered
	- **Relationship attributes**- add an attribute to a relationship because that attribute is unique to a specific record of that relationship- eg a order could have many quantities of items in it
## **Convert ERD to tables**
- Entities become tables with their attributes as columns
	- tables written line- TABLENAM(PrimaryKEY, attribute2, attribute3)
	- primary key always underlined and goes first
- **Foreign KEy**- containing the primary key of another entity, indicates that there is a one-to-many or many-to-many relationship
	- the primary key atribute is put as an attribute as an identifier into the record
	- One-to-many  relationsip (Class (M), Teacher(1)) the TeacherId will be the foreign key within the Class as the Class can only have one teacher in it so therefore has the TeacherId because it is unique
	- written in italics
	- Class(classId, className, code, *TeacherId*)
- **Many-to-many relationship**- create a new table which is called **JUNCTION TABLE**
	- table contains both primary keys of the entities and they act as both the primary key and foreing keys
	- contains its own attributes
	- **composite key**- primary key that uses multiple columns- eg the primary/foreign keys of all entities part of the relationship. has to be unique as well
- **One-to-one relationship**- when an entity may reference itself- eg a Person may also be a Student or Teacher and still have the PersonId as the primary/foreign key to themself
## **Create Tables with SQL and insert data**
- **Structured Query Lanauge (SQL)**- very popluar in relational databases, allows for search, add, delete data from database
	- is standard so most relational databases siupport basic SQL operations
	- data types in SQLite are Null = null value, integer= value signed integer, REAL = floating point value, Text is a string
	- No datetime in SQLite data type, so use UNIX timestamp
	- **CREATE TABLE**- creating a table with attributes and the data type
		- CREATE TABLE TableName (
			  FirstCold INTEGER,
			  SedoncdCol TEXT,
			  PRIMARY KEY (FirstCol)
			  );
		  - If a composite key then PRIMARY KEY (Attribute1, attribute2)
	  - **DROP TABLE**- delete a table, it will completely delete it
		  - DROP TABLE TableName;
	  - **INSERT INTO**- once tables are created (MUST BE DONE BEFORE INSERT) then can insert the data, the order of the values inserted needs to match order of columns, unless inputting the data with all columns then just have the order, dont need to specify in the INERT INTO
		  - INSERT INTO TableName(FirstCol, ThirdCol)
			  VALUES(value1, value3);
		  - INSERT INTO TableNameAllAttr
			  VALUES(value1, value2, value3)
	- **SELECT command**- Primary command in SQL to retrieve data from the database
		- SELECT * FROM TableName;
		- This will select all the columns for every row, dont always need all columns so can be more specific
		- SELECT Col1, Col2 FROM TableName;
		- Where keyword will be an arguement
		- SELECT Col1, Col2 FROM TableName WHERE ClientId = '1';
		- Can have operators in as well- this is any clientId greater than 10
		- SELECT Col1, Col2 FROM TableName WHERE CarerId > '10';
	- **LIKE Operator**- checks if texts match a particular pattern
		- **WIldcard**- to have unknown characters match text
			- % will match zero or more characters
			- _ will match exactly one character
		- SQLite the LIKE operator is not case sensitive
		- R% will have matches that start in R
		- %e% will have matches that contain the letter e
		- _ a% show any matches that have an a after the first letter
		- Can have AND or OR conditionals within them as well
		- SELECT Col1, Col2 FROM TableName WHERE FirstName LIKE 's%' AND FirstName LIKE '%s'
			- Above is find any where firstname starts with s and ends with s and return the col1 and col2
	- **IN Operator**- check if a value is in a list of possible values
		- SELECT * FROM TableName WHERE ClientId IN (4, 6, 7);
	- **ORDER BY**- orders the displayed results in a particular order and by a particular field- ASC for ascending and DESC for descengin
		- SELECT * FROM TabkeName ORDER BY ClientId ASC;
	- **AS (alias)**- rename a columnfor ease of use
		- SELECT FirstName as FN, LastName as LN FROM TableName;
		- displays the aliases on the returned table, handy for when theres a condition that makes it easier to see why the column might be different than the name
	- **LIMIT and OFFSET**- restrict amount of rows returned from statement
		- SELECT * FROM TableName LIMIT 100 offset 4;
		- LIMIT will determine how many rows are returned
		- OFFSET will skip a certain number of rows before it starts returning rows
## Aggregate Functions
- Special functions that work over multiple rows and combine the rows, being able to rediuce the table down into a single row
- **COUNT**- count how many values are returned, it returns the number of rows, returns one row with the counted value. In the brackets is how you want it to count that field if that field is not null
	- SELECT COUNT(ClientId) FROM TableName;
- **SUM**- add all values together and return thr sum
	- SELECT SUM(Weight) FROM TableName;
	- Returns the sum of all the weights (that arent null) from the table
- **AVG**- average all the values and return the average value
	- SELECT AVG(Price) FROM TableName;
	- Will return the average of the price column where value is not null
- **MIN**- get the lowest value
	- SELECT MIN(Price) FROM TableName;
	- return the lowest price from the rows that are not null
- **MAX**- get the highest value
	- SELECT MAX(Price) FROM TableName;
	- return the highest price from the rows that are not null
- **GROUP BY**- if you don't want the aggregate to happen over all of the rows, you can group what you are looking for
	- SELECT AVG(Price) FROM TableName GROUP BY categoryId;
	- This will get the average price of each item that shares the categoryId
- The aggregate happens after a WHERE clause so the WHERE clause can minimise and specify the set of records that you are wanting to put the aggregate on as well
	- SELECT AVG(Price) FROM TableName WHERE Price < '200';
	- This will first get all the prices below 200 and then find the average of all of them
- **HAVING clause**- opposite of above and the WHERE clause happens after the aggergate
	- SELECT AVG(Price) FROM TableName HAVING AVG(Price) > 10;
	- finds the average of the prices and then returns any that are greater than 10 average
- **VIEW**- a saved query that works like a normal table except you cant eddit the rows, useful if you have a large and complex query
	- CREATE VIEW MyNewView AS SELECT * FROM TableView;
		- if you have a complex query that you dont want to have to keep repeating, use the VIEW to save it and then just write
		- SELECT * FROM MyNewView;
		- This will reference the saved one from above so just instead of table name you have the VIEW name, you just cant change the rows that were declared in the VIEW creation
- **JOINS**- retrieve information from multiple tables by connecting them together from common fields. Different types of JOINS
	- SELECT client.FirstName, carer.FirstName FROM tblClient client INNER JOIN tblCarer carer ON client.ClientId = carer.TakingCareOfId;
	- INNER JOIN- most common and only show joins that are in both tables
	- LEFT JOIN- also known as LEFT OUTER JOIN, shows all the records that are on the left table even if not matching on the right, then returns a null from right side
	- RIGHT JOIN- alsto known RIGHT OUTER JOIN, same as above but for RIGHT
	- FULL OUTER JOIN- least common, shows all returns even if there are no matches both sides will just return null
	- **ON Claiuse**- is main way to connect the JOIN together
	- **USING clause**- can replace ON, does same thing and can be used for simplicity
		- SELECT cl.ClientName, cl.ClientID, ca.CarerName, ca.CarerId FROM tblCarer ca LEFT JOIN tblClient cl USING(ShiftId);
		- This uses the ShiftId which is in both the tblClient and tblCarer tables and returns the records