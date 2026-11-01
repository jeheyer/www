<?php

include_once('fix_mysql.inc.php');

$mysql_port = "3306";
$mysql_server = getenv('MYSQL_HOSTNAME');
$mysql_database = getenv('MYSQL_DATABASE');
$mysql_username = getenv('MYSQL_USERNAME');
$mysql_password = getenv('MYSQL_PASSWORD');

?>
