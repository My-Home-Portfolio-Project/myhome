<?php
if (empty($_POST["name"])) {
    die('Please fill in the name field');
}
if ( ! filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
    die('Invalid email address');
}
if (strlen($_POST['password']) < 8) {
    die('Password must be at least 8 characters long');
}
if ($_POST['password'] !== $_POST['repeat_password']) {
    die('Passwords do not match');
}
if ( ! preg_match('/[A-Z]/', $_POST['password'])) {
    die('Password must contain at least one uppercase letter');
}
if ( ! preg_match('/[a-z]/', $_POST['password'])) {
    die('Password must contain at least one lowercase letter');
}
if ( ! preg_match('/[0-9]/', $_POST['password'])) {
    die('Password must contain at least one number');
} 
print_r($_POST);
   