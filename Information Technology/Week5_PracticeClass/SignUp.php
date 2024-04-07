<?php // <--- do NOT put anything before this PHP tag
	include('functions.php');
	$cookieMessage = getCookieMessage();
?>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8" /> 
	<title>Sign Up Page</title>
	<link rel="stylesheet" type="text/css" href="shopstyle.css" />
</head>
<body>
	<?php 
        include('./Navigation.php');
    	?>
	<h1>Sign Up!</h1>
	<?php
		echo $cookieMessage;
	?>
	
	<form action = 'AddNewCustomer.php' method = 'POST'>

        <fieldset style='display:flex; flex-direction: column; gap: 8px;'>
            <label for='UserName'>UserName:</label>
            <input required type='text' id='UserName' name='UserName' placeholder="Enter UserName" />

            <label for='FirstName'>FirstName:</label>
            <input required type='text' id='FirstName'  name='FirstName' placeholder="Enter FirstName" />

            <label for='LastName'>LastName:</label>
            <input required type='text' id='LastName'  name='LastName' placeholder="Enter LastName" />

            <label for='Address'>Address:</label>
            <input required type='text' id='Address'  name='Address' placeholder="Enter Address" />

            <label for='City'>City:</label>
            <input required type='text' id='City'  name='City' placeholder="Enter City" />
        </fieldset>

        <input type='submit' value='Sign Up'/>
	</form>
	
</body>
</html>