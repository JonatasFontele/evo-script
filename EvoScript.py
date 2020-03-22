# -*- coding: utf-8 -*-
# Evo Bracket Sort Script created by Jony Walker.
# Script ordenador de chaves da Evo feito por Jony Walker.

arq = open('entrada.txt', 'r')         #Abre e le um arquivo txt, depois salva em arq.
lista = arq.readlines()                 #Le todas as linhas salvas em arq e salva na memória virtual de lista
arq = open('chaveamento.txt', 'w')      #Abre ou cria um arquivo txt para ser escrito
qtdLinha = 0
nome = []
                
for linha in lista:                     #Iteracao.
        if linha != "\n":               #Se a linha nao for vazia, continue.
                qtdLinha =+ qtdLinha    #Contador
                nome.append(linha)      #Adiciona cada linha a cada iteracao ao vetor 'nome'

if (qtdLinha <= 16):                      #Se quantidade de inscritos for menor ou igual a 16, imprima chave para 8 confrontos.
        while (qtdLinha < 16):
                nome.append("ninguem")
                qtdLinha =+ qtdLinha
        chaves ="""[fase]
[luta=A | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=B | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=C | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=D | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=E | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=F | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=G | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=H | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[/fase]
[fase]
[luta=I | player1=A | player2=B | resultado_p1=? | resultado_p2=?]
[luta=II | player1=C | player2=D | resultado_p1=? | resultado_p2=?]
[luta=III | player1=E | player2=F | resultado_p1=? | resultado_p2=?]
[luta=IV | player1=G | player2=H | resultado_p1=? | resultado_p2=?]
[/fase]
[fase]
[luta=1 | player1=I | player2=II | resultado_p1=? | resultado_p2=?]
[luta=2 | player1=III | player2=IV | resultado_p1=? | resultado_p2=?]
[/fase]
[fase]
[luta=X | player1=1 | player2=2 | resultado_p1=? | resultado_p2=?]
[/fase]""" % (nome[0], nome[1], nome[2], nome[3], nome[4], nome[5], nome[6], nome[7], nome[8], nome[9], nome[10], nome[11], nome[12], nome[13], nome[14], nome[15])
        arq.write(chaves)
elif (16 < qtdLinha <= 32):             #Se quantidade de inscritos for maior que 16 e menor ou igual a 32, imprima chave para 16 confrontos.
        while (qtdLinha < 32):
                nome.append("ninguem")
                qtdLinha = qtdLinha+1
        chaves ="""[fase]
[luta=I | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=II | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=III | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=IV | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=V | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=VI | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=VII | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=VIII | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=IX | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=X | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=XI | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=XII | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=XIII | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=XIV | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=XV | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=XVI | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[/fase]
[fase]
[luta=A | player1=I | player2=II | resultado_p1=? | resultado_p2=?]
[luta=B | player1=III | player2=IV | resultado_p1=? | resultado_p2=?]
[luta=C | player1=V | player2=VI | resultado_p1=? | resultado_p2=?]
[luta=D | player1=VII | player2=VIII | resultado_p1=? | resultado_p2=?]
[luta=E | player1=IX | player2=X | resultado_p1=? | resultado_p2=?]
[luta=F | player1=XI | player2=XII | resultado_p1=? | resultado_p2=?]
[luta=G | player1=XIII | player2=XIV | resultado_p1=? | resultado_p2=?]
[luta=H | player1=XV | player2=XVI | resultado_p1=? | resultado_p2=?]
[/fase]
[fase]
[luta=I | player1=A | player2=B | resultado_p1=? | resultado_p2=?]
[luta=II | player1=C | player2=D | resultado_p1=? | resultado_p2=?]
[luta=III | player1=E | player2=F | resultado_p1=? | resultado_p2=?]
[luta=IV | player1=G | player2=H | resultado_p1=? | resultado_p2=?]
[/fase]
[fase]
[luta=1 | player1=I | player2=II | resultado_p1=? | resultado_p2=?]
[luta=2 | player1=III | player2=IV | resultado_p1=? | resultado_p2=?]
[/fase]
[fase]
[luta=A | player1=1 | player2=2 | resultado_p1=? | resultado_p2=?]
[/fase]""" % (nome[0], nome[1], nome[2], nome[3], nome[4], nome[5], nome[6], nome[7], nome[8], nome[9], nome[10], nome[11], nome[12], nome[13], nome[14], nome[15],
              nome[16], nome[17], nome[18], nome[19], nome[20], nome[21], nome[22], nome[23], nome[24], nome[25], nome[26], nome[27], nome[28], nome[29], nome[30],
              nome[31])
        arq.write(chaves)
