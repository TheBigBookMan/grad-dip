<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8" /> 
	<title>My First SQL Page</title>
	<link rel="stylesheet" type="text/css" href="shopstyle.css" />
</head>
<body>
	<!-- <h1>Products List</h1> -->
	<?php 
		include("./Navigation.php");

		// include some functions from another file.
		include('functions.php');
		
		if(isset($_GET['ProductID']))
		{		
			// connect to the database using our function (and enable errors, etc)
			$dbh = connectToDatabase();
            $productId = $_GET['ProductID'];
			
			// select all the products with the specified ID.
			$statement = $dbh->prepare('SELECT P.*, B.* FROM Products P INNER JOIN Brands B ON B.BrandID = P.BrandID WHERE P.ProductID = ?');
			
            $statement->bindValue(1, $productId);
			
			//execute the SQL.
			$statement->execute();

            $addToCart = true;

            // ? Check if current productID is in cookie and show add to cart button
            if(isset($_COOKIE['ShoppingCart']) && $_COOKIE['ShoppingCart'] != ""){

                $cookies = explode(',', $_COOKIE['ShoppingCart']);

                if(in_array($productId, $cookies)) {
                    $addToCart = false;
                } 
            }


            if($addToCart) {
                echo "<form method='POST' action='./AddToCart.php?ProductID=$productId'>";
                echo "<input type='submit' name='BuyButton' id='add-to-cart' value='Buy Now' />";
                echo "</form>";
            }

			// get the result, there will only ever be one product with a given ID (because products ids must be unique)
			// so we can just use an if() rather than a while()
			if($row = $statement->fetch(PDO::FETCH_ASSOC))
			{
                $description = htmlspecialchars($row['Description'], ENT_QUOTES, "UTF-8");
                $price = htmlspecialchars($row['Price'], ENT_QUOTES, "UTF-8");
                $brandName = htmlspecialchars($row['BrandName'], ENT_QUOTES, "UTF-8");
                $brandID = htmlspecialchars($row['BrandID'], ENT_QUOTES, "UTF-8");
                $website = htmlspecialchars($row['Website'], ENT_QUOTES, "UTF-8");

				// display the details here.
                echo "<div id='product-item'>";
                echo "<p style='font-weight: bold; font-size: 1.8rem; color: blue;'>$brandName</p>";
                echo "<p style='font-weight: bold;'>$description</p>";
                echo "<p>$$price</p>";
                echo "<a href='$website' target='_blank'>$website</a>";
                echo "<img src='../IFU_Assets/ProductPictures/$productId.jpg' width='240px' />";
                echo "<img src='../IFU_Assets/BrandPictures/$brandID.jpg' width='240px' />";
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