import requests #necessária para leitura da api
from googletrans import Translator #responsável por traduzir o texto final

#iniciando a função translator em uma variável
trans = Translator()

#indicando o caminho da API e salvando em uma variável
conselho = "https://api.adviceslip.com/advice"

#fazendo o request na API
pegar_conselho = requests.get(conselho)

#transformando o retorno da api em json
conselho_atual = pegar_conselho.json()

#listando o conteúdo do json
conteudo = list(conselho_atual.values())

#tratando a primeira array
dicionario_final = conteudo[0]

#listando o conteúdo principal
lista_final = list(dicionario_final.values())

#traduzindo o conselho trazido pela API
texto_traduzido = trans.translate(lista_final[1],'pt').text

print(texto_traduzido)

