<!DOCTYPE html>
<html lang="EN">
<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Search Engine</title>
</head>

<body>

<center>
<form action"./results.php" method="get">
	<input type="text" name="input" size="50" <?php echo $_GET ['input'];?>/>

	<input type="submit" value="search" />

</form>
</center>

</body>
</html>