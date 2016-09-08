import os
import glob
import pickle
import random
import config
from user import User
		
def get_fname(uid):
	return config.USERS_PATH + '/{0}.usr'.format(uid)

def save_user(usr):
	if usr is None:
		return
		
	with open(get_fname(usr.uid), 'wb') as outfile:
		pickle.dump(usr, outfile)

def ban(uid):
	usr = get_user(uid)
	usr.banned = True
	save_user(usr)

def new_user(uid, nickname=None):
	was = get_user(uid)
	if was and was.banned:
		return

	usr = User(uid, nickname)

	save_user(usr)

def get_telegram_users():
	for f in glob.glob(config.USERS_PATH + '/*.usr'):
		uid = os.path.basename(f)[:-4]

		if not uid.startswith('vk'):
			yield uid

def get_user(uid):
	if os.path.exists(get_fname(uid)):
		usr = None

		with open(get_fname(uid), 'rb') as outfile:
			usr = pickle.load(outfile)

		return usr
	else:
		return None

def message(uid, reply, text):
	usr = get_user(uid)

	if not usr:
		reply('Что-то пошло не так. Попробуй /start')
	else:
		usr.message(reply, text)

	save_user(usr)