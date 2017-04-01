<?php
$db = new SQLite3('db.sqlite') or die('Unable to open database');


$data = json_decode(file_get_contents('php://input'), true);
if ($data == "") {
  echo "<h1>ERROR</h1> <h3>Uhm, this is the webhook listener for <a href='https://github.com/avivace/radiogit'>RadioGit</a>, you shouldn't open it with a GET request.</h3>";
} else {
  $repo_name = $data['repository']['full_name'];
  $commit_message = $data['commits'][0]['message'];
  $url = $data['commits'][0]['url'];
  $author = $data['commits'][0]['author']['username'];

  $text = "*".$repo_name."* - ".$author." committed "."[".$commit_message."](".$url.")";
  $query = 'INSERT INTO Payloads VALUES (NULL, "'.$repo_name.'","'.$text.'")';

  $result = $db->query($query) or die('Query failed');
}

?>
