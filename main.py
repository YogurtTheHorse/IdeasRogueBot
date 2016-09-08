import os
import config
import logging
import telegram
import constants
import usermanager


from telegram.ext.dispatcher import run_async
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext import Job

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger('rgi')

def reply(c_id, bot, txt, buttons=None, photo=None):
	if c_id == 0:
		return

	if buttons:
		custom_keyboard = [ [ x ] for x in buttons ]
		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
		bot.sendMessage(c_id, text=txt, reply_markup=reply_markup)
	elif len(txt) > 0:
		bot.sendMessage(c_id, text=txt)

def start(bot, update):
	reply(update.message.chat_id, bot, constants.HELLO_MESSAGE)

	nickname = bot.getChat(update.message.chat_id)['username']
	if len(nickname) == 0:
		nickname = None

	usermanager.new_user(update.message.chat_id, nickname)
	logger.info('New user with id {0}'.format(update.message.chat_id))

def msg(bot, update):
	c_id = update.message.chat_id

	def rep(txt, btns=None, uid=c_id):
		reply(uid, bot, txt, btns)

	try:
		usermanager.message(c_id, rep, update.message.text)
	except Exception as e:
		logger.warn(str(e))

def ban(bot, update):
	c_id = update.message.chat_id

	if c_id == config.MODERS_CHAT:
		cmd, ban_id = update.message.text.split()
		usermanager.ban(ban_id)

		reply(ban_id, bot, constants.BAN_MESSAGE)
	else:
		reply(c_id, bot, 'Много хочешь')

def notify(bot, update):
	if update.message.chat_id == config.MODERS_CHAT:
		msg = update.message.text[len('/notify@ideasrogbot'):]

		logger.info(msg)

		for user_id in usermanager.get_telegram_users():
			try:
				reply(user_id, bot, msg)
			except:
				logger.info('Couldn\'t send message to {0}'.format(user_id))
	else:
		bot.sendMessage(update.message.chat_id, text='Много хочешь')

def error_callback(bot, update, error):
	error_msg = 'User "%s" had error "%s"' % (update.message.chat_id, error)
	if '429' in str(error):
		logger.warn('429!')
	else:
		logger.warn(error_msg)
	msg = 'Ошибка внутри сервера. Если это мешает играть, сообщите @yegorf1'
	bot.sendMessage(update.message.chat_id, text=msg)
	bot.sendMessage(update.message.chat_id, 
					text='```text\n{0}\n```'.format(error_msg),
					parse_mode=telegram.ParseMode.MARKDOWN)

if not os.path.isdir(config.USERS_PATH):
	logger.info('Creating users directory..')
	os.makedirs(config.USERS_PATH)

if not os.path.isdir(config.IDEAS_PATH):
	logger.info('Creating ideas directory..')
	os.makedirs(config.IDEAS_PATH)

logger.info('Creating Updater...')
updater = Updater(config.TELEGRAM_TOKEN)

updater.dispatcher.add_handler(CommandHandler('notify', notify))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('ban', ban))
updater.dispatcher.add_handler(MessageHandler(False, msg))
updater.dispatcher.add_error_handler(error_callback)

logger.info('Starting polling...')
updater.start_polling()

logger.info('Bot now officially started!')
updater.idle()