<?php

include "mysql.php";

if (isset($argv[1]))
    $mysql_table = $argv[1];
else {
    if (isset($_GET["type"]))
        $mysql_table = $_GET["type"];
    if (isset($_POST["type"]))
        $mysql_table = $_POST["type"];
}
if (!isset($mysql_table))
    die("I do not know what you seek\n");

$link = mysql_connect($mysql_server, $mysql_username, $mysql_password);
$db = mysql_select_db($mysql_database);
if (!$link || !$db) { die ('MySQL error: ' . mysql_error()); }

if ($mysql_table == "polls") {
    if (isset($argv[2]))
        $poll_name = $argv[2];
    else {
        if (isset($_GET["poll_name"]))
            $poll_name = $_GET["poll_name"];
            if (isset($_POST["poll_name"]))
                $poll_name = $_POST["poll_name"];
    }
    if (!isset($poll_name))
        die("Need to know which poll\n");
    $query = "SELECT full_name,num_votes FROM polls,$poll_name WHERE poll_name = '$poll_name' AND id = polls.choice_id ORDER by num_votes DESC";
} else {
    $query = "SELECT * FROM $mysql_table ORDER BY id";
}
if (!mysql_query($query))
    die ('MySQL error: ' . mysqli_error($link));
else {
    $result = mysql_query($query);
    $nr = mysql_num_rows($result);
    $data = array();
    for($i = 1; $i <= $nr; $i++)
        array_push($data, mysql_fetch_object($result));
}

mysql_close($link);

header('Content-type: application/json');
print(json_encode($data, JSON_PRETTY_PRINT));
print("\n");

?>
