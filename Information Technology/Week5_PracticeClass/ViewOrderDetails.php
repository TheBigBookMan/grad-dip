<!DOCTYPE HTML>
<html lang="en">
<head>
	<title>Order</title>
	<link rel="stylesheet" type="text/css" href="shopstyle.css" />
	<meta charset="UTF-8" /> 
</head>
<body>

<?php
    include("./Navigation.php");
// did the user provided an OrderID via the URL?
if(isset($_GET['OrderID']))
{
	$UnsafeOrderID = $_GET['OrderID'];
    $safeOrderID = htmlspecialchars($UnsafeOrderID, ENT_QUOTES,"UTF-8");
	
	include('functions.php');
	$dbh = connectToDatabase();
	
	// select the order details and customer details. (you need to use an INNER JOIN)
	// but only show the row WHERE the OrderID is equal to $UnsafeOrderID.
	$statement = $dbh->prepare('
		SELECT * 
		FROM Orders 
		INNER JOIN Customers ON Customers.CustomerID = Orders.CustomerID 
		WHERE OrderID = ? ; 
	');
	$statement->bindValue(1,$safeOrderID);
	$statement->execute();
	
	// did we get any results?
	if($row1 = $statement->fetch(PDO::FETCH_ASSOC))
	{
		// Output the Order Details.
		$FirstName = makeOutputSafe($row1['FirstName']); 
		$LastName = makeOutputSafe($row1['LastName']); 
		$OrderID = makeOutputSafe($row1['OrderID']); 
		$UserName = makeOutputSafe($row1['UserName']); 
		$Address = makeOutputSafe($row1['Address']); 
		$City = makeOutputSafe($row1['City']);
		$TimeStamp = date('Y-m-d H:i:s',makeOutputSafe($row1['TimeStamp']));
		
        $cookieMessage = getCookieMessage();
        echo "<h1 style='color: green;'>$cookieMessage</h1>";

		// display the OrderID
		echo "<h2>OrderID: $OrderID</h2>";

		// its up to you how the data is displayed on the page. I have used a table as an example.
		// the first two are done for you.
		echo "<table>";
		echo "<tr><th>UserName:</th><td>$UserName</td></tr>";
		echo "<tr><th>Customer Name:</th><td>$FirstName $LastName </td></tr>";
		echo "<tr><th>Address:</th><td>$Address</td></tr>";
		echo "<tr><th>City:</th><td>$City</td></tr>";
		echo "<tr><th>TimeStamp:</th><td>$TimeStamp</td></tr>";
		echo "</table>";
		
		// this will involve three tables: OrderProducts, Products and Brands.
		$statement2 = $dbh->prepare('
			SELECT OP.*, P.*, B.*
            FROM OrderProducts OP
            INNER JOIN Products P ON P.ProductID = OP.ProductID
            INNER JOIN Brands B ON B.BrandID = P.BrandID
			WHERE OP.OrderID = ? ; 
		');
		$statement2->bindValue(1,$safeOrderID);
		$statement2->execute();
		
		$totalPrice = 0;
		echo "<h2>Order Details:</h2>";
		
		// loop over the products in this order. 
		while($row2 = $statement2->fetch(PDO::FETCH_ASSOC))
		{
			//NOTE: pay close attention to the variable names.
			$ProductID = makeOutputSafe($row2['ProductID']); 
			$Description = makeOutputSafe($row2['Description']); 
			$BrandName = makeOutputSafe($row2['BrandName']); 
			$BrandID = makeOutputSafe($row2['BrandID']); 
			$Price = makeOutputSafe($row2['Price']); 
			$Quantity = makeOutputSafe($row2['Quantity']); 
			$Website = makeOutputSafe($row2['Website']); 
			
            echo "<div class='order-product'>";
            echo "<img src='./IFU_Assets/BrandPictures/$BrandID' />";
            echo "<a href='./ViewProduct.php?ProductID=$ProductID' ><img src='./IFU_Assets/ProductPictures/$ProductID' /></a>";
            echo "<div style='display: flex; flex-direction: column;'>";
            echo "<h2>$BrandName</h2>";
            echo "<h3>$Description</h3>";
            echo "<div style='display: flex; gap:4px;'>";
            echo "<p>$$Price - </p>";
            echo "<p>Quantity:$Quantity</p>";
            echo "</div>";
            echo "</div>";
            echo "</div>";
			
            $quantityAndPrice = $Price * $Quantity;
            $totalPrice += $quantityAndPrice;
		}		
		
        echo "<p style='font-weight: bolder; font-size: 2rem;'>Total Price: $$totalPrice</p>";
	}
	else 
	{
		echo "System Error: OrderID not found";
	}
}
else
{
	echo "System Error: OrderID was not provided";
}
?>
</body>
</html>
