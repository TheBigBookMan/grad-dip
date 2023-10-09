# Chapter 1- Intro to database technologies

## Databases

-   Represesnts aspects of the real world through raw data (facts)
-   Logical collection of data with inherent meaning
-   Data is build and designed for a specific purpose (business )

### DBMS

-Software to allow the system to define, construct, manupulate and shar the databases among users and applications. - defining: specifying the data type, structures and constraints of the data and can store the description as a dictionary - constructing: process of storing the data on some sort of medium - manipulating: functions like querying the database to retrieve data, update and generating reports on the data - sharing: allowing mulltiple users and programs to access the database simultaneously

### Characteristics of Databases

-   Self descirbing nature of a database system
    -   the DBMS will have a catalog or dictionary that contains _meta-data_ about each bit of data in there- such as description, data type, name, no of columns, table belongs to etc
    -   Makes it easier to understand what all the data is doing and how it related to one another while accessing and ensuring data integrity
-   Insulation between programs and data, and dat aabstraction
    -   _program-data independence_ is where any updates in the DMBS tables by adding in or updating field names doesnt cause problems on the data, while a file sotrage would make it not usable
    -   abstract use of concepts can be used in conjunction with functions and queries to retrieve specific data based on different things
    -   eg operation of average can caluclate the average GPA for a student based on their average from all their Grades
-   Support of multiple views of the data
    -   The DBMS can offer users different views of the data depending on their needs
-   Sharing of data and multiuser transaction processing
    -   **concurrency controle** must be happening to ensure that multiple queries to the database can be happening at once from different sources
    -   transactions need to be happening at very fast speeds and the updating of the database needs to keep up to ensure users are seeing data in real time- **online transaction processing (OLTP)**

### Actors on the scene

Many different job titles manage the database
**Database admin(DBA)**- AUthorizes access to the DB, monitoring and acquiring software and hardware resources for the DBM.
**Database Designers**- Choosing appropriate structures for representing and storing the data.
**End users**- People usually querying the databse - Casual: Occasionaly access thdatabase using query interface - Naive/parametric: People that are accessing the DB and creating transactions for updating eg bank tellers processing transactions etc - Sophisticated: Engineers and analyss etc who familiriazr themselves with the DMBS to perfor complex things
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

-   Persistent is being able to be restored after turned off program, unlike volatile data like RAM where it is turned off and restarted

### Providing storage sttrucutes and search techniques for efficient query processing

-   providing quick ad efficient queries and updates to the database and so needs specialised techniques to ensure this.
-   **INdexes** are part of disk search and they are auxiliary files which are based on tree data structures or hash data structures. To provess the database record it needs to be copied from disk to main memoery and this involves bufffering and caching.
-   **Query processing and optimization** is choosing the efficient query execution plan for query based on storage structures.

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

-   **deductive database systems** complex rules that can be determined by deduction in the database
-   **triggers**- when certain stuff happems in the fields, then something else can get triggered and cause a field to be updated
-   **stored procedures** - these are done when certain conditions are met within the database

# Chapter 2- Database System Concepts and Architecture

Databases used to be a part of the monolithic system but now theres more broken down database architecture eg- web servers, database saervers, file servers, application servers etc

**CLoud computing** environments usually have thousand of alrge servers to manage big data

## Client/Server architecture

-   **Client Module** -designed so it can run on mobile device, user workstation and PC. Application programs and UI like priovindg the GUI, forms, mobile device apps.
-   **SErver module**- handles data storage, access, search and other functions

## Data Models, Schemas and Instances

-   **Data abstraction** - being able to hide a lot of the complex business logic and organisation and storage.
-   **Data model** - collection of concepts that describe the structure of the database- data types, relationships and constraints and operaions for updates based on circumstances. Providing the layout and structure for how the database will be
-   **dynamic aspect**- can provide details about more complex operations that may be special in particular to that database- eg calculate_GPA, rather than insert/delete etc

## Categories of data models

-   **High-level/conceptual data models**- Provide the concepts that are closer to how users perceive data
    -   **entities**- represents a real-world objet or concept (employee/ project)
    -   **attribute**- represents some field that describes the entity (emploeeName, salary)
    -   **relationship**- how two entities are associated together (employee works on project)
    -   **Object-data model**- Newer version of high-level data model
        -   **Object Data Management Group (ODMG)**-
-   **Low-level/physical data models**- Provide concepts that are more representational to people with good understanding of computers/database already
    -   Describes data stored as files in the computer by using recording formats and acces spaths.
    -   **Access paths**- search structure for how the database searches through records faster
    -   **index**- putting an index or key term on data to allow for quicker organisation and finding
-   **Representational/implementation data models**- a mix of inbetween, where easily understood by end users but not too far from being computer specialist.
    -   _Relational data model_- most commonly used in DBMSs- sometimes called record-based models
    -   Will usually have explicit names for attributes and fields as well as data types
-   **Self-describing data models**- data that is stored in the database and has a key-value pairs that have a description of the data within the data themselves- _descriptive_
-   **Hierarcal data model**- like a tree structure with the parent-chiold relationships, parent can have multiple children but child can only have one parent
-   **Network data model**- more complex relationships between data, same as tree structure

## Schemas, Instances and Database state

-   **Database Schema**- the description of how the database design is, utilises the **schema diagram** to show users how the data fields and attriutes will be laid out using the names of the database fields and their attributes. Not all bits of data information will be in the schema diagram, it is more of just a basic layout for how the fields and attributes will work. Usually no relationship eonnectors, constraints or data type. Usually the dataqbase schema does not change but when a new field is added to a table it is called **schema evolution**.
-   **Schema construct**- Each object in the schema is a schema construct (Student, Course)
-   **Database state/snapshot**- the current state of how the database is at any given moment in time when there is not an **occurrence/instance** happening (insert, update, delete etc) is what that current database state is. It can change all the time and therefore the sdatabase state is changing.
-   How they connect are that the database _schema_ is how the data model is defined and this controls how the state will look and ensure its integrity. When the database schema has been defined the database _state_ is empty until first **populated/loadad** with data and the state has changed. The DBMS needs to ensure that the current state is of the right integrity based on the schema, this is **valid state**. Creating a correct schema is important and writing the details in the data catalog for correct usage.

## Three-schema architecture and Data Independence

IMportant characterists of the database, good for visualisation of the database in different schema levels. Process of transforming requests and results between levels are called **mappinngs**.

1. catalog to store database description (schema) so its self-describing
2. insulation of programs and data (program-data independence) so change in data doesn't impact programs
3. support musltipl users- so different viewers can do different interactions with data
   **Three-Schema Architecture**- split the applications from physical database
