<HTML>
<HEAD><TITLE>Trivia Game</TITLE>
	<META NAME="author" CONTENT="J Five Internet Solutions - http://www.jfive.com">
	<META NAME="generator" CONTENT="UltraEdit 32 Text Editor">
</HEAD>
<BODY BGCOLOR="000000" BACKGROUND="graphics/bastards.jpg" TEXT="FFFFFF" LINK="CC6600" VLINK="996600" ALINK="CC0033">

<H4 ALIGN=CENTER><TT>John the Fisherman's</TT></H4>
<CENTER><IMG SRC="pictures/johnfish.gif" ALT=""></CENTER>
<H3 ALIGN=CENTER><TT>Unofficial Primus Trivia Quiz</TT></H3>

<P><FONT FACE="Arial, Helvetica">Have you ever heard that Primus Sucks?  If you haven't, then this 
little quiz here probably isn't going to be much fun for you.  On the 
other hand, this can also be used to make you a bonafide Bastard! 

<FORM METHOD="POST" ACTION="grade.php">
<DL>
<?php

  include "mysql.php";

	$mysql_table = "trivia";

	$link = mysql_connect($mysql_server, $mysql_username, $mysql_password);
	$db = mysql_select_db($mysql_database);
  if (!$link || !$db) { die ('MySQL error: ' . mysql_error()); }
	$query = "SELECT * FROM $mysql_table";
	$result = mysql_query($query);
	$nr = mysql_num_rows($result);
	for($i = 1; $i <= $nr; $i++) {

		$row = mysql_fetch_object($result);
		print "<DT>$row->Number) $row->Question</DT>\n";
		for ($j=1; $j <= 4; $j++) {
			$answer = "Answer". $j;
			print "<DD><TT><INPUT TYPE=radio NAME=". $row->Number ." VALUE=". $j .">";
			print $row->$answer ."</TT></DD>\n";
		}
	}
	mysql_close($link);
?>
</DL>

<HR>
<!------------------END OF SECTION----------->
<INPUT TYPE="submit" VALUE="Let's See How I Did!">
<INPUT TYPE="reset" VALUE="Clear My Answers; I Suck">
</FORM>

</BODY>
</HTML>
