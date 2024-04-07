<?php // <--- do NOT put anything before this PHP tag

include('functions.php');

// get the cookieMessage, this must be done before any HTML is sent to the browser.
$cookieMessage = getCookieMessage();

?>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8" /> 
	<title>View Your Cart</title>
	<link rel="stylesheet" type="text/css" href="shopstyle.css" />
</head>
<body>
	<?php

	include('./Navigation.php');

    echo "<h1>Your Cart</h1>";

	// does the user have items in the shopping cart?
	if(isset($_COOKIE['ShoppingCart']) && $_COOKIE['ShoppingCart'] != '')
	{
		// the shopping cart cookie contains a list of productIDs separated by commas
		// we need to split this string into an array by exploding it.
		$productID_list = explode(",", $_COOKIE['ShoppingCart']);
		
		// remove any duplicate items from the cart. although this should never happen we 
		// must make absolutely sure because if we don't we might get a primary key violation.
		$productID_list = array_unique($productID_list);
		
		$dbh = connectToDatabase();

		// create a SQL statement to select the product and brand info about a given ProductID
		// this SQL statement will be very similar to the one in ViewProduct.php
		$statement = $dbh->prepare('SELECT P.*, B.* FROM Products P INNER JOIN Brands B ON B.BrandID = P.BrandID WHERE P.ProductID = ?');

		$totalPrice = 0;
		
		// loop over the productIDs that were in the shopping cart.
		foreach($productID_list as $productID)
		{
			// great thing about prepared statements is that we can use them multiple times.
			// bind the first question mark to the productID in the shopping cart.
			$statement->bindValue(1,$productID);
			$statement->execute();
			
			// did we find a match?
			if($row = $statement->fetch(PDO::FETCH_ASSOC))
			{				

                $ProductID = htmlspecialchars($row['ProductID'], ENT_QUOTES, 'UTF-8'); 
                $Price = htmlspecialchars($row['Price'], ENT_QUOTES, 'UTF-8'); 
                $Description = htmlspecialchars($row['Description'], ENT_QUOTES, 'UTF-8'); 
                $BrandName = htmlspecialchars($row['BrandName'], ENT_QUOTES, 'UTF-8'); 
                $BrandID = htmlspecialchars($row['BrandID'], ENT_QUOTES, 'UTF-8'); 
                
                // output the data in a div with a class of 'productBox' we can apply css to this class.
                echo "<div class = 'productBox'>";

                echo "<img src='../IFU_Assets/ProductPictures/$ProductID.jpg' />";
                echo "<img src='../IFU_Assets/BrandPictures/$BrandID.jpg' />";
                echo "<div style='display: flex; flex-direction: column;'>";
                echo "<h1>$BrandName</h1>";
                echo "<p style='font-weight: bold; font-size: 1.6rem;'>$Description</p>";
                echo "<p style='font-size: larger; font-weight: bold; color: blue;'>$$Price</p>";
                echo "</div>";
                echo "</div> \n";

                $totalPrice += $Price;
			}
		}


        echo "<p style='font-size: 2rem;'>Total: $$totalPrice</p>";
		
		// if we have any error messages echo them now.
		echo "<p style='color: red;'>$cookieMessage</p>";
		
		// you are allowed to stop and start the PHP tags so you don't need to use lots of echo statements.
		?>
			<form style='margin-bottom: 12px;' action = 'ProcessOrder.php' method = 'POST'>
			
                     <input type="text" name="UserName" placeholder="UserName..." />
			
				 <input type='submit' value='Confirm Order' name='BuyButton' />
			</form>
			
			<form action = 'EmptyCart.php' method = 'POST'>
			<input type = 'submit' name = 'EmptyCart' value = 'Empty Shopping Cart' id = 'EmptyCart' />
			</form>
		<?php 		
	}
	else
	{
		// if we have any error messages echo them now. 
		echo "<p style='color: red;'>$cookieMessage</p> <br/>";
		
		echo "You Have no items in your cart!";
	}
	?>
</body>
</html>