4. internal level has internal schema, describes the physical storage of the daabase, physical data model and describes the access paths for the database (low-level)
5. conceptual level has conceptual schema where describes structure of the whole database for users which makes it readable to non-tech people. Usually hides the complexities of the storage and makes the description more abstract. (high level)
6. external level with external schemas or user views, describes the particular part of the database that that user uses and then hides the rest, usually using a representation model in a high level format for the end user to understand

**Data Independence**- Being able to change the data on one level without having to change it on another level.

-   **Logical data independence**- having the data in the schema for specific tables and relationships, and being able to change something (add new table, column, field, row) or create relationships without impacing the other data and the applications that represent the data.
-   **Physical data independence**- changing the physical storage of data (disks, cloud, database type- NOSQL, SQL) without data being skewed or changed or location of the data on storage (maybe change for speed by compression etc)

## Database Languages and Interfaces

DBMS must provide eppropriate langauges and itnerfaces for users to be able to use without trouble and not cause data integrity problems

-   _Languages_
    -   **data definition language (DDL)**- define the schemas and creates a description across all the levels as most DBMS dont have a clear separation of the levels listed above
    -   In DBMS where clear separation of the levels ism the DDL specifies the conceptual schema only and another the **storage definiton language (SDL)** is used to specify the interal schema.
    -   To be able to view the user views and their mappings to the conceptual schema- use SQL
    -   The DBMS uses a **data manuplation language (DML)** for insertion, deletion, retrievel and modification
    -   SQL does basically everything above and is the main way to talk to the DB, there are other ways though to do low-level database storage as thats different to the conceptual database storage
-   _Interfaces_
    -   **Menuu based interfaces for web clients**- Menu type of list of options that allows the user to select the query that they want to use, reduces the complexity of syuntax memorisation of SQL
    -   **Mobile apps**- applications on the phone that allow the user to be able to access databases- eg banking on phone
    -   **Forms-based Interface**- Providfes end users an easier way to fill out information to be added to the database, _forms specification languages_
    -   **GUI**- Some sort of graphical way that has forms and menus for the user
    -   **Natural langauge interfaces**- uses a natural language (english) for the end user to create a query through matching the words to a dictionary from the conceptual schema, it tries to create the query through this, the user can write it in asentence (return all users that went to UNley high)
    -   **Keyword-based database search**- Similar to how web search works with strings of natural language and will match them with a keyword to return the value
    -   **Speech input and output**- similar to natural language interface where the user will speak a sentence and the words will match up to sepcifed schema in the application to create the query

## Database System Environment

How the whole DMBS is split into different components that do separate things and combine together to make it all work

-   Database and DBMS catalog is stored on the disk and controlled by the OS, disk read/write
-   **Stored data manager**- module ofg the DBMS controls access to DBMS information that is stored on the disk
-   The users (DBA staff, casual users, application programmers etc)- will forumlate queries through programming languages, applications, data entry through parametric transactions.
-   The users queries will then be compiled by processing the schema definitions and stored meta data iof the description in the DBMS catalog, which inlcudes names, file sizer,, mapping data, constraints
-   **Query optimizer**- takes the internal query ad will do the rearrangements and algorithms to reduce redundency and make the checks against the system catalog for stored data
-   Even if an application is written in a language like Java, C++ etc the **precompiler** will extract the DML commands and sent to the DML compiler

## Database SYstem Utilities

These utilities help the DBA manage the database system, basically through functions and certain operations

-   **Loading**- Being able to load existing data files that are in a specific format into the database, there would be specific utilities that require specific file types, using conversion tools
-   **Backup**- backup of the database which is stored on some storage area in ccase of needing to reimplement it
-   **Database storage reorganization**- reorganise set of database files into different file organisations and creat new access paths for performacen imporvement
-   **Performance monitoring**- monitors database usage and statistics to the DBA on how the CPU etc are being used and if things need changing

## Tools, application environments and communication facilities

-   **Information repository**- is an expanded data dictionary that also has meta data information about design decisions, application program descriptions and user information. Can be accessed by the DBA or user
-   **COmmunication software**- software packages that allow for communicating to the database from a remote location through termainsl, workstations or PCs. Usually using stff like interet routers, local networks etc. Called DB/DC and can also be used through LANs.

## Centralized DBMs Architecture

-   Having all the features of the DBMS on one processing machine, like a PC or mobile phone.
-   Would hav ethe DBMS functionality, application program execution and user interface processing all in one
-   was because PC computers hardware became cheaper and could move from the terminal to having a graphical interface

## Basic client/server Architectures

-   Usually mobile phones and PCs are client side only machines because they are handling most client rendering, while a server hosting backend stuff- API, databases would be hosting that
-   The client usually uses some sort of local server in the device to allow functionality to produce client side stuff, but once it needs backend things it will connect to the server through wireless networks or LANs
-   The server is hardware that contains software which is specific for providing services to the client
-   Some machines only install client software, some only server software and some bboth

## Two-tier Client/SErver Architecture for DBMs

-   Using two-tier mainly in an RDMS due to SQL providing more logical divide between server and client, the server side can be called **query server/transaction server/SQL server**.
-   The user interface programs and app programs run on client side. The standard of **Open Database Connectivity (ODBC)** is used to create the API for the client side to talk to the DBMS server.
-   Both client and server need the relavant software for the connection to happen

## Three-Tier and n-Tier Architectures for Web Apps

-   many web apps use the three tier, add an intermediate layer between client and server
-   **Application server/web server**- the middle layer where a lot of the business logic is made to be able to determine the correct querying for the database, this is due to the clients request, where it will then be handled by the business logic in the middle and then send request to the DBMS
-   There is good security in the middle layer where users credentials can be checked on the request before any request to the database will be made

## Classifications of Database Management Systems

-   **Data model**- NOSQL, SQL, hierachal, object-relationa:- based on how the data will be represented
-   **Number of users**- single-user systems like a PC or miltiuser-system like a DBMS that allows concurrent multiple users
-   **Nmber of sites distributed**- If the DBMS is crentralized then the data is stored on the single computer, can support miu;tiple users but relies on always using that one site. **distributed DBMS (DDBMS)** has the database and software distributed over many sites connected by the computer network.
    -   **Homogenous DDBMSs**- use same DBMS software at all the sites on a distributed sites
    -   **Heterogenous DDBMSs**- can use different DBMS software at each site and have midleware software can access several different databases, which is a **federated DBMS/Multidatabase system**- allowing for each database to have some sort of autonomy
-   **Cost**- Some software like MySQL, PostgreSQL are open source and then there are some other DBMS services which are paid. SOme have licenses that allow certain amoun of usage
-   **Types access paths**- DBMS can be created for a general purpose or a speci;liased purpose. **specialised purpose**- the DBMS cannot be used for other applications without major changes, these are **Online transaction processing (OLTP)**

# Chapter 3- Data Modeling Using the Entity-Relationship (ER) Model

## Using High lievel Coneptal Data models for Database Design

