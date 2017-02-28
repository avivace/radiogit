<?php
$token= '';
$chat_id= '';
$data = json_decode(file_get_contents('php://input'), true);
$text = $data['repository']['full_name'].$data['commits'][0]['message'].' - '.$data['commits'][0]['url'];
$request = 'https://api.telegram.org/bot'.$token.'/sendMessage?chat_id='.$chat_id.'&text='.$text;
$r = file_get_contents($request);
?>
