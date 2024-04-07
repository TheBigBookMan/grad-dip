<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8" /> 
	<title>Order List</title>
	<link rel="stylesheet" type="text/css" href="./shopstyle.css" />
</head>
<body>

    <?php
        include('./Navigation.php');
    ?>
    <h1>Order List</h1>
    <?php

        include("./functions.php");

        // ? Connect to database
        $dbh = connectToDatabase();
        $statement = $dbh->prepare("SELECT C.*, O.* FROM Customers C INNER JOIN Orders O ON O.CustomerID = C.CustomerID;");
        $statement->execute();

        echo "<table>";
        echo "<tr>";
        echo "<th>OrderID</th>";
        echo "<th>TimeStamp</th>";
        echo "<th>CustomerID</th>";
        echo "<th>Username</th>";
        echo "<th>FirstName</th>";
        echo "<th>LastName</th>";
        echo "<th>Address</th>";
        echo "<th>City</th>";
        echo "</tr>";

        // ? Loop through each row returned from database call and echo out table row with customer information
        while($row = $statement->fetch(PDO::FETCH_ASSOC)) {
            $orderID = htmlspecialchars($row['OrderID']);
            $timestamp = date('Y-m-d H:i:s', htmlspecialchars($row['TimeStamp']));
            $customerID = htmlspecialchars($row['CustomerID']);
            $username = htmlspecialchars($row['UserName']);
            $firstName = htmlspecialchars($row['FirstName']);
            $lastName = htmlspecialchars($row['LastName']);
            $address = htmlspecialchars($row['Address']);
            $city = htmlspecialchars($row['City']);

            echo "<tr>";
            echo "<td><a href='./ViewOrderDetails.php?OrderID=$orderID'>$orderID</a></td>";
            echo "<td>$timestamp</td>";
            echo "<td>$customerID</td>";
            echo "<td>$username</td>";
            echo "<td>$firstName</td>";
            echo "<td>$lastName</td>";
            echo "<td>$address</td>";
            echo "<td>$city</td>";
            echo "</tr>";

        }

        echo "</table>";
    ?>

</body>
</html>