-   **Requirements collection and analysis**- first step when designing a database is getting the user to explain their **data requirements** which need to be in detail and as complete as possible
-   Need to also specify the **functional requirements**- that are the transactions and operations that are happpening withi nhe database- retrievals and updates
-   THen once getting a broad overview, need to create the **conceptual schema** which is a high level data model of the **conceptual design** of the data. Detail descriptions of entity types, relationships and constraints.
-   **Logical design/Data model Mappeing**- implementing the data design into a DBMS, transforming the conceptual schema into the implementation data model.
-   Last step ius the **Pshycial design**- when internal storage structure, file organisaztions, indexes and access paths are implementd.

## Entity Types, Entity Sets, Attributes and Keys

**Entities**- are specific instances of an object- Employee, Manager, Department etc
**Entity Attributes**- each entity will have attributes- firstname, lastname, id number etc

-   **Composite/atomic attributes**
    -   **Composite Attributes**- When an attribiute can be broken down into multiple parts, eg- persons address (street, suburb, city, country). This then can also be broken down more in the street composite attribute- forming a **composite hierarchy** (streetNum, streetName). Don't always need to break down if not going to be referencing the indibidual broken down composite attributes.
    -   Attributes that cant be broken down are \*\*atomic attributes/simple attributes
-   **Single valued/multivalued attrbiutes**
    -   **multibvalued valued attributes**- when an attribute can end up having different amount of values, eg- a attribute called numDegrees- where some people may have 0, some 1, me 3- there can sometimes be constraints on what the values can be or be between
    -   **single valued**- when there is only going to be one value for that attribute- age, height, weight
-   **Stored/derived attributes**
    -   **stored attributes**- are attributes that are created by hard data- eg birth date
    -   **derived attributes**- are data that are made by a certain measurement- eg someones age based on the current date and their birth date.
-   **Null values**- This is just non applicable, can be used **TWO** cicrumstance- when the attribute is not applicable to that entity, or when the value for that entity is unknown
-   **Complex attributes**- nesting of composite attributes and multivalued attributes, using () and {}
-   **Entity Types/Entity sets**- These are similar to tables and instances of the entities, but they are a more abstractr representation. Entity type is the schema for how an entity will be created, it defines the atributes and the title for the entity, while the entity set is a collection of entities that are created through that entity type schema- eg type (Employee), set ((Ben Smerd, 27), (Jack Morgan, 28))
-   **Key attributes of entity type**- a unique attribute where every entity will have a different value for that specific attribute- this could be an email address, ID, name etc. **Composite key**- is the grouping of values to form a unique key
-   **Value sets (domains) of attributes**- can be a sort of constraint on the value by setting it a specific range or data type- age has to be anumber between 12-70

## Relationship Degree, Role names and Recursive Relatoships-

**Degree of relationship**- is determined by amount of entitity types that are participating, more amount of enetities being involved in the relationship mean a greater degree of the relationship

-   **Unary**- when an entity can have a relationship with itself, eg- Person can be a Parent of another Person
-   **Binary**- when there are two types- eg a Student and Course where they are Enrolled
-   **Ternary**- When there are three types- eg Student, Course, Teacher in a Classroom
-   **N-ary**- When there are more than 3 entities creating a relationship
    **Relationships as attributes**- either direction of the binary relationship can be represented as an attribute- Student is enrolled in Course, a Course has Students enrolled
    **Role Names and Recursive Relationships**- **Role names** help to identify the attributes plying role in the relationship (its not necessary but can provide a more detailed explanation for what they do)
-   **Recursive relationships**- are when entities within their own type participate in more than one role, for example an employee can be a supervisor while also being supervised
    **Constraints on Binary relationship types**-
-   **Cardinality ratios for binary relationships**- Identfying the amount of times an entity can have a relationships with another entity, eg an Employee can only be in one Department but a Department can have many EMployees- E 1:N D
-   **Participation Constraints**-
    -   **Minimum cardinality constraint/total participation/existence dependency**- when an entity can only existence when it is related to another one- eg an Employee entity can only exist if it is related to a Department, so any employees must be related to deparments via the works_for entity
    -   **partial cardinality**- some of the set of entities are related to another entity, eg. the Employees only have some that are Managers
    -   Both equal the **structural constraints**
-   **Attributes of relationship types**- these are attributes that are in the relationship type between the entities that are involved eg. an Employee WORKS_IN a Department and the WORKS_IN relationship type may have an attribute about Department_Start_date that has the Employee and Department relationship. These relationship type attributes could also be migrated to either entity depending on suitability

## Weak Entity Types

Entities that have no key attributes are **weak entity types** and ones that do have key atributes are **strong entity types**

-   **Strong entity type**- have primary keys and attributes that can be used to identify the entity
-   **Weak entity type**- relies on other entities to identify the the entity, its relation to the entity that is used is called the **owner entity type**, it also has a **participation constraint** as it is dependent on the owner entity types existence
    -   Weak entity has the **partial key** where there is the relating attribute to the owner entity type used to identify the entity, sometimes needs a composite key

## Relationships Types of Degree Higher than Two

Different type of relationship entity degree, before explained binary where there were two entities that formed a relationship, ternary (or more) are **higher degree relationships**

# Chapter 4- The Enhanced Entity-Relationship (EER) Model

EER is a more advanced way to create a database design when there is more complex data (complex businesses)

## Subclasses, Superclasses and Inheritance

EER model contains everything the same from ER model

-   **Subclass/subtype**- A subgroup entity that is derived from the parent entity, for example the parent entity (**superclass/supertype**) called Employee and the child centity (**subclass/subtype**) called Engineer, Admin, Clerk, Developer, SalariedEMployee, HourlyEmployee etc. the relationship between the **superclass** and the **subclass** is called the **class/subclass relationshiup**. The child subclass may have a certain record of the parent superclass to be able to recognise its relationship.
- Instance of the superclass can be members of multiple subclasses and not all instances of the superclass need to be an instance of a subclass
-   IMPORTANT- an entity cannot exist in the database as only a subclass, it also needs to become a member of the parent entity (superclass)
-   The superclass entity can then be optionally added in to a subclass if they meet the descriptiong
-   An entity can be a member of multiple subclasses
-   The subclass **inherits** all the attributes and relationships from the parent class and this can mean that subclass can also be known as its own entity type

## Specialization and Generalization

