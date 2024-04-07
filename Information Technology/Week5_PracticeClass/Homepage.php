<?php // <--- do NOT put anything before this PHP tag
	include('functions.php');
	$cookieMessage = getCookieMessage();
?>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8" /> 
	<title>Bens Magnificent Shopping Centre</title>
	<link rel="stylesheet" type="text/css" href="shopstyle.css" />
</head>
<body>
	<?php 
        include('./Navigation.php');
    ?>
	<h1>Welcome to Bens Magnificent Shopping Centre</h1>
	<?php
		echo "<p style='color: blue;'>$cookieMessage</p>";
	?>
        <form action='./ProductList.php' method='GET'>
            <input type='text' name='search' placeholder="Search Shop..." />
            <input type='submit' />
        </form>
		
        <h2>Products Under $20!!!!</h2>
    <?php
        // ? Row of items below price of $20

        $dbh = connectToDatabase();
        $statement = $dbh->prepare('SELECT P.*, B.* FROM Products P
        INNER JOIN Brands B ON B.BrandID = P.BrandID
        WHERE Price < 20');
        $statement->execute();

        echo "<ul id='sales-box'>";

        while($row = $statement->fetch(PDO::FETCH_ASSOC)) {
            $ProductID = htmlspecialchars($row['ProductID'], ENT_QUOTES, 'UTF-8');
            $Description = htmlspecialchars($row['Description'], ENT_QUOTES, 'UTF-8');
            $Price = htmlspecialchars($row['Price'], ENT_QUOTES, 'UTF-8');
            $BrandName = htmlspecialchars($row['BrandName'], ENT_QUOTES, 'UTF-8');
            $Website = htmlspecialchars($row['Website'], ENT_QUOTES, 'UTF-8');

            echo "<li class = 'sales-item'>";
			echo "<a href='./ViewProduct.php?ProductID=$ProductID' ><img src='../IFU_Assets/ProductPictures/$ProductID.jpg' alt='Product pic' /></a>";
			echo "<p style='font-weight: bold;'>$BrandName</p>";
			echo "<p >$Description</p>";
			echo "<p style='font-weight: bold; color: blue;'>$$Price</p>";
			echo "<a href='$Website' target='_blank'><p>$Website</p></a>";
			echo "</li> \n";
        }

        echo "</ul>";
    ?>

    <h2>Our Most Popular Brands!!!</h2>
    <p>Measured by amount of products they have. Click on the brand to see the products they offer.</p>

    <?php
        // ? Brands with most products, can click on brand image to see list of products that brand offers

        $statement2 = $dbh->prepare('SELECT B.BrandName, B.BrandID,COUNT(P.BrandID) AS AmountProductsByBrand 
        FROM Products P
        INNER JOIN Brands B ON B.BrandID = P.BrandID
        GROUP BY P.BrandID
        ORDER BY AmountProductsByBrand DESC');
        $statement2->execute();

        echo "<ul id='brand-box'>";

        while($row2 = $statement2->fetch(PDO::FETCH_ASSOC)) {
            $BrandID = htmlspecialchars($row2['BrandID'], ENT_QUOTES, 'UTF-8');
            $BrandName = htmlspecialchars($row2['BrandName'], ENT_QUOTES, 'UTF-8');
            $AmountProductsByBrand = htmlspecialchars($row2['AmountProductsByBrand'], ENT_QUOTES, 'UTF-8');

            echo "<li class = 'sales-item'>";
			echo "<a href='./ViewBrandProducts.php?BrandID=$BrandID&BrandName=$BrandName'><img src='../IFU_Assets/BrandPictures/$BrandID.jpg' alt='brand pic' /></a>";
			echo "<p style='font-weight: bold;'>$BrandName</p>";
			echo "<p>$AmountProductsByBrand Products</p>";
			echo "</li> \n";
        }

        echo "</ul>";
    ?>

	
</body>
</html>