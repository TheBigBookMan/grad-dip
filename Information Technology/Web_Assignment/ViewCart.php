<?php // <--- do NOT put anything before this PHP tag

include('functions.php');

// get the cookieMessage, this must be done before any HTML is sent to the browser.
$cookieMessage = getCookieMessage();

?>
<!doctype html>
<html>
<head>
	<meta charset="UTF-8" /> 
	<title>TODO put title here</title>
	<link rel="stylesheet" type="text/css" href="shopstyle.css" />
</head>
<body>
	<?php

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
		$statement = $dbh->prepare('
			
			--TODO PUT YOUR SQL HERE--
			
		');

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
				//TODO Output information about the product. including pictures, description, brand etc.				
				//TODO add the price of this item to the $totalPrice
			}
		}

		// TODO: output the $totalPrice.
		
		// if we have any error messages echo them now. TODO style this message so that it is noticeable.
		echo "$cookieMessage";
		
		// you are allowed to stop and start the PHP tags so you don't need to use lots of echo statements.
		?>
			<form action = 'ProcessOrder.php' method = 'POST'>
			
				<!-- TODO put a text input here so the user can type in their UserName.
					 this input tag MUST have its name attribute set to 'UserName' -->
			
				<!-- TODO put a submit button so the user can submit the form -->
				 
			</form>
			
			<form action = 'EmptyCart.php' method = 'POST'>
			<input type = 'submit' name = 'EmptyCart' value = 'Empty Shopping Cart' id = 'EmptyCart' />
			</form>
		<?php 		
	}
	else
	{
		// if we have any error messages echo them now. TODO style this message so that it is noticeable.
		echo "$cookieMessage <br/>";
		
		echo "You Have no items in your cart!";
	}
	?>
</body>
</html>