-   **Specialization**- A specific type of subclass that can be a part of the parent class, for exampl (RELATED TO EMPLOYEE ABOVE)- may have the subclasses (Engineer, Admin, Clerk, Developer) that are _job type_ and then (Developer, Engineer) are _engineer type_ and (HourlyEmployee, SalariedEmployee) might be _method of pay type_
-   THe sepcialisation on the diagram will be split from the parent Entity and then have the subclasses branching off of that
-   Attributes that are attached to Subclass are called **specific/local attributes** meaning that any attribute that is specifically to the subclass is that, eg attributes to Engineer but arent attributes to Secrarty
-   Subclasses can also participate in relationships called **specific relationship types**
-   It looks like a 1:1 relationship between entities but it is actually the same entity being represented within the superclass and the subclass because they are instances of both entities (an instance of the subclass has to be an instance of the parent class) as they are playing a **specialized role**
-   Use of specilizations is in case there are certain subclasses that have specific attributes that other entities would find redundant
-   Also important to be able to create entity specific relationships that would be unecessary with other entities
-   **Generalization**- Essentially the reverse of the specialiszatio, where you find entitties that have common attributes (or similar) aand then create a superclass entity that will have the common attributes and then the former 2 separate entities are now subclasses of the **generalized superclass**
-   Can view the Employee entity as a generalization of the Engineer and Secratry entities or we can view the Engineer and Secretary entities as specializations of the EMployee entitity
- In a diagram, a **specialization** is represented by a circle using a singular or double line (*depending on completeness constraint*) connected to the superclass\
- **Completedness constraint**- if a specialisation is total or partial partiticpation
	- **Total participation**- if the superclass has a total participation to the specialisation then every member of the superclass MUST BE a member of  atleast one subclass in the specialisation
	- **Partial particiaption**- the superclass has a partial participation to the speclisation and therefore can have the option of being NONE of the members of the subclass to the specialisation
- A 'U' shape is on the line from the circle (listed above) and the child entity with the U pointing towards the parent entity
- in the middle of the circle is either 'o' or 'd' represented for **overlapping** or **disjointed**. Can't have one for a singular subclass as the whole point of the o or d is to determine how many superclasses can also be a part of the subclass, so if theres just one then it is not needed
	- Overlap (o) means that an entity from the superclass can belong to more than one of the subclasses where it can have attributes and characterstics of multiple subclasses simultaneously. This means that the entity Employee that has subclasses of Secretary, Engineer and Technician, that an instance of Employee can be a Secretary OR an Engineer OR a technician OR can be a multiple of them-eg Secratrey AND Engineer
	- The disjointed (d)  means that an entity from the superclass can belong to only one of the subclasses and that they are mutually exclusive. A specialisation has to be either one. This means that they can only be one subclass at max so a Secretary OR Engineer OR Technician. 
- 

## Constraints and Characteristics of Sepcialization and Generalization Hierarchies

-   **Predicate-defined/condition-defiend subclass**- when the subclass has a predefined condition that must be met to be able to become part of that subclass, which is a **constraint**.
-   The **Predicate constraint** is presented on the line joining the parentclass to the subclass with the title of what must be met by the subclass, for example the Employee parent has the **predicate constraint** that each subclass must have a job_type value- this connects them to the Employee entity
-   If all the **specilisation attribute** are of the same for each subclass then its called the **attribute-defined specialization** and the attribute is called **defining attribute**.
-   If no **condition** to determine membership in subclass then the subclass called **user-defined** where it is determined by the user applying the operation to the subclass
-   **Disjointness constraint**- defines that a subclass of a specializaton can be a member of at most ONE subclass

# Chapter 5- The Relational Data Model and Relational Database Constraints

## Domains, Attributes, Tuples and Relations

-   **Domain (_D_)**- values that are restricted to certain guidleines- 10 digit phone numbers. Can also have specific measuremtns for helping guide the value representation, like $ for dollar as it could also be euros or other currencies
-   **Relation Schema (_R_)**- Describing a relation by describing the attributes of that relation. The **degree of relation** is number of attributes of its relation schema
-   **Tuple (_t_)**- are the fields of that entry that would be added as an instance to the entity, essentially the row of values that match up to the attribtues. usually Tuples are ordered in sequency of how the attributes are displauyed in the table, however you can make them unordered by making it a key=value pair
-   **Values and Nulls in tuples**- the values have to be atomic, meaning cant be broken down in composite or multivalue, called **flat relational model**, any mulivalue values have to be represented by a separate relation. **NULL** is when the value is unkown for that specific entity or the attribute is non applicable

## Relational Model Constraints and Relational Database Schemas

THree different types of constraints

1. **Inherent model based constraints/implicit constraints**- inherent in the data model
2. **Schema based/explicit constraints**- Directly expressed in the schemas
3. **Application based/semantic/business rules**- cant be expressed in the schema and need to be enforced by the actual application

-   **Primary key**- singular or multiple attributes/columns in a table to identify a record uniqurly identifies- can be singular like a superkey or multiple like a composite key
-   **Suerpkey**- is the attribute that uniquely identifies an entity (like an ID) and can identify alone- least amount of superkeys that can uniquely identify a record,
-   **Composite key**- is when multiple fields together are joined to create a uniqueness of identifying and if one of the keys is gone then they dont work, so need all to work together, can find the least amomunt to identify the uniqueness
-   **Candidate Key**- same as composite key but each key is unique in itself
    Any database has the database schema and state, if the current state of the database doesnt hold up the integrity of the database schema it is called **not valid state**
-   **Entity integrity constraint**- a primary key _CANNOT_ be NULL
-   **Referential integrity constraint**- if a relation between two tuples in two relations, that the tuple that is relating must relate to an existing entity

## Update operations, transactions and dealing with constraint violations

-   **Retrievals**- relational algebraic expression to query database for data creates a new relation
-   **Result relation**- is the result from the relational operators to retrieve the data
-   If performing a **DELETE** command these are the types of constratins you can apply on delete:
    -   **cascading**- when a violation has occured with modification of some sort, the tuples that are involved with relations with the modified record will have their own values or something changed due to the changing situation to hold up data integrity. So if you are deleting a row from the entity with the primary key, then it will delete the row in a entity model that holds it as a foreign key and delete that row
    -   **Nullify**- if removing an item from a relation then we can set it so that value in the forein key tuple will be set to NULL
    -   **Restricted**- if the item being deleted has a reference (**referential integrity constraint**) then the item cannot be deleted. Throw an error when trying to delete it, can force it to go through though and then do something like cascade and delete the referetnial table

# Chapter 9- Relational Database Design by ER- and EER-to-Relational Mapping

Designing an relational database schema based on conceptual schemas. This step of the database design process is the **logical database design/data model mapping** where we are transferring the concepts of what is wanted for the businesses and creating a form of table and relational schema with entitities and relationships. It's bridging the gap between having a conceptual diagram of overall concepts and then creating the tables to establish entity attributes and relationships.

-   **Conceptual schema diagram**- usually is a some sort of links between diagram shapes with titles
-   **Entity-relational diagram**- entity tables (2-dimensional tables with rows/records and columns/attributes) which will have the relationships between the bits of data presented within keys (primary and foreign), which is showing how the entity and referential integrity is created.
    -   **Integrity constraints**- **Entity integrity constraint** is shown by the primary keys that are drawn with the line under. **Referential integrity constraint** is shown by the relationship that one entity is referencing another by the foreign key

