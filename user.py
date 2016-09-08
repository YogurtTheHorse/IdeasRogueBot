import time
import config
import constants
import questions

class User(object):
	def __init__(self, uid, nickname=None):
		super(User, self).__init__()
		self.uid = uid
		self.nickname = nickname
		
		self.banned = False
		self.state = 'start'
		
		self.question = 'none'
		self.question_number = 0
		self.questions = {
			'new_monster': questions.new_monster,
			'new_pet': questions.new_pet,
			'new_item': questions.new_item,
			'feedback': questions.feedback,
			'other': questions.other
		}

		self.variables = dict()

	def get_variable(self, name, def_val=None):
		if name in self.variables:
			return self.variables[name]
		else:
			return def_val

	def set_variable(self, name, val):
		self.variables[name] = val

	def get_current_question(self):
		lst = self.questions[self.question]['list']

		if self.question_number >= len(lst):
			return None
		else:
			return lst[self.question_number]

	def start_questions(self, reply, question):
		self.question = question
		self.question_number = 0

		reply('Теперь мы зададим неколько вопросов')

		self.ask(reply)

	def ask(self, reply):
		question = self.get_current_question()
		self.state = 'answer'

		reply(question['text'])

	def get_result(self):
		variables_list = self.questions[self.question]['variables']

		res = 'Автор: {0}'.format(self.uid)

		if self.nickname and len(self.nickname) > 0:
			res += ' (@{0})'.format(self.nickname)
		res += '\n'

		for k, v in variables_list.items():
			res += '{0}: {1}\n'.format(v, self.get_variable(k))

		return res

	def ask_next(self, reply):
		self.question_number += 1
		question = self.get_current_question()

		if question is None:
			result = self.get_result()
			reply('Оп! Вопросы закончилсь. Подведем итоги:\n\n{0}\nОтправляем?'.format(result), ['Да', 'Фигня вышла'])

			self.state = 'agree'
		else:
			reply(question['text'])

	def send_idea(self, reply):
		idea_id = str(self.uid) + '_' + str(round(time.time() // 1000))
		res = 'id: {0}\n'.format(idea_id) + self.get_result()

		with open(config.IDEAS_PATH + '/{0}.i'.format(idea_id), 'w') as f:
			f.write(res)

		reply(res, uid=config.MODERS_CHAT)

	def message(self, reply, text):
		if self.banned:
			reply(constants.BAN_MESSAGE)
		elif self.state == 'start':
			if text.startswith('/') and text[1:] in self.questions:
				cmd = text[1:]
				self.start_questions(reply, cmd)
			else:
				reply(constants.HELLO_MESSAGE)

		elif self.state == 'answer':
			current_question = self.get_current_question()
			checker = current_question['checker']
			if checker(text):
				self.set_variable(current_question['variable_name'], text)
				self.ask_next(reply)
			else:
				reply(current_question['failure'])
		elif self.state == 'agree':
			if text == 'Да':
				self.send_idea(reply)
			else:
				reply('Как знаешь')

			self.state = 'start'
			reply(constants.HELLO_MESSAGE)