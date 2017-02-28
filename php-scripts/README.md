## telegram-examples
Some intro examples on Telegram APIs integration with other services.

- [**reddit.php**](reddit.php) Publish the top posts of a subreddit (or multireddit or series of subreddits) on a Telegram Channel.
- [**radiogit.php**](radiogit.php) Broadcasts repository activities to Telegram 

### Tips
- You can get the unique chat ID for private chats making them public, using the @id, sending a sendMessage request and copying the chat ID on the response (then you can switch back the chat to private).
- You can (periodically) run a PHP script setting up a cronjob (e.g. <code> crontab -e </code> with a job like <code> curl localhost/yourscript.php </code>
