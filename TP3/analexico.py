import sys
import re

def tokenize(input_string, linha):
	reconhecidos = []
	mo = re.finditer(
		r'(?P<COMENT>#[^\n]*)|'
		r'(?P<VAR>\?\w+)|'
		r'(?P<LANG>@[a-z]{2})|'
		r'(?P<STRING>"[^"]*")|'
		r'(?P<PR>(?:select|where|LIMIT)\b)|'
		r'(?P<DELIM>[{}.])|'
		r'(?P<NUM>\d+\b)|'
		r'(?P<CONC>\w+(?:\:\w+)?)|'
		r'(?P<ERRO>\S)',
		input_string)
	
	for m in mo:
		dic = m.groupdict()
		if dic['COMENT']:
			continue
		elif dic['VAR']:
			t = ("VAR", dic['VAR'], linha, m.span())
		elif dic['LANG']:
			t = ("LANG", dic['LANG'], linha, m.span())
		elif dic['STRING']:
			t = ("STRING", dic['STRING'], linha, m.span())
		elif dic['PR']:
			t = ("PR", dic['PR'], linha, m.span())
		elif dic['DELIM']:
			t = ("DELIM", dic['DELIM'], linha, m.span())
		elif dic['NUM']:
			t = ("NUM", dic['NUM'], linha, m.span())
		elif dic['CONC']:
			t = ("CONC", dic['CONC'], linha, m.span())
		elif dic['ERRO']:
			t = ("ERRO", dic['ERRO'], linha, m.span())

		reconhecidos.append(t)
	return reconhecidos


for n, texto in enumerate(sys.stdin, 1):
	for tok in tokenize(texto, n):
		print(tok)

 