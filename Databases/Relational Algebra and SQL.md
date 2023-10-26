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

# Structured Query Language (SQL)
Standard language to perform CRUD with relational databases
Different DBMS use different versions of SQL (Mysql, postgresql, oracle) and this can be a bit difficult because some write their queries with diifferent syntax
- **Data Definition Language (DDL)**- Create tables with the proper structure
- **Create Table command**- "CREATE TABLE tableName
						(field1 dataType constraint check,
						field2 dataType constraint check,
						PRIMARY KEY (uniqueField),
						FOREIGN KEY(foreingField) REFERENCES associatedTable(foreginField)
						);"
	- **Constraint**- are checks for things like NOT NULL
	- **Check**- are more checks for specific conditions like cant be less than X number etc- basically give a **set** of values that the value for this data HAS TO BE- write like "gender VARCHAR2(10) CHECK (gender IN ('Male', 'Female', 'Other'))"- the IN basically means Male OR Female OR Other
	- **Foreign Key**- the foreign key (primary key from another table) the table with it as the PK has to have been created already so it can be referred in the new table and hold up referential integrity. Spelling of the FK can be different but it must reference the same spelling
	- **Primary Key**- WHen creating a composite key for the primary key in the CREATE TABLE command just need to have them together PRIMARY KEY (firstKey, secondKey)- same as FK if the PK is also a FK from another table that table MUST exist before this table using their FK as a PK for referential integrity
		- MUST MAKE THE PRIMARY KEYS NOT NULL CONSTRAINT SO IMPORTANT!!!

## Data Types
- **VARCHAR2**- basically a string max 4000 chars, you can set a limit VARCHAR(24)
	- VARCHAR2- the 2 NEED TO USE because VARCHAR has a limitation with nulls and empty strings MUST DO!!!!!!!
	- Must specify the length when using VARCHAR2
	- No trailing whitespaces so the length of the string will take up that amount based on amount of characters, so if you had VARCHAR(20) and the string was 'Ben' it would still take up 3 spaces
-  **Char**-  When have a very simple explanation like a singular character use **Char(1)** eg Gender(M, F, U, B)
	- Char would take up the amount specified so same example as above CHAR(20) and value is 'Ben' it would still take up 20 spaces 
- **NCHAR**- Supports 16 digit binary character codes, stuff for things like Japanese alphabet and other long things
- **LONG**- Store up to 2GB of variable length data
	- Each table cna only have ONE LONG field in the table
- **NUMBER**- Precision- number of digits on either side of the decimal point. Scale- number of digits on right side of the decimal point
	- Defined like variableName NUMBER (precision, scale)
	- **INTEGER**- whole number with no digits to the right so 0 scale so when identifying an integer number for the datatype it would be "variableName NUMBER (2)" where the 2 represents precision but no scale. Singular number in the bracket wll immediately be an integer. Writing NUMBER (2) means it can be 2 digits as a whole max so (99) is the maximum number that the Number can be because precision is 2 which is max amount of numbers in the number
	- **Fixed point numbers** The precision defines how many numbers are in the NUMBER and the scale defines where the split between the decimal will be with the number indicating how many on the right of the decimal, eg (7, 3) 7(precision) 3(scale) so 7 digits with 3 of those digits on the right of the decimal (9999.999)
	- **Floating Point numbers**- Precision and scale are omitted, contains a variable number of decimal places
- **DATE**- started 1/1/4712BC to 12/31/4712AD lel
	- default date DD-MON-YYYY (05-MAR-2016) different databases can have different default dates
	- can also store time values- default time format HH:MI:SS A.M.
	- If notime given on date insert the default value is 12:00:00 A.M.
	- If no date value is given when it is inserted the default date is first day of current moneth
	- the two queries to use for dates are to_date() and to_char()

## Integrity Constraints
- **Value constraints**- restricts data values that can be inserted into a field
	- Types- the CHECK condition- eg gender CHAR(1) CHECK((gender = 'M' OR (genfer = 'F')))- to make sure that any value going into the field of gender that is a CHAR of 1 length has to be either an M or an F
	- NOT NULL- specifiying that the field cannot be null when entering something name VARCHAR(30) NOT NULL

## Drop Commands
Deleting a table
- **Restrict**- specified then the table can only be dropped if it is not referenced by any other table
- **Cascade**- is specified then all references/dependents will also be dropped- like a domino effect where the table is dropped then wherever the PK was a FK it will be dropped in there as well (the FK will be dropped)
- **Recycle Bin**- SHOW RECYCLEBIN to see the recyclebin if you want to maybe bring the dropped tbale back to life
- **Retrieve table**- FLASHBACK TABLE tableName TO BEFORE DROP- brings the table back to life from the recyclebin
- **Delete table**- PURGE TABLE tableName- to permanently delete the table from the recycle bin