## Conceptual ER- diagrams

-   WHen drawing an **entity** it is important to have it as a square with the entity name in the middle and then **attributes** are drawn as a circle with the attribute name in the middle, linked by a line
-   **primary keys** are identified by having an underline of the word in the attribute in a circle
-   **foreign keys** are identified by being in italics
-   Most **attributes** are **atomic/simple** in that they are singular valued and cannot be broken down, however if the attribute is **composite** it can be broken down (address: (number, street name, postcode, state)) and this can be represented by each of the sub-attributes of the composute attribute being represented by more circles with the attribute text in the middle
-   **multi-valued attributes**- attributes that the instance of the entity can have multiple values for- degrees (RMIT, flinders, la trobe) and this represented by the attribute being in a cirlce with another circle around it
-   **derived atributes**- are attributes that has their values based on another attribute- an age can be derived from someones birth (current date - birthdate) and this is represented by the attribute circle being dotted lined
-   **Relationships**- relationship entitties are represented with a diamond with the relationship entity name in the middle
    **Cardinality**- representing the relationship between the two entities and how many instances of one will there be an instance of the other entity, it also shows the minimum and maximum number as constraints
    -   1:N relationship is represented by a 1 on one entity and N on the other, with the min-max cardinality values being represented on the lines between entitiy to relationship entity, eg (0,N means that the entity on the left can have minimum teaching 0 subjects or being teaching infitnite amount of subjects), while on the other end the subjects entity (1,1 means that the subject can only have minmum 1 teacher (this is dependent on the teacher entity being existant- **total participation**) and maximim 1 teacher (as a class can only have one teacher))
    -   IMPORTANT to map out the min-max to figure out if one entity is reliant on the other entity for being existant- their level of participation (**total**- if the entity is reliant on the other entity existing for that entity to exist (represented by a double line on the diagram), **partial**- if the entity is not dependent on the existence of the other entity (represented as just the normal straight line)). the min-max deteremines the amont of instance existence that entity has in relation to the other entity, through the relationship entity- so looking at the min-max on the Teacher side represents the minimum amount of Subjets they can teach and the maximum amount of Subjects they can teach- so it represents the other entity
    -   **Participation constraints**- represents if aan entity can exist without the existence of the other entity (**partial**) like the Teacher entity witht the Teaches relationship entity (a teacher doesnt need to teach a subject), while the Subject entity is only in existence to the Teaces relationship entity (**total**) if there is a Teacher that can be teaching the course (as a subject needs a teacher to teach it)
    -   **_TIP_** - can determine the **cardinality participation** by looking at the minimum cardinality- if it is zero then it is **partial** participantion and if it is a number not zero then it is **total**
    -   The **weak entity** is an entity that is total dependent on the other entity and only exists because of that **owner-entity**

## Step to draw ER diagram

1. **identify enttities**- incluring the weak entitites
2. Represent each entity graphically by a rectangle
3. Search for reltaionships between entitties and represent them graphically by a diamond (check for degree of relationship- unary, binary, ternary, n)
4. Identify constraints on each relationship
    1. Cardinatlity (1:1, 1:M, M:N) and min-max
    2. Participation- Total or Partial and make either the double or singular line
5. Identify all attributes and underline the priumary keuy

## Top-Down approach transform Data Model into Relationsl Logical Model

Transforming the relational model into an ER diagram of relational tables

-   **Moddeling**- looking at the problem description in a natural language (english) and modelling the problems into an ER diagram--- doing the tranformation mapping above
-   **Design**- Creating the actual diagram (the UML diagram like on the Lucidchart)

## Steps to creating transofrmation from conceptual to ER diagrams- 7 step mapping algorithm
Don't need to consider children entities in step 1, only until step 8 start looking into the children entities and their relationships.
1. **Mapping of regular entity types**- find the **strong entity types** (ones that have primary keys) and start to identify which key would be the primary- (may be an individual key or composite key). These are the main entities that represent the core conceptual objects in the database. Underline the primary key. Only add the simple attributes (no multivalue or composite etc). NOT CHILD ENTITIES, this is the reason why coming back to step 2 is important after step 9 because you have formed new regular entities by looking at cardinality, union, specilisation and coming back here is to find new entities
2. **Mapping of weak entity types**- the **weak entity types** (do not have keys) and find the relation, create the relation primary key to be the **owner-entity type** and the partial key of the weak type (if it has one) (COMPOSITE KEY). Make the primary key of te weak entity also the foreign key from the owner-entity
3. **Mapping of binary 1:1 relationship types**- 3 possible approaches to create a 1:1 relationship type: Try and pick the side that would have more rows in the database as the one that will have their primary key as the FK as it will change way less rows than the other
    1. **Foreign key approach**- the entity that is not dependent on the other entity will be chosen to have its main attributes as the relation attribute because it is not reliant on another entity for existence. Having the foreign keys in the relation. Entity that is total pariticipation indluces the foreign key which is the primary key of the other relation
    2. **Merged relation approach**- mergin the two entity types and the relationship into a single relation, would need both participants being total
    3. **Cross-refernce or relationship relation approach**- adding in the relationship relation as a third table that would have both primary keys of the other two relations to be as foreign keys within it
4. **Mapping of binary 1:N Relationship types**- 2 possible approaches to create a 1:N relationship type
    1. **Foreign key approach**- add in the primary key of the entity that is going to have multiple instances, so for example if its an Employee that will have Shifts, have each primary key of the Employee as a foreign key in the Shift entity. Whatever is the Many (M) will have the primary key of the 1 in their foreign key
    2. **Relationship relation approach**- creating the third relation **relationship relation** and this has the foreign keys as the primary keys of the entities
5. **Mapping of binary M:N relationshiup types**- must use the **relationship relation/cross-reference option**- as the third relationship is the only possible way to store multiple instances of an entity comprising of two participating entitities. Have both relations primary keys as foreign keys within the relationship relation as well as the attributes. THe primary keys create a composite key as they are a combination of both primary keys
6. **Mapping of multivalued attributes**- when an attribute has multi values, create a new relation which will be the instance of that value, and make the primary key of the relation entity as the foreign key in the new relation
7. **Mapping of N-ary relationship types**- using the **relationship relation option**- this is where there are more than 2 entitities in a relationship and therefore will need a relationship relation whjich will store the primary keys of each entity as foreign keys and as the primary keys as all of these will be considered to make up the uniqueness of each entity (**composite key**) , if there isnt one of the other relation primary key then the relation fails

-   having the foreign key in the relation allows for a natural join (**EQUIJOIN**) of that sharing attribute from both entities, but then when there is a relationship entity it requires 2 joins for M:N as the relationship entity wil lrequired a join from both of the participating entitites and a N-ary relationship entity will have n joins as it will have to get all of the entitties to match the attribute of the foreign key

