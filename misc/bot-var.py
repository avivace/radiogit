def sub(bot, update):
    logging.warning(str(update.message.chat_id) + " sub")
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO subs VALUES (' +
        str(update.message.chat_id)+',"'+str(update.message.from_user.username)+'",1)')
    bot.sendMessage(chat_id=update.message.chat_id,
        text=sub_text,
        parse_mode=ParseMode.MARKDOWN)
    conn.commit()

def stop(bot, update):
    logging.warning(str(update.message.chat_id) + " stop")
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO subs VALUES (' +
        str(update.message.chat_id)+',"'+str(update.message.from_user.username)+'",0)')
    bot.sendMessage(chat_id=update.message.chat_id,
        text=stop_text,
        parse_mode=ParseMode.MARKDOWN)
    conn.commit()

def broadcast_callback(bot, job):
    global actualsu
    global batch
    global step
    global timetodie
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT "chat_id" FROM "subs" WHERE "status" = 1')
    subs = c.fetchall()
    l = len(subs)
    logging.warning("BATCH" + str(batch))

    if actualsub+step > l:
        endrange = l
        timetodie = 1
    else:
        endrange = actualsub+step

    for i in range (actualsub, endrange):
        logging.warning("  SENDING TO " + str(subs[i][0]))
        chat = int(subs[i][0])
        bot.sendMessage(chat_id=chat,
            text='testing job handler. this is batch '+str(batch))
    actualsub += step
    batch += 1

    if timetodie == 1:
        timetodie = 0
        job.schedule_removal()
        logging.warning("JOB REMOVED")

def test(bot, update):
    j.put(Job(broadcast_callback, 1.0))
    bot.sendMessage(chat_id=update.message.chat_id,
        text="Started a job")

defun sendReddit(bot, update)
    json_file = "https://www.reddit.com/r/" + SUBREDDIT + "/top.json"
    j = requests.get(json_file)
    j_obj = j.json()
    url= str(j_obj['data']['children'][i]['data']['url'])
    title = j_obj['data']['children'][i]['data']['title'].encode('utf-8')
    tag= str(j_obj['data']['children'][i]['data']['subreddit'])
    bot.sendMessage(chat_id=chat_id2,
            text="#"+tag + " " + title + " " + url)
