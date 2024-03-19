-  data is stored as set of documents usually like JSON or XML format
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
## Create queries to extract information
- 