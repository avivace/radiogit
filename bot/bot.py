from telegram.ext import Updater, CommandHandler, Job
from telegram import ParseMode
from random import randint
import logging, sqlite3, urllib, json, urllib2, requests, requests_cache

updater = Updater(token='YOUR_BOT_TOKEN')
dispatcher = updater.dispatcher
j = updater.job_queue

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.DEBUG)

# Messages
start_text = "Hey! To subscribe to a (GitHub) Repository events, send `/sub Owner/RepositoryName` and I'll send you events from that repository.\nFor example, if the repository URL is `https://github.com/avivace/testrepo`, send me `/sub avivace/testrepo`."

# Database
db_file = 'db.sqlite' # MAKE SURE THIS IS THE SAME DB USED BY THE WEBHOOK HANDLER
conn = sqlite3.connect(db_file)
c = conn.cursor()

def sub(bot, update):
    text = update.message.text[5:]
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT ID FROM Subscribers WHERE Chat_ID = '+ str(update.message.chat_id)+' AND Repo_name ="'+str(text)+'"')
    query_result = c.fetchall()
    if (query_result == []):
        c.execute('INSERT INTO Subscribers VALUES(NULL,"' + str(update.message.chat_id) + '","' + str(text) + '")')
        conn.commit()
        logging.warning(str(text))
        bot.sendMessage(
                chat_id=update.message.chat_id,
                text="Done. I've subscribed you to events from *" + text +"*. \nNow go in your repository Settings > Webhooks > Add webhook.\nType `YOUR_WEBHOOK_URL` as *Payload URL* and select `application/json` as *Content type*.\nSelect the events you want to be notified of and press *Add webhook*.",
                parse_mode=ParseMode.MARKDOWN)
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="You were already subscribed to this repo.")

def unsub(bot, update):
    text = update.message.text[7:]
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('DELETE FROM Subscribers WHERE Chat_ID='+ str(update.message.chat_id) + ' AND Repo_name="'+ str(text) +'"')
    conn.commit()
    bot.sendMessage(chat_id=update.message.chat_id, text="Done. I've unsubscribed you to events from " + text)

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
            text=start_text,
            parse_mode=ParseMode.MARKDOWN)

# Regular Check payloads Job
def callback_10(bot, job):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT * FROM Payloads')
    result = c.fetchall()
    for i in range(0, len(result)):
        payload_id = result[i][0]
        repo_name = result[i][1]
        message = result[i][2]
        c.execute('SELECT Chat_ID from Subscribers WHERE Repo_name="'+str(repo_name)+'"')
        query_result = c.fetchall()
        chat = query_result[0][0]
        bot.sendMessage(chat_id=chat,
                text=str(message),
                parse_mode=ParseMode.MARKDOWN)
        c.execute('DELETE FROM Payloads WHERE ID='+str(result[i][0]))
        conn.commit()

job_10 = Job(callback_10, 3.0)
j.put(job_10, next_t=0.0)

# Handlers and Dispatchers
start_handler = CommandHandler('start', start)
sub_handler = CommandHandler('sub', sub)
unsub_handler = CommandHandler('unsub', unsub)
dispatcher.add_handler(unsub_handler)
dispatcher.add_handler(sub_handler)
dispatcher.add_handler(start_handler)

# Start the bot
updater.start_polling()

# Run the bot until some SIGINT/SINTERM/SIGABRT (start_polling is non
#  blocking).
updater.idle()
logging.warning('Gracefully stopped')
conn.commit()
conn.close()
