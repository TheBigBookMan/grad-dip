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
		
		if(isset($_GET['ProductID']))
		{		
			// connect to the database using our function (and enable errors, etc)
			$dbh = connectToDatabase();
            $productId = $_GET['ProductID'];
			
			// select all the products with the specified ID.
			$statement = $dbh->prepare('SELECT P.*, B.* FROM Products P INNER JOIN Brands B ON B.BrandID = P.BrandID WHERE P.ProductID = ?');
			
			// TODO: bind the value here
            $statement->bindValue(1, $productId);
			
			//execute the SQL.
			$statement->execute();

			// get the result, there will only ever be one product with a given ID (because products ids must be unique)
			// so we can just use an if() rather than a while()
			if($row = $statement->fetch(PDO::FETCH_ASSOC))
			{
                $description = htmlspecialchars($row['Description'], ENT_QUOTES, "UTF-8");
                $price = htmlspecialchars($row['Price'], ENT_QUOTES, "UTF-8");
                $brandName = htmlspecialchars($row['BrandName'], ENT_QUOTES, "UTF-8");
                $brandID = htmlspecialchars($row['BrandID'], ENT_QUOTES, "UTF-8");

				// display the details here.
                echo "<div>";
                echo "$description <br/>";
                echo "$price <br/>";
                echo "$brandName <br/>";
                echo "<img src='./IFU_Assets/ProductPictures/$productId.jpg' />";
                echo "<img src='./IFU_Assets/BrandPictures/$brandID.jpg' />";
                echo "</div>";
			}
			else
			{
				echo "Unknown Product ID";
			}
		}
		else
		{
			echo "No ProductID provided!";
		}
	?>
</body>
</html>