Step 1-7 is for ER and 8 and 9 are for EER
## Transformation of Specialisations in EER diagram
Transforming the diagram into the set of relational tables in step 8 of the transformation. Can have one of the 4 options from the **completedness** and the **disjointeed** constraits. 
1. Disjointed and total participation
2. Disjointed and partial participation
3. Overlapping and total participation
4. Overlapping and partial participation
Depending on the selection one of those 4 and other considertaion need to decide on one of these for creating the tables. MORE Efficient to go with single tables, but if not applicable then fine with multiple tables
- **Option 8A- Multiple tables**- *Superclass and subclasses*- 
	- Relation for superclass that contains PK and all other superclass attributes
	- Create relation for each subclass which includes all attributes of that subclass and PK is the PK from superclass which also makes the PK in the subclasses and FK
	- Option is suitable for any specialisation combination
	- Creating a table for each superclass and its subclass where the primary key of the superclass will be the foreign and primary key in the subclasses
	- not good if the subclasses have no attributes as extra tables for no reason
- **Option 8B- Multiple tables**- *subclasses only*- 
	- Create relation for each subclass that contains superclass attrbitues and the attributes of that subclass, PK is PK of superclass
	- Option only works for specialisation whose subclasses are total participation (everu entity in the superclass must belong to a subclass) because there wouldnt be a table for the superclass that isnt a subclass
	- If specialisation is overlapping, entity may be duplicated in several relations
	- The difference here is that the subclass tables are not foreign keys as they dont refer to the superclass table primary key anymore
	- No superclass, just the subclasses and each subclass will have what was the superclass PK as their PK along with the attributes inherited from the superclass and their own local attributes
	- can never be with partial
	- probably not good idea to be used when the parent has many attributes as each child table would have to repeat all the attributes
- **Option 8C- Single table with one attribute**- 
	- Single relation that has its attributes and all attributes of the superclass, plus all attributes of each of the subclasses and an attribute called 'type'
	- 'type' attribute is what identifies the subclass apart for each tuple. PK is the PK of the superclass
	- Option only works for specialisation whose subclasses are disjointed and has potential for generating many NULL values if many specific attributes exist in the subcasses
	- Does NOT work for overlapping specialisation where an entity can be multiple subclasses as the 'type' attribute would only have one value where it is an OR entity of the subclass
	- can never be with overlapping, use for disjoint and 8D for overlappying
- **Option 8D- Single table with multiple type attributres**- 
	- Create single relation with all attributes of superclass, plus attributes of each subclass, plus mutiple 'type' attributes. Each 'type' attribute is boolean indicating where tuple belongs to particular subclass
	- Option only works for specialisations whose subclasses are overlapping but can also work for disjointed specialisation as you can have a boolean for each subclass
	- The attributes would be boolean and representative of each subclass that the entity could be
	- Never use with disjoint, use 8C, use this for overlapping
How to choose which option to go with in step 8 of the transformation, good to remember these
	- If specialisation is oberlapping, cannot use 8C as the 'type' attribute cannot accomodate instances with more than one subclass
	- If specialisation is partial, cannot use 8B since partial specialisations might have instances at the superclass lbel that dont belong to any subclass. Does not create any superclass table which creates problems for any superclass lebvel instances
	- If alot of local attributes (attributes only at that subclass level) then going for the single table option (8C or 8D) might not be good because you would get a lot of NULL values (as they are referred to NULL if that tuiple instance is not related to the that specific subclass attributes)
	- If a lot of superclass attributes then not good idea to go wuith 8B as end up copying attributes across the subclass tables as well as if the superclass has relationships with other entities they need to be considered as well

- **IS-A test**- from the direction of the child to the parent ask if they are a a valid relationship from them to the parent, eg a parent Employee and subclass Salaried Employee- IS A Salaried Emploee AN EMployee, asnwer is YES so valid relationship then with the Employee as the parent and Salaried EMployee as Subclass because the EMployee could be Salaried or Hourly
	- Always asking the IS-A question from a child to parent in a union should always have response YES and from parent to child NO 
## Union Relationship
Having just the one superclass is where we have the **specialisation/generalisation** but when there is multiple superclasses that don't have any relation, but we want to create a subclass from multiple superclasses is called a **Union type/category**.
- Category member must exist in a least one of its superclasses
- Represented in the diagram by a 'U' inside the circle that connects the subclass with multiple superclasses (similar to 'd' or 'o' in specilisations)
- In a specialisation usually the subclasses would inherit the primary key from the superclass, while in the union that cannot happen as the superclasses would have their own unique keys that would cause confusion. Union create the surrogate key which is their own PK and put that PK as a FK in the superclasses

## Transformation of Union Step 9 types
- When the Union (Category) has superclasses with different keys, need to make a new key attribute called **surrogate key** when creating the relation corresponding to the union/categroy.
- Cannot use the defining keys from any of the subclasses because each one is different and cannot be used exclusively to identifiy all entities in the union
- The union/category becomes an entity with the surrogate key and the surrogate key becomes the FK in the defining superclasses
- If defining superclasses have the same key then that key becomes the PK of the union/category

## once finished wih step-9 then go step2-7 again to tidy up, rinse and repeat
Because in step 1 you are finding the regular entities (ones that dont have children) amd then once found cardinality, specialisation and union, there will be clearly entitites without children as the entities have been made, so repeat is important as the diagram has evolved from children entitties into regular entitities.
- After step 8 you find out about the cardinality and children because you are looking at those concepts
- So even if tghere is an entity that has a relationship for step 4, if it also has union or speiclicastion it cannot be done because it is not at that step yet, so this is why important t ogo through multiplte times as things clear up

## Final step of transformation
HAVE TO LIST THE FINAL TABLES
- must write down the whole procedure of transforming the tables to show steps, so its important to show the finbal tables as its the final product


# Chapter 14- Basics of Functional Dependencies and Normalization for Relational Databases
# Module 3- Normalisation and Data Manipulation using Relational Algebra
Two approaches to database deisgn- top-down (ER/EER diagram listed above) and bottom-up (normalisation)
Bottom-up uses user views and nomralisation of these user-views (user registration form, student enrolment form) to come up with relatonal tables

## Normalisation 
- **Normalisation**- process that produces set of relational tables that do not contain any problems (anomalies)
- Usually best for when there is not a text description of the businesses needs, can look at things like forms or some other sort of way that the data has prebviously been stored and described
- **user-view** is some sort of perspective that users have had when interacting with the companies data (filling out a form for something the company does eg filling a form to hire a care at a car hire shop- can see the important needed data on that form)
- **Normalisation steps**- 
	1. Represent all user views as a collection of relations (eg forms, reports)
	2. Normalise these relations, user view by user view
	3. Combine relations that have exactly the same primary keys

