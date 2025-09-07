<?php

	// MySQL Server Information
	$mysql_server = "tarbash.dotstermysql.com";
	$mysql_database = "db1128519_primus";
	$mysql_table = "polls";
	$mysql_username = "u1128519_primus";
	$mysql_password = "dingdang";

	// Open MySQL Connection & Select DB
	$link = mysql_connect($mysql_server, $mysql_username, $mysql_password);
	if (!$link)
		print "Connection to MySQL server failed.\n";
		
	mysql_select_db($mysql_database);

	// Form the Query
	$query = "SELECT * FROM $mysql_table";

	// See if it succeeded
	$result = mysql_query($query);
	if ($result != NULL) {
		$n = mysql_num_rows($result);
		if ($n > 0)
			print "There were $n rows found in the table!\n";
		else			
				print "Table appears to be empty.";
	} else
			print "The query '". $query ."' did not succeed.\n";

	mysql_close($link);

?>
