"""
Mauricio P Pires <mauricioppires at gmail dot com>

"""

"""
arquivo1.txt contem:
----------------
ADMINISTRADOR
TÉCNICO REDES DE COMPUTADORES
PROGRAMADOR DE COMPUTADOR
RÁDIO TÉCNICO

"""

from unidecode import unidecode         # se não tiver essa lib, instale: pip install unidecode

arquivo1 = open("arquivo1.txt","r")     # Abre para leitura.
lista = arquivo1.readlines()            # lista recebe todas as linha do arquivo1.txt.
arquivo2 = open("arquivo2.txt","w")     # Abre para gravacao.

contador = 1                            # variavel para implementar auto numeração na nova lista.

for linha in lista:
    # novaLinha recebe a linha atual, removendo os caracteres acentuados.
    # str() - converte numero em string.
    # .strip() - remove todos os espaços excedentes das duas pontas da string.
    # '\n' - nova linha (new line) - basicamente um ENTER no final da linha.
    novaLinha = str(contador).strip() + ',' + unidecode(linha).strip() + '\n'
    # arquivo2 recebe a nova linha (ja processada).
    arquivo2.write(novaLinha)
    # incremento: contador = (recebe) contador + 1
    contador += 1

# Fecha arquivo1 e arquivo2
arquivo1.close()
arquivo2.close()

"""
arquivo2.txt recebeu:
----------------
1,ADMINISTRADOR
2,TECNICO REDES DE COMPUTADORES
3,PROGRAMADOR DE COMPUTADOR
4,RADIO TECNICO

"""