## Data Manipulation Language Statements (DML)
- **Insertion**- can do two different methods to insert
	- This is for when you are inbserting all the values into the table- 
		- "INSERT INTO tableName
			  VALUES (col1 value, col2 value etc...)"
	  - THis is for when inserting only some values into the table, the order of fields is relevant to the order of the values inserted so MAKE SURE IN ORDER, leaves the other fields as NULL if they are not added in the query=
		  - "INSERT INTO tableName (field1, field2)
			  VALUES (col1 value, col2 value etc...)"
- **Insertion with Date**- if inputting date data in that does NOT follow the formatted date 'dd-Mon-yyyy' and you want it to be a specific date format
	- **to_date()**- Takes a string and converts it into the DATE format to_date('01/01/2020', 'DD/MM/yyyy') first arg takes the date string and second arg is the format you want- "INSERT INTO E
								VALUES ('E1', to_date('01/01/2020', 'dd/mm/yyy'));"
	- **to_char()**- the opposite of the to_date where it turns a date into a string "SELECT DOB FROM tableName WHERE field = 'condition'" it would return the date in the default format but if you want to get a specific part of the date like the month you could use to_char(). to_char(DOB, 'Mon') fuirst arg is the field and second is the format (this case is name of month)
- **Select**- "SELECT attribute FROM tableName WHERE attribute = 'condition';"
	- Many **operators** to determine the WHERE clause condition-
		- = equals
		- < less than
		- > greater than
		- <= less than or equals
		- >= greater than or equals
		- <> not equal to
		- LIKE wildcard- can say you want a specific match of something so can say '%en%' this means any values that contains the substring of 'en' with as many chars on either side- 'r%' means must begin with r and '%i' means must end in i- WHERE firstName LIKE '%en%'- return rows where firstname has the 'en' in the name- case sensitive
			- also has NOT LIKE '%k%'- meaning no character can be a k- inverse of the wildcard
		- IN test for in an enumerated list- WHERE deptName IN ('Comp Sci, Physicas') so it has to be in those values- can do NOT IN as well so its the inverse
		- OR becomes an either condition- WHERE name = 'ben' OR name = 'adam'; name can be either adam or ben
		- AND same as OR but returns both of the rows that match the values- WHERE firstname = 'ben' and lastname = 'gary'- get the 2 rows where one has firstname of ben and the row of lastname equal to gary
	- SQL does not remove duplicates, can explicitly ask to remove- SELECT DISTINCT employee WHERE firstname= 'ben'-
	- **Order by**- SELECT employeNo, LastName FROM Employee ORDER BY LastName- orders the return values to have descending (defualt ascending) and DESC at end of query
	- **ALias**- using AS as a alias so can rename whatever you are doing, if making a count can say COUNT(\*\) AS total_thing 
	- **No Grouping**- **Aggregate function**- 
		- **count**- returns the number of rows- SELECT count(\*\) FROM Employee, the \*\ returns all the rows, can do SELECT count(deptNum) FROM EMployee- this stil lreturns same amount because it would be same amount of rows, unless the value is empty then that row will not be returned-  the * as the parameter will return ANY row that iexists while if you put in a parameter it will count the row if the value is NOT NULL
	- **Grouping**- Group By-
		- **Group by**- SELECT deptNum, count(\*\) FROM EMployee GROUP BY deptNumber"- this will return the number of groups based on the condition, so for each deptNumber that a row shares that will count for that number group and it will return a table that has the deptNumber name and the number of instances it has- THIS wih count essentially will count the amount of rows that are matching within a specific attribute and then group them into groups of the matching value
		- **Having group by**- SELECT deptNumber, count(\*\) FROM EMployee GROUP BY deptNumber HAVING count(\*\)>2; so this will return whatever group has more count numbers than 2, so its kind of the WHERE clause for the returned value table of the counts, WHERE clause targets individual rows, where HAVING targets groups- can combine both to really restrict down what searching for- WHERE clause saying which rows will be counted based on the condition and HAVING determines which group will be returned back based on the condition- adds on to the GROUP BY by creating another clause to the result you want back matching a condition-- filtering the groups
		- **Aggregate function**- Have these to create new columns with **Aliases**- work well with the **grouping**
			- **Sum**- Returns the sum of the values in a specified column (numeric column)- like a total amount
			- **Min**- returns the min value in a specified column
			- **Max**- returns the max value from specified column
			- **Avg**- returns the average of the values in specified column
