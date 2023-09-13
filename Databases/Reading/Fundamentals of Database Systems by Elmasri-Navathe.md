# Chapter 1- Intro to database technologies

## Databases
- Represesnts aspects of the real world through raw data (facts)
- Logical collection of data with inherent meaning
- Data is build and designed for a specific purpose (business )
### DBMS 
-Software to allow the system to define, construct, manupulate and shar the databases among users and applications.
	- defining: specifying the data type, structures and constraints of the data and can store the description as a dictionary
	- constructing: process of storing the data on some sort of medium
	- manipulating: functions like querying the database to retrieve data, update and generating reports on the data
	- sharing: allowing mulltiple users and programs to access the database simultaneously

### Characteristics of Databases
- Self descirbing nature of a database system
	- the DBMS will have a catalog or dictionary that contains *meta-data* about each bit of data in there- such as description, data type, name, no of columns, table belongs to etc
	- Makes it easier to understand what all the data is doing and how it related to one another while accessing and ensuring data integrity
- Insulation between programs and data, and dat aabstraction
	- *program-data independence* is where any updates in the DMBS tables by adding in or updating field names doesnt cause problems on the data, while a file sotrage would make it not usable
	- abstract use of concepts can be used in conjunction with functions and queries to retrieve specific data based on different things
	- eg operation of average can caluclate the average GPA for a student based on their average from all their Grades
- Support of multiple views of the data
	- The DBMS can offer users different views of the data depending on their needs
- Sharing of data and multiuser transaction processing
	- **concurrency controle** must be happening to ensure that multiple queries to the database can be happening at once from different sources
	- transactions need to be happening at very fast speeds and the updating of the database needs to keep up to ensure users are seeing data in real time- **online transaction processing (OLTP)**

### Actors on the scene
Many different job titles manage the database
**Database admin**- AUthorizes access to the DB, monitoring and acquiring software and hardware resources for the DBM.
**Database Designers**- Choosing appropriate structures for representing and storing the data.
**End users**- People usually querying the databse
	- Casual: Occasionaly access thdatabase using query interface
	- Naive/parametric: People that are accessing the DB and creating transactions for updating eg bank tellers processing transactions etc
	- Sophisticated: Engineers and analyss etc who familiriazr themselves with the DMBS to perfor complex things
**System analysts/Application programmers**- Making sure the requirements of end users to do specific things and programmers need to know everything as they the big dogS ME

### Workers behind scene
People working on DMBS things

### Data Normalization
Ensuring that data is only in one place to ensure consitency and saving data storage

### Denormalization
Grouping data into same places even if there are multiple fields that are the same to ensure that similar things can be presented together.
**Cotrolling redundency** this way makes it easier to control data, however it MUST be controlled

### Restrictin unauthorizaed access
DBMS must allow for sub-restriction on users as there may be certain people that cant acess specific data or querying due to their unauthorised position.

### Persistent Storage for program objects
**Object oriented database systems** allow for complex data structures in OOP languages. When program terminates the objects are discarded unless they tell them to be stored in a permanent file and this needs to be converted to be stored and then retrieved once application starts agian. **Persistent** object means it can survive termination of porgram and be retrieved by another program
- Persistent is being able to be restored after turned off program, unlike volatile data like RAM where it is turned off and restarted

### Providing storage sttrucutes and search techniques for efficient query processing
- providing quick ad efficient queries and updates to the database and so needs specialised techniques to ensure this.
- **INdexes** are part of disk search and they are auxiliary files which are based on tree data structures or hash data structures. To provess the database record it needs to be copied from disk to main memoery and this involves bufffering and caching.
- **Query processing and optimization** is choosing the efficient query execution plan for query based on storage structures. 

### Providing backup and recovery
DMBS must provide backup for hardware or software failures

### Providing multiple iuser interfaces
GUIs can provide different interfaces for different users that may have different queries for the database.

### Representing complex relationships among data
Must have capaibilites for the complex relationships between data, this is where keys are important and having the ability to match them in the DBMS.

### Enforcing integrity constraints
**Integrity contraints** enforcing these in the DBMS so data sticks by guildines to ensure data integrity among the whole datbaase.
**Referential integrity** ensuring that every section of a record must be related to another record if explicitly said.
**kjey/uniqunesss** - must have a uniuque value
These are applied dependent on the business rules

### Permitting inferencing and actions using reules and triggers
- **deductive database systems** complex rules that can be determined by deduction in the database
- **triggers**- when certain stuff happems in the fields, then something else can get triggered and cause a field to be updated
- **stored procedures** - these are done when certain conditions are met within the database