# RadioGit
A Python Bot, built upon the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) wrapper, to broadcast GitHub repository events and activities to Telegram chats.

Provides public interface, handles multiple users with multiple subscription to repositories.

Every user can add and remove his subscriptions. Currently, only **commit** events are supported.

## Usage
**Dependencies**: PHP, a web server, python (telegram, sqlite3).

1. Clone this repo;
2. Set up the webhook listener in your webserver folder, make sure it's accessible and accepting POST requests;
3. Insert your bot token and run the bot with `python bot.py`;

A public instance of the bot is online at [@radiogit_bot](https://t.me/radiogit_bot).

If the repository url is https://github.com/RepoOwner/RepoName, send `/sub RepoOwner/RepoName` to set up event subscription. Adding the bot to a group and senting `/sub` commands from it will make events sent to the group.

The `misc` folder contains various other code related to Telegram bots.

## TODO
- Support other types of events;
- Implement *secret* checking;
- Implement webhook listener in something not PHP;
- Conversation Handling;
- Rate Limitation;
- Message Templates;

### Related Projects
- [TeleGit](https://github.com/FruitieX/telegit)