- **Nested Queries/Subqueries**-
	- SQL statement embedded within another SELECT statement- the result of the inner SELECT statement is used in the outer statement to help determine the contents of the final result
	- If using a nested query and there is an **alias** in the outer query, it can still be referenced within the nested query
		- **subquery with equality**- "SELECT firstName, lastName 
			FROM Employee 
			WHERE deptNum = 
				(SELECT deptNum 
				From Department
				WHERE mailNum = 30)"
		- It's like finding a value that you wouldnt know, but you know the condition in the WHERE close for the inner statement which will give you the result to then be able to select in the outer query
		- **subquery with IN**- using the IN instead of = to find a nested value if it is a member of a set--- better than equality when you have a set of valiues that you want it to be
		- **subquery with aggregate function**- can use an aggregrate function as the subquery to be able to find the specific value in the nested query- like count or sum etc
- **Joins**- Multi table queries when joining the attributes together
	- **Simple join**- Use a **prefix** to signify the table that you want that specific attribute to be from and then signify which attributes are mataching up
		- "SELECT E.firstName, E.lastName, D.deptName 
			FROM EMployee E, Department D
			WHERE E.deptName = D.deptName";
			- THis is choosing the attributes firstName and lastName from the Employee tanble and the attribute deptName from Department table and they are joined by the Department attribute deptName to the FK in the Emaployee as deptName
			- **aliases**- GOOD TO DO
		- Simple join returns every row and attribute back selected from the two tables, no row will be brought back if it isnt matching to the other
	- **Left outer join**- considers all the rows on the left hand side even if they are not matched
	- **right outer join**- consders all the rows on the right hand side even if they are not matched
	- **full outer join**- considers all the rows even if they are not matched
	- IMPLEMENTING THE outer joines- in Oracle put a plus on the opposire side that you want to join for the value---- suss online when doing
	- **Multi join query**- joining multiple tables- used for when joining a M:N relationships where a new table was created to pair two tables together who dont have the PK and FK in each other but in the third table
		- "SELECT E.firstName, E.lastName, P.projTitle
			FROM EMployee E, Works_On W, Project P
			WHERE E.employeeNo = W.employeeNo
			AND W.projNo = P.projNo"
		- See how the Works_On W is the middle man to merge the other two teogether by matching them up
- **Exists**- Used with nested queries- this returns true if there exists atleast one row in te result table returned by the subquery, it is false if it returns an empty table- NEED TO LEARN THIS BETTER
- **Union**- having a relation in one side with Union in the middle and another relation on the other side-- related to the relational algebra that they must have corresponding attributes for both relations and must be union compatible.
	- EACH UNION CALL AUTOMATICALLY REMOVES DUPLICATES
	- It will return all the rows combined as a set of both tables (3 from employee and 5 from dependent and it will return 8 rows)- this is only though because the attributes trying to get from each would return them- "SELECT employeeNo, firstName, lastName FROM EMployee UNION SELECT employeeNo, firstName, lastName from Dependent"--- both tables have the exact same attributes
	- **UNION ALL**- forcing the duplicates not to be removed
- **Intersect**- the query is structured the same as the union but with the INTERSECT in the middle instead of UNION
	- Returns the common attribute between the two tables- UNION returns the combination- returns the common ones in a set
- **Difference**- Using the same but with MINUS in the middle of the two relations
	- Returns the attributes that are not present in the second relation that are present in the first relation
- **Update**- Update a value in a column of a row, can update one row at a time but update multiple values in one query
	- "UPDATE Employee
		  SET firstName = 'Benjamin', lastName = 'SMeeeerd'
		  WHERE employeeNo = '1020';"
	- Dont need the WHERE clause but if dont use it then it will update EVERY Row with that specific value
-  **Delete**- can delete multiple records if the search condition specifies multiple records, if search condition omitted then all table records deleted
	- "DELETE FROM tblName
			WHERE condition = 'value'"
- **Views**- A virutal table that is derived from other existing tables
	- mainly built so it can be used for quick reference of things you need to see frequently, it doesnt actually have records and isnt a stored piece of the database, just VIRTUAL
	-  "CREATE VIEW name (attribute names)
		AS 
		SELECT statement"
	- Can have any sort of operators for the select statement as it is any usual SQL query that is being selected to be the view--- so any sort of table or anything you want will then be a virtual query
	- Handy to keep complex queries ready to go rather than constantly having to write the query--- HANDY
	- Can also control the access for a user by creating the query with spefic things to return and this can make it easy for specific users to see certain things without having to keep writing new queries
- **Query by example**- Query ois defined byu filling in a template
	- Basically a template of what rows you want to see and can put in names that you want to return for specific columns- set out like the table you want to return basically

## Using APEX Oracle
- Create tables
- can describe tables to show info- DESCRIBE tblName
	- Use the Object Browser functionality in the APEX as it is quick and shows the information