## Functional Dependencies
Relational tables have multiple attributes and the table itself is what creates the relation between each attribute
- **Functional dependency (FD)**- Expressed using a left-hand side, right-hand side and arrow. There can be multiple attributes on either side and these determine the importance of dependency. If there ar emultiple on the left hand side then that means to find out the right hand side attributes we must know the left hand side first. EmployeeID - > EMployeeName
	- This means that if there is an EmployeeId, there is an EmployeeName
	- This means that the EmployeeName is determined by the EmployeeId
	- This means that the EmployeeName is uniquely determined by the EmployeeeId
	- This means that he EmployeeName depends on the EmployeeId
	- It would not work if it was EmployeeName - > EmployeeID, because in any set of instances, the EmployeeName is not unique to be able to determine someones EmployeeId, while an EmployeeId is unique to then be able to identify the EmployeeName
	- EmployeeId determines the value of EmployeeName, the expression then is a **valid functional dependency**
	- Both EmployeeId and EmployeeName are made up of attributes in a **functional dependency** 
- Different types of functional dependencies
	- **Full Dependency**- The right hand side of the FD depends on the entire left hand side, all of the left hand side attributes need to be known to be able to know what the values iof the right hand side attributes are, eg LabTime, SubjetCode -> Tutor- here we need to know both LabTime AND SubjectCode to be able to determine what the value of the Tutor is
	- **Partial Dependency**- This is where the right hand side of the FD is only dependent on some of the valiues on the left hand side. eg LecturerId, SubjectCode -> LecturerName- we can know the LecturerName by ONLY knowing the LecturerId and not knowing the SubjectCode
	- **Transitive Dependency**- When you have two attributes and then a third intermediary attribute that links the two. If we want to find the Tutor and we have the lectureId but they are not related then eg LecturerId -> SubjetCode (need the LectureId to get SubjectCode) SubjectCode -> Tutor (Need the SubjectCode to get the Tutor) then transitively LecturerId -> Tutor (we can use the LceturerId to get the Tutor) = Tutor is transitively dependent on LecturerId

## Normalisation using Functional Dependencies (FDs)
Functional dependencies can be used to deicide whether a shcema is well designed, **anomalies** which are problems arise when poorly dfesigned data has queries on them
- **Insertion anomaly**- If there is an etity with an attribute that can be NULL but is also a primary key then this is an entity integrity constraint and an example of an **insertion anomaly** because trying to insert something that is NULL and a PK is invalid
- **Update anomaly**- If you are trying to update a specific value for a row but that value change doest change consistently if there are multiple rows with that same initial value then this is an **update anomaly**
- **Deletion anomaly**- If a row is deleted and it has a primary key as a foreihn key in aother row, then that row as well could be deleted which is a problem, this is a **deletion anomaly**

## Removal of anomlaies
Decomposing relations can remove anomalies to result into  **normal forms**
- **Major/main normal forms**- **First (1NF)**, **Second (2NF)**, **Third (3NF)** and **BoyceCodd (BCNF)**. 
- **Higher/advanced normal forms**- **Fourth (4NF)**, **Fifth (5NF)**
- Forms are increasingly strict (more errorfree), **advanced forms** are nased on more complex kinds of dependencies and functional dependencies
- Because 4NF and 5NF rarely have problems and industry don't need to worry about highest possible NF for practical reasons, just use 3NF and BCNF

## Normal Forms defined
Increasingle less errors as the number increases
- **Unnormalised form**- Put every available piece of information in that user-view into one single relation, this is **UNF**
- **First Normal Form**- 
	- Relation is 1NF only if there are no repeating groups (meaning that data is constantly repeated in columns eg item1, item2, item3 etc), have each row to determine the item, 
	- PK has been identified for the relation, 
	- all attributes are functionally dependent on the entire key, or part of the key.
	- Any row that doesnt have a PK violates 1NF. 
	- Cannot use row order to determine information
	- Mixing data types in a column is invalid
- **Second Normal FOrm**- 
	- A relation is 2NF if only the relation is in 1NF(already satisfies the requirements of the 1NF) 
	- and all non-key attributes are fully functionally dependent on the entire key (ie if there were any partial dependency in 1NF, its been removed (partial dependency is if the attribute can be recognised through only part of the primary keys)). 
	- If an attribute is not fully dependent (needs both PK to be recognised) then it will be removed into its own table
- **Third Normal Form**-
	- A relation is 3NF if the relation is in 2NF (satisfies all criteria of 2NF), all transitive dependencies on the PK have been removed (note to quickly identify transitive dependency in a relation is to look for functional dependencies between non-key attributes) so if a pair of attributes depend on each other and none of them are part of the key, they have a transitive dependency between them, and the dependence must be removed for table to be in 3NF
	- Move to a new table
	- Third Normal FOrm- Every non-key atribute should depend on the key
	- Boyce-Codd Normal Form- Every attribute in a table should depnd on the key
- **Remove dependency**- decompose a relation to multiple relations so the partial/transitive dependencies dont exit anymore in the new formed tables

