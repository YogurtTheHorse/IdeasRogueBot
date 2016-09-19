import constants

def check_str(name):
	return not ('_' in name or '*' in name)

def check_int(number):
	try:
		a = int(number)
		return True
	except:
		return False

new_monster = {
	'variables': {
		'monster_name': 'Имя',
		'monster_hp': 'Жизней',
		'monster_min_damage': 'Минимальный урон',
		'monster_max_damage': 'Максимальный урон',
		'monster_loot': 'Лут',
		'monster_enter_phrase': 'Фраза на входе'
	},
	'list': [
		{
			'text': 'Как назовем нового монстра?',
			'checker': check_str,
			'variable_name': 'monster_name',
			'failure': constants.WRONG_NAME
		},
		{
			'text': 'Какой минимальный урон он будет наносить?',
			'checker': check_int,
			'variable_name': 'monster_min_damage',
			'failure': constants.WRONG_INT
		},
		{
			'text': 'Какой максиимальный урон он будет наносить?',
			'checker': check_int,
			'variable_name': 'monster_max_damage',
			'failure': constants.WRONG_INT
		},
		{
			'text': 'Какую фразу выводить на входе?',
			'checker': check_str,
			'variable_name': 'monster_enter_phrase',
			'failure': constants.WRONG_STR
		},
		{
			'text': 'Сколько жизней будет у монстра?',
			'checker': check_str,
			'variable_name': 'monster_hp',
			'failure': constants.WRONG_STR
		},
		{
			'text': 'Какой лут будет у монстра?',
			'checker': check_str,
			'variable_name': 'monster_loot',
			'failure': constants.WRONG_STR
		}
	]
}

new_pet = {
	'variables': {
		'pet_name': 'Имя питомца',
		'pet_path': 'Способ получения',
		'pet_description': 'Описание',
	},
	'list': [
		{
			'text': 'Как назовем нового питомца?',
			'checker': check_str,
			'variable_name': 'pet_name',
			'failure': constants.WRONG_NAME
		},
		{
			'text': 'Как получить?',
			'checker': check_str,
			'variable_name': 'pet_path',
			'failure': constants.WRONG_STR
		},
		{
			'text': 'Опиши его особенности',
			'checker': check_str,
			'variable_name': 'pet_description',
			'failure': constants.WRONG_STR
		}
	]
}

new_item = {
	'variables': {
		'item_name': 'Название',
		'item_price': 'Цена',
		'item_description': 'Описание'
	},
	'list': [
		{
			'text': 'Как будет называться вещь?',
			'checker': check_str,
			'variable_name': 'item_name',
			'failure': constants.WRONG_NAME
		},
		{
			'text': 'Сколько будет стоить?',
			'checker': check_int,
			'variable_name': 'item_price',
			'failure': constants.WRONG_INT
		},
		{
			'text': 'Что будет делать?',
			'checker': check_str,
			'variable_name': 'item_description',
			'failure': constants.WRONG_STR
		}
	]
}

feedback = {
	'variables': {
		'feedback': 'Фидбэк',
		'game_rate': 'Оценка игры'
	},
	'list': [
		{
			'text': 'Рассказывай',
			'checker': check_str,
			'variable_name': 'feedback',
			'failure': constants.WRONG_STR
		},
		{
			'text': 'Оцени игру',
			'checker': check_str,
			'variable_name': 'game_rate',
			'failure': constants.WRONG_STR
		}
	]
}

other = {
	'variables': {
		'other': 'Сообщение'
	},
	'list': [
		{
			'text': 'Рассказывай',
			'checker': check_str,
			'variable_name': 'other',
			'failure': constants.WRONG_STR
		}
	]
}

podcast = {
	'variables': {
		'question': 'Вопрос'
	},
	'list': [
		{
			'text': 'Что бы ты хотел узнать?',
			'checker': check_str,
			'variable_name': 'question',
			'failure': constants.WRONG_STR
		}
	]
}