# Week 5- SQL Applied Practice and Basic PL/SQL
- PL- procedural language programming in sql
	- Will have a DECLARE space that starts with the DECLARE word- declare any local variables we want to be computed in the task
	- program body begins with BEGIN and ends with END- where the body code will be executed. after END need ; and /
	- Cannot use DDL (CREATE TABLE etc) but can use DML (SEELCT, inSERT etc) in the body
	- THe point is to create a procedural function that will do things with the data and do a specific execution like print
	- "declare
			v_age NUMBER(2);
			v_name VARCHAR(20);
			v_city CHAR(3);
		body
			SELECT first_name
			INTO v_name
			FROM STUDENT
			WHERE student_id = '101';

			DBMS_OUTPUR.PUT_LINE(v_firstName || 'is a good boyy')
		end;
		/"
	- adding in the INTO v_name is storing the returned value from the SQL statement into that variable
	- DBMS_OUTPUT.PUT_LINE('message here') is the console.log for it and use || to concatenate variables/string
- **Local variables**- classic variables to be able to make some sort of functionality on it
	- **simple variables**- regular variables that store one single value at a time- BEST TO DECLARE THE TYPE WITH THE ANCHORED TYPE INCASE OF ANY CHANGE IN THE TABLE ATTRIBUTE TYPE SO IT CAN DYNAMICALLY CHANGE
		- has types so var_age NUMBER;
		- acnhored data type- uses the data type of a specific column from a table- "var_age TBLNAME.attribute%TYPE;"
		- assigning a variable uses := so var_age:=24;
	- **cursor variable**- for when you want multiple values, and multiple cant be stored in a simple variable. Cursor stores multiple values- a collection of data
		- in the declare block- "Cursor studentNames is
							SELECT firstName, lastName 
							FROM Student
							WHERE Department = 'COmps cioence';"
		- THis will put the values of the select statement in the devlare block it will store them values into the cursor variable
		- Cursor has a loop-
			- In the body part- "for student IN studentNames loop
				 student.firstName
			end loop;"
			- very basic loop, kida like a python loop
	- Need to put the ouput for SQL on if the output isnt printing anything by using- SQL> SET SERVEROUTPUT ON;
- **If-THEN-ELSE statement**- standard IF-ELSE statement
	- "IF variable < 50 THEN
		v_newthing :=20;
		ELSE
			v_newthing:=10;
		END IF;"
	- get errprs if things fail
- **looping**- create basically a while loop (LOOP)-
	- "Begin
		LOOP
			code here
		END LOOP
	END;"
- Can make a while loop as well which would be more based on a condition to stop
- Can put a statement like INSERT with the variable to be assigned as the insert attribute value based on conditions or whatever

## Stored Procedures and Stored Functions
- **Stored procedure**- the prcoedure is stored in the database and persistent so if you leave the application and come back it will still be there
	- GRoups a set of SQL statements and it can accept parameters, perform operations and return to the caller, need to encapsulate the statement into the stored procedure
	- Same syntax as the PL but it replaces the DECLARE block
	- Need to have the parameters as anchored types
	- "CREATE OR REPLACE PROCEDURE procdeureName(
			p_ID TABLENAME.attribute%TYPE,
			p_firstName TABLENAME.first_name%TYPE,
			) AS"
	- And then have the other variable declaration in this blcok before the BEGIN block starts
	- Have the logic- so the logic is the functionality of the procedure so could be an insert, so this block takes the parameters from abocve and then put the parameters into the INSERT query then END tableName; 
		/
	- That slash is the end of the command IMPORTANT
	- To call the procudre do "EXECUTE procedureName(arguements);"
	- Basically a function but you will have SQL queries in the BEGIN -end block
	- LEAVE MODE DONT REALLY NEED TO USE IN THIS COURSE
	- optionally add in a **MODE**- default is IN OUT but can have IN or OUT or IN OUT- this goes next to the parameter name and type- "p_ID modehere TABLENAME.attribute%TYPE"
		- If it is IN then you cannot write to it only read the parameter, so can assign another variable to the variable with IN mode and work on that newly assigned variable but NOT on the one that was brought in through the parameter. Cannot assign the variable to somehint else
		- If it is OUT, you can write to it but cannot read from it, so you can assign it to other value but cannot assign a variable to it as reading it
		- IN OUT is allowing to do both to it
	- **Exception**- within the BEGIN-END body after the logic section at the end of it- This is like a fall back functionality if the code block before doesnt work-- KINDA LIKE A TRY/CATCH BLOCK- so once making some sort of statement like SELECT/INSERT/UPDATE and it doesnt work then the EXCEPTION block will execute
		- good idea if the data doesnt exist to then insert the data