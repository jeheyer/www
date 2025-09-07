<HTML>
<HEAD><TITLE>Trivia Results</TITLE>
<BODY BGCOLOR="000000" BACKGROUND="graphics/bastards.jpg" TEXT="FFFFFF" LINK="CC6600" VLINK="996600" ALINK="CC0033">
<?php

  include "mysql.php";
  
	$mysql_table = "trivia";
	
	$link = mysql_connect($mysql_server, $mysql_username, $mysql_password);
	$db = mysql_select_db($mysql_database);
	if (!$link || !$db) { die ('MySQL error: ' . mysql_error()); }

	$query = "SELECT question_num, correct_choice FROM $mysql_table";
	$result = mysql_query($query);
	$nr = mysql_num_rows($result);

	$score = 0;
	for($i = 1; $i <= $nr; $i++) {

		$answer = $HTTP_POST_VARS["$i"];

		$row = mysql_fetch_object($result);
		if ($answer == $row->correct_choice)
			$score++;
		else {
			if (!$numwrong)
				print "You answered the following questions incorrectly:<BR>\n";
			print "<P>". $row->question_num .") ". $row->choice_text ."?</P>";
			$numwrong++;
		}
	}
	mysql_close($link);

	print "<H2>Your Score: $score / $nr</H2>\n";

	if ($numwrong > 0)
		print "(Total of $numwrong Wrong)\n<HR>\n";
	else
		print "Congratulations!!! You are Mr. Knowitall!";
?>
</BODY>
</HTML>
