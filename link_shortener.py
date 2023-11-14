#Encurtador de Links, feito em Python através do pacote Pyshorteners
# Documentação: https://pyshorteners.readthedocs.io/en/latest/

import pyshorteners

#Entrada | Input
longo = input(" Insira o link para encurtar: ")

#Processo de encurtação do link
type_tiny = pyshorteners.Shortener()
curto = type_tiny.tinyurl.short(longo)

#Saida | Output: Link encurtado com tinyurl.com
print("Link encurtado: " + curto)


