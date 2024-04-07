<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8" /> 
	<title>Brands Products</title>
	<link rel="stylesheet" type="text/css" href="./shopstyle.css" />
</head>
<body>
	
	<?php 
        include('./Navigation.php');
		
		// include some functions from another file.
		include('functions.php');
		
		// connect to the database using our function (and enable errors, etc)
		$dbh = connectToDatabase();
        
        if(isset($_GET['BrandID']) && isset($_GET['BrandName'])) {
            $BrandID = htmlspecialchars($_GET['BrandID'], ENT_QUOTES,"UTF-8");
            $BrandName = htmlspecialchars($_GET['BrandName'], ENT_QUOTES,"UTF-8");
            
            // select all the products.
            $statement = $dbh->prepare('SELECT * FROM Products WHERE BrandID = ?');
            
            $statement->bindValue(1, $BrandID);
            
            echo "<h1>$BrandName</h1>";
            
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
                echo "<a href='./ViewProduct.php?ProductID=$ProductID' ><img src='../IFU_Assets/ProductPictures/$ProductID.jpg' /></a>";
                echo "<div style='display: flex; flex-direction: column;'>";
                echo "<p style='font-weight: bold; font-size: 1.6rem;'>$Description</p>";
                echo "<p style='font-size: larger; font-weight: bold; color: blue;'>$$Price</p>";
                echo "</div>";
                echo "</div> \n";			
            }

        }
        ?>
</body>
</html>