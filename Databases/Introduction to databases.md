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