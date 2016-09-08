# -*- coding: utf-8 -*-
import os
import sys
import config

variables = {
	'Имя': 'name',
	'Жизней': 'hp',
	'Минимальный урон': 'min_damage',
	'Максимальный урон': 'max_damage',
	'Лут': 'loot',
	'Фраза на входе': 'enter_phrase' 
}


MONSTER_CODE = u"""name = '{0}'
hp = {1}

damage_range = ( {2}, {3} )

coins = 0
loot = [ ]

def enter(user, reply):
	msg = '{4}'
	reply(msg)
"""

def gen_code(idea_id):
	room_vars = dict()
	file_name = config.IDEAS_PATH + '/{0}.i'.format(idea_id)

	lines = [ ]
	with open(file_name, 'r', encoding='utf-8') as f:
		lines = f.readlines()

	for line in lines:
		k, v = line.split(': ')
		if k in variables:
			room_vars[variables[k]] = v[:-1]

	return MONSTER_CODE.format(
			room_vars['name'],
			room_vars['hp'],
			room_vars['min_damage'],
			room_vars['max_damage'],
			room_vars['enter_phrase']
		)

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('Use like that:\npython3 gen_monsters.py 1234546_123456')
		sys.exit()

	for idea_id in sys.argv[1:]:
		print(str(gen_code(idea_id)))


