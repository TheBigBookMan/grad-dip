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
IMPORTANT TO LOOK AT NOTES ON THE PICTURE AS THIS CAN HAVE AN INFLUENCE ON THE PROCESS
- **Unnormalised form**- Put every available piece of information in that user-view into one single relation, this is **UNF**
- **First Normal Form**- 
	- Relation is 1NF only if there are no repeating groups (meaning that data is constantly repeated in columns eg item1, item2, item3 etc), have each row to determine the item, - usually the repeating group will then have the PK of the table it was originally in as the FK PK in it- SAME AS 1:M relationship
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
	- If you find two non-key attributes and one is dependent on the other then that will be a transitive dependency and needs to be moved to a new relation
	- Move to a new table
	- Third Normal FOrm- Every non-key atribute should depend on the key
	- Boyce-Codd Normal Form- Every attribute in a table should depnd on the key
		- If an attribute that is non-key can also identify a key attribute then that breaks the boyce-codd normal form and to solve it you break the relation into two relations- one where the non-key (but has dependency) is the PK and the attribute that was the key (was dependend) and that becomes a non-key attribute. The PK in that new relation is now the FK and PK in the other relation with another key attribute
		- very rare to have this problem though
- **Remove dependency**- decompose a relation to multiple relations so the partial/transitive dependencies dont exit anymore in the new formed tables

## Normalisation Process
When normalising multiple user-views, focus on ONE user-view at a time and at the end combine the tables that have the same PK
- If multiple user-view,s treat each one separately when making the normal form process. Look for tables that have the same primary key and combine them into one table by getting the tbale with the most information
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
	- Sometimes dont need to create an extra table with both PK from the deprecated tables, can just have the PK of one in the other- look at the cardinality, if M:N then create the extra table if 1:M then the PK of the 1 as a FK in the M