else:                                   #Se quantidade de inscritos for maior do que 32, imprima chave para 32 confrontos.
        while (qtdLinha < 64):
                nome.append("ninguem")
                qtdLinha = qtdLinha+1
        chaves ="""[fase]
[luta=1 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=2 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=3 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=4 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=5 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=6 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=7 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=8 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=9 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=10 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=11 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=12 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=13 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=14 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=15 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=16 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=17 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=18 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=19 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=20 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=21 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=22 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=23 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=24 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=25 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=26 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=27 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=28 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=29 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=30 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=31 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[luta=32 | player1=%s | player2=%s | resultado_p1=? | resultado_p2=?]
[/fase]
[fase]
[luta=I | player1=1 | player2=2 | resultado_p1=? | resultado_p2=?]
[luta=II | player1=3 | player2=4 | resultado_p1=? | resultado_p2=?]
[luta=III | player1=5 | player2=6 | resultado_p1=? | resultado_p2=?]
[luta=IV | player1=7 | player2=8 | resultado_p1=? | resultado_p2=?]
[luta=V | player1=9 | player2=10 | resultado_p1=? | resultado_p2=?]
[luta=VI | player1=11 | player2=12 | resultado_p1=? | resultado_p2=?]
[luta=VII | player1=13 | player2=14 | resultado_p1=? | resultado_p2=?]
[luta=VIII | player1=15 | player2=16 | resultado_p1=? | resultado_p2=?]
[luta=IX | player1=17 | player2=18 | resultado_p1=? | resultado_p2=?]
[luta=X | player1=19 | player2=20 | resultado_p1=? | resultado_p2=?]
[luta=XI | player1=21 | player2=22 | resultado_p1=? | resultado_p2=?]
[luta=XII | player1=23 | player2=24 | resultado_p1=? | resultado_p2=?]
[luta=XIII | player1=25 | player2=26 | resultado_p1=? | resultado_p2=?]
[luta=XIV | player1=27 | player2=28 | resultado_p1=? | resultado_p2=?]
[luta=XV | player1=29 | player2=30 | resultado_p1=? | resultado_p2=?]
[luta=XVI | player1=31 | player2=32 | resultado_p1=? | resultado_p2=?]
[/fase]
[fase]
[luta=A | player1=I | player2=II | resultado_p1=? | resultado_p2=?]
[luta=B | player1=III | player2=IV | resultado_p1=? | resultado_p2=?]
[luta=C | player1=V | player2=VI | resultado_p1=? | resultado_p2=?]
[luta=D | player1=VII | player2=VIII | resultado_p1=? | resultado_p2=?]
[luta=E | player1=IX | player2=X | resultado_p1=? | resultado_p2=?]
[luta=F | player1=XI | player2=XII | resultado_p1=? | resultado_p2=?]
[luta=G | player1=XIII | player2=XIV | resultado_p1=? | resultado_p2=?]
[luta=H | player1=XV | player2=XVI | resultado_p1=? | resultado_p2=?]
[/fase]
[fase]
[luta=I | player1=A | player2=B | resultado_p1=? | resultado_p2=?]
[luta=II | player1=C | player2=D | resultado_p1=? | resultado_p2=?]
[luta=III | player1=E | player2=F | resultado_p1=? | resultado_p2=?]
[luta=IV | player1=G | player2=H | resultado_p1=? | resultado_p2=?]
[/fase]
[fase]
[luta=1 | player1=I | player2=II | resultado_p1=? | resultado_p2=?]
[luta=2 | player1=III | player2=IV | resultado_p1=? | resultado_p2=?]
[/fase]
[fase]
[luta=A | player1=1 | player2=2 | resultado_p1=? | resultado_p2=?]
[/fase]""" % (nome[0], nome[1], nome[2], nome[3], nome[4], nome[5], nome[6], nome[7], nome[8], nome[9], nome[10], nome[11], nome[12], nome[13], nome[14], nome[15],
              nome[16], nome[17], nome[18], nome[19], nome[20], nome[21], nome[22], nome[23], nome[24], nome[25], nome[26], nome[27], nome[28], nome[29], nome[30],
              nome[31], nome[32], nome[33], nome[34], nome[35], nome[36], nome[37], nome[38], nome[39], nome[40], nome[41], nome[42], nome[43], nome[44], nome[45],
              nome[46], nome[47], nome[48], nome[49], nome[50], nome[51], nome[52], nome[53], nome[54], nome[55], nome[56], nome[57], nome[58], nome[59], nome[60],
              nome[61], nome[62], nome[63])
        arq.write(chaves)
arq.close()
