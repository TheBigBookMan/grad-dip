<!doctype html>
<html>
<head>
	<meta charset="UTF-8" /> 
	<title>My First SQL Page</title>
	<link rel="stylesheet" type="text/css" href="shopstyle.css" />
</head>
<body>
	<h1>Products List</h1>
	<?php 
		
		// include some functions from another file.
		include('functions.php');

        if(isset($_GET['search'])) {
            $searchString = $_GET['search'];
        } else {
            $searchString = '';
        }

        if(isset($_GET['page'])) {
            $currentPage = intval($_GET['page']);
        } else {
            $currentPage = 0;
        }

        $nextPage = $currentPage + 1;

        $sqlSearchString = "%$searchString%";

        echo "<form>";
        echo "<input type='text' name='search' />";
        echo "<input type='submit' />";
        echo "</form>";
		
		// connect to the database using our function (and enable errors, etc)
		$dbh = connectToDatabase();
		
		// select all the products.
		$statement = $dbh->prepare('SELECT P.*, COUNT(OP.OrderID) FROM Products P LEFT JOIN OrderProducts OP ON P.ProductID = OP.ProductID  WHERE Description GROUP BY P.ProductID LIKE ? LIMIT 10 OFFSET ?;');

        $statement->bindValue(1, $sqlSearchString);
        $statement->bindValue(2, $currentPage * 10);
		
		//execute the SQL.
		$statement->execute();

		// get the results
		while($row = $statement->fetch(PDO::FETCH_ASSOC))
		{
			// Remember that the data in the database could be untrusted data. 
			// so we need to escape the data to make sure its free of evil XSS code.
			$ProductID = htmlspecialchars($row['ProductID'], ENT_QUOTES, 'UTF-8'); 
			$Price = htmlspecialchars($row['Price'], ENT_QUOTES, 'UTF-8'); 
			$Description = htmlspecialchars($row['Description'], ENT_QUOTES, 'UTF-8'); 
			
			// output the data in a div with a class of 'productBox' we can apply css to this class.
			echo "<div class = 'productBox'>";
			// [Put Task 5A here]  
            echo "<a href='./ViewProduct.php?ProductID=$ProductId' ><img src='./IFU_Assets/ProductPictures/$ProductId.jpg' /></a>";
			echo "$Description <br/>";
			echo "$Price <br/>";
			echo "</div> \n";			
		}
        echo "<a href='ProductList.php?page=$nextPage'>Next Page</a>'";
	?>
</body>
</html>