## Normalisation Process
When normalising multiple user-views, focus on ONE user-view at a time and at the end combine the tables that have the same PK
1. Identifying UNF
	- **Unnormalised form**- all attributes in one relation that is in the user-view
	- **Repeating group**- when an instance of a relation can be repeated within a single isntance of an entity (a order number and customer number can then represent multiple orders (item, quantity, date) so therefore the orders are the repeating group). They are represented by being in brackets in the UNF- ORDER(ORder#, Customer#, CustpomerName, CustomerAddress, (DateOrdered, ProductName, Quantity))
	- Not a requirement to identify PK
2. Transform to 1NF
	- Have to remove the repeating group and identify the PK
	- So have two separate tables ORDER(<u>Order#</u>, Customer#, CustomerNae, CustomerAddress) and ORDER_PRODUCT(*<u>Order#</u>FK*, <u>Product#</u>, ProductName, Quantity)
	- So to remove the repeating group, have to create a new table and have the PK from the other table as the PK (along with the PK for new table) and FK
	- This is holding up referential integiry constraints as well as entity integrity constraints
	- Identify the **Insert**, **Updaet** and **Delete** anomaloies
3. Transform to 2NF
	- Need to make sure that all non-key attriutes are fully dependent on the entire key (could be two primary keys (composite))
	- If they are only dependent on one part of the key they are **partially dependent**
	- Need to create a new relation that consists of parts of the keys (which became the PK of the new relation) and all non-key attributes that are dependent on that partial key
	- Separating ORDER_PRODUCT(*<u>Order#</u>FK*, <u>Product#</u>, ProductName, Quantity) into two relations- PRODUCT(<u>*Product#*</u> , ProductName, price) ORDER_PRODUCT(<u>*Order#*</u>, <u>*Product#*</u>, Quantity)
	- The Product table now has the attributes that had dependency on Product# PK
	- Don't need to keep the attributes in multiple ables
	- If the table has one PK and the attributes are full-dependency on it then don't need to break it down more
4. Transform to 3NF
	- Cannot have transitive dependencies- where a non-key attribute is dependent on another non-key attribute
	- ORDER(<u>Order#</u>, Customer#, CustomerNae, CustomerAddress) changes into  new relation- CUSTOMER(<u>Customer#</u>, CustoerName, CustomerAddress) and ORDER(<u>Order#</u>, <u>*CustomerName*</u>, CustomerName, OrderDate)
	- So the Customer became a new relation and the Customer# will now be a PK and FK in the Order relation
	- CUSTOMER table now has the attributes that had dependency on CUstomer#
	- IMPORTANT to identify the non-key attributes that are related where one is needed to identify another (something like a code/number to identify a name/address etc) as this is transitive- create separate relation

# Data Manipulation Using Relational Algebra
Wanting to be able to get specific tuples from a row you need to build a query, relqational algebra is the maths behind the queries as the query needs to query a table or multiple tables to return information
Each operation (algebra operation forms a relational algebraic expression that also results in a relation) takes a relation (two relations sometimes) as input and produces a relation as output
**π Name (σ Suburb=’Bundoora’ (Student))**
This **expression** has two **operators** a **projection** (π) and **selection** (σ) and they take thje Student relation as the **input** and then gives back the **output** (which is also a relation (table))- so in this case it would return the relation with the column of Name with the Names as rows that match to the Suburb='Bundoora'
- **Set** in relational algebra is a table that has no values that are the same

## Relational Algebra Operations
- **Projection (π- pi)**- An operation that selects specified attributes from a relation, it is classified as a **Vertical subset** of a relation
	- English- Find the names of all the students from a database
	- Relational Algebra- πName(Student)
	- THe pi symbol is signifying that we are making a projection with the Name being the spot where you want the attributes you are choosing to return, with the table that you want the attributes to be selected from within the ()
	- **Projection** removes any duplicate tuples that are a result from the projection- HOWEVER if there are duplicate tuples within one attribute but the corresponding tuple has a different attribute as well, then both would return eg the **projection** πSubjectName, Course (Subject) outputs- (tuple1(Algebra, Maths) tuple2(Algebra, CompSci)) both would return if wanting to get the attribute SubjectName and Course, but if just wanting to get the SubjectName  then it would return (tuple1(Algebra)) because the tuple2 would be (Algebra) anmd thats a repeat from that relation
- **Selection (σ- sigma)**- An operation that is classified as a **Horizontal subset** of a relation, it implies creating a condition on which the returning tuple must be met to be returned
	- English- Select names that are equal to Ben from student database
	- Relational Algebra- σName = 'Ben'(Student)
	- This returns all the tuples that would have the attribute of Name equal to Ben, this returns all the attributes, eg (Name='Ben', age=27, course='Grad dip'), this returned the other attributes along with the Name as it is the whole tuple
	- Selection can also remove duplicates if every tuple in the two rows are exact same
- **Projection and Selection**- The  selection will identify the rows that match the condition and then the projection will identify the tuples value that have that attribute. It is important about order of operations, so expression in the brackets is performed first and then outside of brackets. 
	- English- Select the names of the students who suburb is Bundoora
	- Relational Algebra- πName(σSuburb='Bundoora'(Student))
	- So it will select rows that have the attribute of Suburb value as Bundoora and from those rows it will select the tuple value for the Name attribute and return the values
- **Union (U)**- Combining the tuples from one relation with another to produce a third relation, the two relations have to be compatible to do so. This is adding the first relation with the second relation when the columns are the same, the rows are being combined together, no duplicates.
	- **π SID (σ SNo=21 (Takes)) U π SID (σ SNo=29 (Takes))** 
	- Above in the first relation it gets the StudentNomber equal to 21 from the Takes table and then gets the SID of that tuple row, while in the second relation it gets the StudentNumber equal to 29 from the Takes relation and then gets the SID of that tuple row. The union then combines these two SID column rows together to form a relation that contains both of the SIDs
- **Intersection (∩)**- Where a third relation is created between an intersection of two other relations (that have to be compatible like a union), the third relation contains common tuples
	- Similar to the Union, in that it has two compativle relations, but the Intersection will find the common tuples and then the third relation will have the resulting similar tuples
	- **π SID (σ SNo=21 (Takes))** ∩ **π SID (σ SNo=23 (Takes))**
	- In above the relation1 will look for the SubjectNumber of 21 in the Takes relation and then gets the SIDs (1108, 8507) and the second relation looks for SUbjectNumber of 23 in Takes relation and gets the SIDs (1108) and then creating the intersection the third relation will just have the SID of 1108 because that is the common one between the two relations
- **Difference (-)**- Where the third relation is the difference between relation 1 and 2, so the tuples that occur in relation 1, but not in relation 2- they both must be union compatible (so matching attribute columns)
	- so if have Names(Ben, Andy, Kieran) in relation 1 and relation 2 Names(Andy, Justin, Kieran) then the third relation would be Names(Ben)
	- **π Name(σ Group='BigBoy'(FriendGroups))** - ** **π Name(σ Group='NotBig'(FriendGroups))** ** 
- **Cartesian Product (X)**- This is where every tuple from relation 1 is combined with the tuple from relation 2 even if they are not union compatible.
	- This causes a lot of useless data as combining relations together with every possible attribute combination makes no sense sometimes
	- Names(Ben, Andy, Kieran) and Numbers (1, 3, 5) = tuple1(Ben, 1) tuple2(Ben, 3) tuple3(Ben, 5) tuple4(Andy, 1) tuple5(Andy, 3) etc
- Join ([X]) - This joins the two relations together where there is a compatible column and provides all the tuples from both relations that are related to the condition
	- πName (σ Course = '113'(Enrol) [X] SID = ID Student )
	- This is first getting the tuples that have the Course = 113 in the Enrol table, and then joining that relation to the tuple in the Student table where the SID in the first relation is equal to the ID in the second relation of table Student, it has then all the tuples from both relations where the SID from table Enrol is matched with the ID ion table Student, it then looks for the Name in those tuples
	- Think of it like joining two tables together based on the common attribute and then having all the tuples from those two relations based on the condition, and then you can select the one attribute that you want or multiple
- **Outer Joines**- Similar to the natural join (above) but instead of listing all the matching tuples of the join condition, it will list both matched and unmatched- results in NULL values for unmatched
	- **Left Outer Join ([=X]) ** - Retains the unmatched tuples from left hand side relation of opoeratoer
	- **Right Outer Join ([X=])**- Retains the unmatched tuples from the right hand side relation of operatior
	- **Full Outer Join ([=X=])**- Retains unmatched tuples from both sides of the operator

