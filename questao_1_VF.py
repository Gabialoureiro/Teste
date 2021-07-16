import os
from os.path import isfile, join
from os import walk
import csv
def encontraArquivosEmPastaRecursivamente(pasta='',extensao=''):
    arquivoscsv = []
    caminhoAbsoluto = os.path.abspath(pasta)
    for pastaAtual, subPastas, arquivos  in os.walk(caminhoAbsoluto):
        arquivoscsv.extend([os.path.join(pastaAtual,arquivo) for arquivo in arquivos if arquivo.endswith('.csv')])
    return arquivoscsv
def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


"""print(encontraArquivosEmPastaRecursivamente('c:/Users/gabia/Python/Gabriela_lista2/Compras', '.csv'))"""
arquivoscsv_final=encontraArquivosEmPastaRecursivamente('c:/Users/gabia/Python/Gabriela_lista2/Compras', '.csv')
"""print("%s" %arquivoscsv_final)"""

todas_compras=[]
compra=[]
itens_discrepantes=[]
itens_totais=[]
i=0

for item in arquivoscsv_final:
  with open(item, encoding='utf-8') as arquivo_referencia:

  # 2. ler a tabela
    tabela = csv.reader(arquivo_referencia)

  # 3. navegar pela tabela
    for l in tabela:
      item_nome = l[0]
      item_preco = l[1]
      item_data= l[2]
      compra=[item_nome,item_preco,item_data]
      todas_compras.append(compra)

"""print(todas_compras)"""

for compras in todas_compras:
  i=0
  a=0
  item=compras[0]
  item_compra=compras[1]
  precos=[compra[1]]
  precos_ordenados=[0]
  item_discrepante=[0]
  for compras in todas_compras:
    if compras[0]==item:
      precos.append(compra[1])
    
  precos_ordenados=sorted(precos)
  menor_preco_item=precos_ordenados[0]
  valor_menor=float(menor_preco_item)
  for preco in precos_ordenados:
    if float(preco) > 1.25*float(menor_preco_item):
      i=1  
  if i==1: 
    item_discrepante=[item] 
    for compras in todas_compras:
      if compras[0]==item:
        dados=[compras[1],compras[2]]
        """print("%s" %dados)"""

        item_discrepante.append(compra[1])
        item_discrepante.append(compra[2])
      print("%s" %item_discrepante)
    itens_discrepantes.append(item_discrepante)

print("%s" %itens_discrepantes)
f= open('relatorio_final.txt','w')
for linha in itens_discrepantes:
  for item in linha:

    f.write(item)
  f.write('\n')
f.close()

  
        

