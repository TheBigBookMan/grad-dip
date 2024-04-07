<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="./shopstyle.css" />
    <title>Business Page</title>
</head>
<body>
    <?php 
        include('./Navigation.php');
        include("./functions.php");
    ?>

    <h1>Business Page</h1>

    <?php

        if(isset($_GET['page'])) {
            $currentPage = intval($_GET['page']);
        } else {
            $currentPage = 0;
        }

        $previousPage = $currentPage - 1;
		$nextPage = $currentPage + 1;

        // connect to the database using our function (and enable errors, etc)
		$dbh = connectToDatabase();

        $statement = $dbh->prepare('SELECT P.*, B.*, COUNT(OP.ProductID) AS ProductPopularity, SUM(OP.Quantity) AS ProductQuantity, (P.Price * SUM(OP.Quantity)) AS TotalProductRevenue FROM Products P
        INNER JOIN Brands B ON B.BrandID = P.BrandID
        INNER JOIN OrderProducts OP ON P.ProductID = OP.ProductID
        GROUP BY OP.ProductID
        ORDER BY TotalProductRevenue DESC
        LIMIT 30 OFFSET ?
        ');

        $statement->bindValue(1, $currentPage * 10);
        $statement->execute();

        echo "<table>";
        echo "<tr>";
        echo "<th>ProductID</th>";
        echo "<th>Description</th>";
        echo "<th>Price</th>";
        echo "<th>Brand Name</th>";
        echo "<th>Popularity</th>";
        echo "<th>Total Quantity</th>";
        echo "<th>Total Revenue</th>";
        echo "</tr>";

        while($row = $statement->fetch(PDO::FETCH_ASSOC)) {
            $ProductID = htmlspecialchars($row['ProductID']);
            $Description = htmlspecialchars($row['Description']);
            $Price = htmlspecialchars($row['Price']);
            $BrandName = htmlspecialchars($row['BrandName']);
            $ProductPopularity = htmlspecialchars($row['ProductPopularity']);
            $ProductQuantity = htmlspecialchars($row['ProductQuantity']);
            $TotalProductRevenue = htmlspecialchars($row['TotalProductRevenue']);

            echo "<tr>";
            echo "<td>$ProductID</td>";
            echo "<td>$Description</td>";
            echo "<td>$Price</td>";
            echo "<td>$BrandName</td>";
            echo "<td>$ProductPopularity</td>";
            echo "<td>$ProductQuantity</td>";
            echo "<td>$TotalProductRevenue</td>";
            echo "</tr>";
        }

        echo "</table>";

        echo "<div id='direct-page'>";
		echo "<a href='BusinessPage.php?page=$previousPage'>Previous Page</a>";
		echo "<a href='BusinessPage.php?page=$nextPage'>Next Page</a>";
        echo "</div>";
    
    ?>

</body>
</html>