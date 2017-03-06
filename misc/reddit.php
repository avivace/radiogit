<?php

/* https://github.com/avivace/telegram-examples
reddit.php - Publish the top posts of a subreddit (or multireddit or series of subreddits) on a Telegram Channel.
*/

for ($i =0; $i < 3; $i++){
	// Get values from Reddit (Top 24h) - top posts from a public multireddit
	$jsonurl = file_get_contents("https://www.reddit.com/user/shinyeye4/m/cs_frontpage/top.json"); // Hint: you can limit the quantity of posts with ?limit=4, lowering the size of the JSON
	$json = json_decode($jsonurl,true);

	// Post Values
	$url= $json['data']['children'][$i]['data']['url'];
	$title= $json['data']['children'][$i]['data']['title'];
	$tag= $json['data']['children'][$i]['data']['subreddit'];

	// GET Request
	$token= '';
	$chat_id= '';				
	$text= '%23'.$tag.' '.$title.' '.$url;    // #subreddit - title - url
	
	$request = 'https://api.telegram.org/bot'.$token.'/sendMessage?chat_id='.$chat_id.'&text='.$text;

	// Print final requests. DON'T RUN THIS IN PUBLIC ENVIRONMENT, botKey and private chat ID can be crawled.
	// echo $i. ' - '.$tag.'<br>'.$request.'<br>';

	// Send the GET Request
	$r = file_get_contents($request); 

}
?>
