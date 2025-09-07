<?php

include "mysql.php";

$mysql_table = "graffiti";

$link = mysql_connect($mysql_server, $mysql_username, $mysql_password);
mysql_select_db($mysql_database);


	if ($_POST) {
	
		$wall = $_POST["wall"];
	
		if (!($name = $_POST["name"]))
			$name = "Anonymous Coward";
	
		if (!($text = $_POST["text"]))
			$text = "I have nothing to say";

                if (!($client_ip = $_SERVER["HTTP_X_REAL_IP"]))
                        $client_ip =  $_SERVER["REMOTE_ADDR"];
	
		$query = "INSERT INTO ". $mysql_table ." (`wall`,`name`,`text`,`client_ip`) VALUES ('$wall', '$name', '$text', '$client_ip');";
		if (!mysql_query($query))
			echo "Could not add line on to wall", exit;
			
	}
	
	print "<HTML>\n<HEAD><TITLE>Graffiti Wall</TITLE></HEAD>\n";
	print "<BODY BGCOLOR=000000 BACKGROUND='graphics/pback.jpg' TEXT=FFFFFF>\n";

	if (!$wall)
		$wall = $_GET["wall"];

	$query = "SELECT * FROM ". $mysql_table ." WHERE wall = '". $wall ."' ORDER by timestamp DESC";
	$result = mysql_query($query);
	$nr = mysql_num_rows($result);
	for($i = 1; $i <= $nr; $i++) {
		$row = mysql_fetch_object($result);
                print "On <TT>". $row->timestamp ."</TT>, ";
		print "<B>". $row->name ."</B> writes:<BR>\n";
		print "<PRE>". $row->text ."</PRE>\n<HR>\n";
	}
	mysql_close($link);
?>
</BODY>
</HTML>
