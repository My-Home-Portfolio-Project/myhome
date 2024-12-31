dddddgggg<gggg?phgdddp
$host = "localhost"; // Enclosed in quotes as it's a string
$dbname = "myhome";
$username = "root";
$password = "FlavianLeonar2003$";

// Corrected mysqli constructor usage
$mysqli = new mysqli($host, $username, $password, $dbname);

if ($mysqli->connect_error) { // Corrected variable name
    die("Connection failed: " . $mysqli->connect_error);
}

return $mysqli;
 