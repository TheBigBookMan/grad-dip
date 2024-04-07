<!doctype html>
<html lang='en'>
<head>
	<meta charset="UTF-8" /> 
	<title>Product List</title>
	<link rel="stylesheet" type="text/css" href="./shopstyle.css" />
</head>
<body>
	<?php 
        include('./Navigation.php');
    ?>

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

        if (isset($_GET['sortby'])) {
            $sortBy = htmlspecialchars($_GET['sortby'], ENT_QUOTES,"UTF-8");
        } else {
            $sortBy = 'popularity';
        }

		$previousPage = $currentPage - 1;
		$nextPage = $currentPage + 1;

        $sqlSearchString = "%$searchString%";
		$safeSearchString = htmlspecialchars($searchString, ENT_QUOTES,"UTF-8");

        ?>
		
        <form action="./ProductList.php" method="GET" class="sort-by-container">
            <input type='text' name='search' value='<?php echo $safeSearchString ?>' />

            <label for="sortby">Sort By</label>
            <select name="sortby" id="sortby">
                <option value="popularity">Popularity</option>
                <option value="nameAscending">Name: A to Z</option>
                <option value="nameDescending">Name: Z to A</option>
                <option value="priceAscending">Price: Low to High</option>
                <option value="priceDescending">Price: High to Low</option>
            </select>
            <input type="submit" name="submit" value="Sort">
        </form>

        <?php
		// connect to the database using our function (and enable errors, etc)
		$dbh = connectToDatabase();

        if($sortBy === 'popularity') {
            $statement = $dbh->prepare('SELECT P.*, COUNT(OP.OrderID) FROM Products P LEFT JOIN OrderProducts OP ON P.ProductID = OP.ProductID  WHERE Description LIKE ? GROUP BY P.ProductID ORDER BY Count(OP.OrderID) DESC LIMIT 10 OFFSET ?;');

        } else if($sortBy === 'nameAscending'){
            $statement = $dbh->prepare('SELECT P.*, COUNT(OP.OrderID) FROM Products P LEFT JOIN OrderProducts OP ON P.ProductID = OP.ProductID  WHERE Description LIKE ? GROUP BY P.ProductID ORDER BY P.Description LIMIT 10 OFFSET ?;');

        } else if($sortBy === 'nameDescending') {
            $statement = $dbh->prepare('SELECT P.*, COUNT(OP.OrderID) FROM Products P LEFT JOIN OrderProducts OP ON P.ProductID = OP.ProductID  WHERE Description LIKE ? GROUP BY P.ProductID ORDER BY P.Description DESC LIMIT 10 OFFSET ?;');

        } else if($sortBy ===  'priceAscending') {
            $statement = $dbh->prepare('SELECT P.*, COUNT(OP.OrderID) FROM Products P LEFT JOIN OrderProducts OP ON P.ProductID = OP.ProductID  WHERE Description LIKE ? GROUP BY P.ProductID ORDER BY P.Price LIMIT 10 OFFSET ?;');

        } else if($sortBy ===  'priceDescending') {
            $statement = $dbh->prepare('SELECT P.*, COUNT(OP.OrderID) FROM Products P LEFT JOIN OrderProducts OP ON P.ProductID = OP.ProductID  WHERE Description LIKE ? GROUP BY P.ProductID ORDER BY P.Price DESC LIMIT 10 OFFSET ?;');

        } else {
            $statement = $dbh->prepare('SELECT P.*, COUNT(OP.OrderID) FROM Products P LEFT JOIN OrderProducts OP ON P.ProductID = OP.ProductID  WHERE Description LIKE ? GROUP BY P.ProductID ORDER BY Count(OP.OrderID) DESC LIMIT 10 OFFSET ?;');

        }

		// select all the products.

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
			echo "<a href='./ViewProduct.php?ProductID=$ProductID' ><img src='../IFU_Assets/ProductPictures/$ProductID.jpg' alt='product pic' /></a>";
            echo "<div style='display: flex; flex-direction: column;'>";
			echo "<p style='font-weight: bold; font-size: 1.6rem;'>$Description</p>";
			echo "<p style='font-size: larger; font-weight: bold; color: blue;'>$$Price</p>";
			echo "</div>";
			echo "</div> \n";			
		}
        echo "<div id='direct-page'>";
		echo "<a href='ProductList.php?page=$previousPage&search=$safeSearchString'>Previous Page</a>";
		echo "<a href='ProductList.php?page=$nextPage&search=$safeSearchString'>Next Page</a>";
        echo "</div>";
	?>
</body>
</html>