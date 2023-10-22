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
1. **Mapping of regular entity types**- find the **strong entity types** (ones that have primary keys) and start to identify which key would be the primary- (may be an individual key or composite key). These are the main entities that represent the core conceptual objects in the database. Underline the primary key. Only add the simple attributes (no multivalue or composite etc). **NOT CHILD ENTITIES**, this is the reason why coming back to step 2 is important after step 9 because you have formed new regular entities by looking at cardinality, union, specilisation and coming back here is to find new entities. **ALSO DO THE PARENT ENTITIES OF SPECIALISATION/UNION** IF A PARENT IS A CHILD THEN IT IS NOT DONE UNTIL STEP 8
2. **Mapping of weak entity types**- the **weak entity types** (do not have keys) and find the relation, create the new relation primary key to be the **owner-entity type** and the partial key of the weak type (if it has one) (COMPOSITE KEY). IN SIMPLE Make the primary key of te weak entity also the foreign key from the owner-entity, so just making a new table of the weak entity and HAVE the PK from the owner-entity as PK FK and if the weak entity has a some sort of unique id have that as composite
3. **Mapping of binary 1:1 relationship types**- 3 possible approaches to create a 1:1 relationship type: Try and pick the side that would have more rows in the database as the one that will have their primary key as the FK as it will change way less rows than the other- ALWAYS GO FOR THE FOREIGN KEY APPROACH- LOOK AT TJHE PARTICIPATION, the total one has the PK of the non total as its FK
    1. **Foreign key approach**- the entity that is not dependent on the other entity will be chosen to have its main attributes as the relation attribute because it is not reliant on another entity for existence. Having the foreign keys in the relation. Entity that is total pariticipation indluces the foreign key which is the primary key of the other relation
    2. **Merged relation approach**- mergin the two entity types and the relationship into a single relation, would need both participants being total
    3. **Cross-refernce or relationship relation approach**- adding in the relationship relation as a third table that would have both primary keys of the other two relations to be as foreign keys within it
4. **Mapping of binary 1:N Relationship types**- 2 possible approaches to create a 1:N relationship type- ALWAYTS GO FOR THE FOREIGN KEY APPROACH MOST OF THE TIME
    1. **Foreign key approach**- add in the primary key of the entity that is going to have multiple instances, so for example if its an Employee that will have Shifts, have each primary key of the Employee as a foreign key in the Shift entity. Whatever is the Many (M) will have the primary key of the 1 in their foreign key
    2. **Relationship relation approach**- creating the third relation **relationship relation** and this has the foreign keys as the primary keys of the entities
5. **Mapping of binary M:N relationshiup types**- must use the **relationship relation/cross-reference option**- as the third relationship is the only possible way to store multiple instances of an entity comprising of two participating entitities. Have both relations primary keys as foreign keys within the relationship relation as well as the attributes. THe primary keys create a composite key as they are a combination of both primary keys and potentially if there is a unique attribute in the relationship this can also be a composite key PK
6. **Mapping of multivalued attributes**- when an attribute has multi values, create a new relation which will be the instance of that value, and make the primary key of the relation entity as the foreign key in the new relation
7. **Mapping of N-ary relationship types**- using the **relationship relation option**- this is where there are more than 2 entitities in a relationship and therefore will need a relationship relation whjich will store the primary keys of each entity as foreign keys and as the primary keys as all of these will be considered to make up the uniqueness of each entity (**composite key**) , if there isnt one of the other relation primary key then the relation fails. potentially if there is a unique attribute in the relationship this can also be a composite key PK

-   having the foreign key in the relation allows for a natural join (**EQUIJOIN**) of that sharing attribute from both entities, but then when there is a relationship entity it requires 2 joins for M:N as the relationship entity wil lrequired a join from both of the participating entitites and a N-ary relationship entity will have n joins as it will have to get all of the entitties to match the attribute of the foreign key

Step 1-7 is for ER and 8 and 9 are for EER
## Transformation of Specialisations in EER diagram
Transforming the diagram into the set of relational tables in step 8 of the transformation. Can have one of the 4 options from the **completedness** and the **disjointeed** constraits. 
This is for the children entities NOT the parent entities as they have been created before.
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

## Finding Cardinality
- **Union Cardinality**- when the entity is a relationship to itself (Person entity can be a parent to itself (parent and child are both Person)) and this would just look at (how many children can a parent have M, how many parents can a child have M)
- **Ternary Cardinality**- When there are three relations in the relationship, just use two to find the cardinality of the other one (do this for each relation of the ternary)- (Employee and Product- how many Customers can be served by the  Employee to buy the Product M, Product and Customer- how many Products can a Customer buy M, Customer and Employee- How many customers can be served by an employee M). 
- **Ternary Cardinality 1:1:M**- if there are two relations that are 1 cardinality then break down into two or three binary relationships to make it easier and ternary might not be the best answer
## Union Relationship
Having just the one superclass is where we have the **specialisation/generalisation** but when there is multiple superclasses that don't have any relation, but we want to create a subclass from multiple superclasses is called a **Union type/category**.
- Category member must exist in a least one of its superclasses
- Represented in the diagram by a 'U' inside the circle that connects the subclass with multiple superclasses (similar to 'd' or 'o' in specilisations)
- In a specialisation usually the subclasses would inherit the primary key from the superclass, while in the union that cannot happen as the superclasses would have their own unique keys that would cause confusion. Union create the surrogate key which is their own PK and put that PK as a FK in the superclasses
- Use over a specialisation when each of the superclasses has a unique ID 
- Also use when each of the superclasses can NOT be part of the child, so the IS-A rule

## Transformation of Union Step 9 types
- When the Union (Category) has superclasses with different keys, need to make a new key attribute called **surrogate key** when creating the relation corresponding to the union/categroy.
- Cannot use the defining keys from any of the subclasses because each one is different and cannot be used exclusively to identifiy all entities in the union
- The union/category becomes an entity with the surrogate key and the surrogate key becomes the FK in the defining superclasses- the entity owner create a PK (surrogatekey)- so something like EntityID and then that is FK in each of the superclasses
- If defining superclasses have the same key then that key becomes the PK of the union/category

## once finished wih step-9 then go step2-7 again to tidy up, rinse and repeat
Because in step 1 you are finding the regular entities (ones that dont have children) amd then once found cardinality, specialisation and union, there will be clearly entitites without children as the entities have been made, so repeat is important as the diagram has evolved from children entitties into regular entitities.
- After step 8 you find out about the cardinality and children because you are looking at those concepts
- So even if tghere is an entity that has a relationship for step 4, if it also has union or speiclicastion it cannot be done because it is not at that step yet, so this is why important t ogo through multiplte times as things clear up

## Final step of transformation
HAVE TO LIST THE FINAL TABLES
- must write down the whole procedure of transforming the tables to show steps, so its important to show the finbal tables as its the final product
