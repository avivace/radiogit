# RadioGit
A Python Bot - built upon the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) wrapper and Node.js - to broadcast GitHub repository events and activities to Telegram chats.

Provides public interface, handles multiple users with multiple subscription to repositories.
Every user can add and remove his subscriptions.

A public instance of the bot is online at [@radiogit_bot](https://t.me/radiogit_bot).

## Overview
- The `webhoook-listener` contains a Node app to listen and record JSON payloads from GitHub;
- The `bot` folder contains the actual Telegram bot, which provides an user interface (allowing personal preferences) and delivers updates;
- In `misc` you'll find some other related code and the old PHP implementation of the webhook listening part (working but **deprecated**).

## Install
### Webhook Listener
**Dependencies**: Node.js (Express 4, body-parser)
Edit the port/webserver configuration and run `node index.js` (you may find useful setting up a reverse proxy). Make sure it's accessible and accepting POST requests, the URL will be the *Payload URL* when setting up the actual webhook in GitHub repository settings.

You can test the listener with `curl` with something like this: 
```
curl -d @payload.json -H "Content-Type: application/json" PAYLOAD/URL/SOME/POST
```
Assuming `payload.json` is something like [this](https://developer.github.com/v3/activity/events/types/#issuesevent).

### The actual bot
**Dependencies**: python3 (telegram, sqlite3).
Insert your bot token and run the bot with `python bot.py`

## Usage
When everything is ready, talk to the bot.
If the repository url is https://github.com/RepoOwner/RepoName, send `/sub RepoOwner/RepoName` to set up event subscription. Adding the bot to a group and senting `/sub` commands from it will make events sent to the group.

## TODO
- Support other types of events (currently supporting only commit events, as POC);
- Implement *secret* checking;
- Conversation Handling;
- Rate Limitation;
- Message Templates;

### Related Projects
- [TeleGit](https://github.com/FruitieX/telegit)
