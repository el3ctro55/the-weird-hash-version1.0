import json
import mysql
import re
alpha_hash = \
{'a': 'α╬◙░',
 'b': '¤╪┘┌',
 'c': '┘┌○┘',
 'd': '╛▓≡∩',
 'e': 'Ωδ«σ',
 'f': '♀§█|',
 'g': '▐▌Γº',
 'h': '∞®ε¯',
 'i': '±ð⌡⌠',
 'j': '#@()',
 'k': '∙▒∙╡',
 'l': '║≡╝*',
 'm': '⌐¬♂∟',
 'n': '▬↔↑↓',
 'o': '×™——',
 'p': '◘○◘☼',
 'q': '☼◄►☼',
 'r': '¶╬╨╞',
 's': '■‡Œ═',
 't': '‰†╘╒',
 'u': '¤¥π░',
 'v': '╥╫╥╫',
 'w': '@∟îε∩',
 'x': '®εå└',
 'y': 'Å®ε░',
 'z': '┼€┬┴'}



def return_hash(txt=str, dict=dict):
	hash = " "
	for letters in txt:

		if letters in dict.keys():
			hash = hash + dict[letters]
		elif letters not in dict.keys():
			hash = hash + letters
	return hash


def return_passwd(hash, dict=dict):
	passwd = " "
	for key, value in dict.items():
		passwd = passwd + hash
		passwd = passwd.replace(value, key)
	return passwd

	


while True:

	user = input('\ncreate password: ')
	hash = return_hash(txt=user, dict=alpha_hash)
	password = return_passwd(hash=hash, dict=alpha_hash)

	print(f"hash:{hash}\npassword:{password}")



