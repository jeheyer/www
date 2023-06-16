<?php

// HTML Form to global variable conversions
$poll_name = $_POST["poll_name"];
$choice_id = $_POST["choice_id"];
$poll_desc = $_POST["poll_desc"];
$action = $_POST["action"];

// Cookie settings
$cookie_name = "alreadvoted:" . $poll_name;
$cookie_options = array('expires' => time() + 3600, 'secure' => true, 'samesite' => 'Strict');

include "mysql.php";
$mysql_table = "polls";

// Tabulate the vote
if ($action == "Vote" && !$_COOKIE[$cookie_name]) {

	if (!$choice_id || $choice_id == "")
 		die ("Need a choice!");

	$link = mysql_connect($mysql_server, $mysql_username, $mysql_password);
	$db = mysql_select_db($mysql_database);
	if (!$link || !$db) { die ('MySQL error: ' . mysql_error()); }
	$query = "SELECT choice_id,num_votes FROM $mysql_table WHERE poll_name='$poll_name' AND choice_id=$choice_id";
	$result = mysql_query($query);

	if ($row = mysql_fetch_object($result)) {

		// There is at least one vote for this choice, so just add 1 vote and update
		$num_votes = $row->num_votes + 1;
		$query = "UPDATE $mysql_table SET poll_name = '$poll_name', choice_id=$choice_id, num_votes=$num_votes WHERE poll_name='$poll_name' AND choice_id=$choice_id";
		if (!mysql_query($query))
			die ('MySQL error during update: ' . mysql_error());
	} else {

		// First vote for this choice
		$query = "INSERT INTO $mysql_table VALUES ('$poll_name', $choice_id, 1);";

		if (!mysql_query($query))
			die ('MySQL error during insert: ' . mysql_error());
	}
	mysql_close($link);

	// Send a cookie noting they've already voted
	setcookie($cookie_name, true, $cookie_options);
}

header('Location: pollresults.html?poll_name=' . $poll_name . '&poll_desc=' . $poll_desc);
exit;

?>
<!doctype html>
<html lang='en'>
<head><title>Poll Results</title>
<?php

// Add appropriate CSS
if ($poll_name == "albums")
	$css_file = "lb.css";
if ($poll_name == "videos")
	$css_file = "pp.css";
if ($css_file)
	echo "<link rel='stylesheet' type='text/css' href='css/". $css_file ."'>\n";

?>
</head>
<body>

<?php

if (!$poll_name)
	die('poll name not provided!');

echo "<h4>". $poll_desc ."</h4>\n<table class='poll'>\n";

$link = mysql_connect($mysql_server, $mysql_username, $mysql_password);
mysql_select_db($mysql_database);

$query = "SELECT SUM(num_votes) as total_votes FROM $mysql_table WHERE poll_name = '$poll_name'";
if (!mysql_query($query))
	die ('MySQL error while retieving num of votes: ' . mysql_error());
$result = mysql_query($query);
$row = mysql_fetch_object($result);
$total_votes = $row->total_votes;


$query = "SELECT full_name,num_votes,ROUND((num_votes/(SELECT SUM(num_votes) FROM polls WHERE poll_name = '$poll_name') * 100),1) percent FROM $mysql_table,$poll_name WHERE polls.poll_name='$poll_name' AND polls.choice_id=$poll_name.id ORDER BY num_votes DESC";
if (!mysql_query($query))
	die ('MySQL error during display votes: ' . mysql_error($link));

$result = mysql_query($query);
$nr = mysql_num_rows($result);
if ($nr == 0) {
	print "</TABLE>No one has voted yet!\n";
	exit;
}
for($i = 1; $i <= $nr; $i++) {
	$row = mysql_fetch_object($result);
	$num_votes = $row->num_votes;
	//$percentage = intval(($num_votes / $total_votes) * 100);
	$percentage = $row->percent;
	print "<TR><TD WIDTH=40%>". $row->full_name ."</TD>";
	print "<TD WIDTH=10%>". $num_votes ." votes</TD>";
	print "<TD WIDTH=10%>". $percentage ."%</TD>";
	$bar_length = ($percentage/2 * 10)+1;
	print "<TD WIDTH=40%><IMG SRC='makebar.php?hsize=". $bar_length ."&vsize=10'></TD>";
	print "</TR>\n";
}
print "</TABLE>\n";
mysql_close($link);
print "<P><B>". $total_votes ."</B> votes so far.</P>\n";
echo "</table>\n</body>\n</html>";

?>
