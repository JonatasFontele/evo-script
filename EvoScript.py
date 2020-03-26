# -*- coding: utf-8 -*-
# Evo Bracket Sort Script created by Jony Walker.
# Script ordenador de chaves da Evo feito por Jony Walker.

file = open('entrada.txt', 'r')      #Abre e le um arquivo txt.
lista = file.readlines()             #Le todas as linhas salvas em file e salva na memória virtual de lista.
file = open('chaveamento.txt', 'w')  #Abre ou cria um arquivo txt para ser escrito.
number_of_lines = 0
name = []
                
for line in lista:                  #Iteracao.
        if line != "\n":            #Se a line nao for vazia, continue.
                number_of_lines += 1 #Contador.
                name.append(line)   #Adiciona cada linha a cada iteracao ao vetor 'name'.

if (number_of_lines <= 16): #Se quantidade de inscritos for menor ou igual a 16, imprima chave para 8 confrontos.
        while (number_of_lines < 16):
                name.append("ninguem")
                number_of_lines += 1
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
[/fase]""" % (name[0], name[1], name[2], name[3], name[4], name[5], name[6], name[7], name[8], name[9], name[10], name[11], name[12], name[13], name[14], name[15])
        file.write(chaves)
elif (16 < number_of_lines <= 32):             #Se quantidade de inscritos for maior que 16 e menor ou igual a 32, imprima chave para 16 confrontos.
        while (number_of_lines < 32):
                name.append("ninguem")
                number_of_lines += 1
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
[/fase]""" % (name[0], name[1], name[2], name[3], name[4], name[5], name[6], name[7], name[8], name[9], name[10], name[11], name[12], name[13], name[14], name[15],
              name[16], name[17], name[18], name[19], name[20], name[21], name[22], name[23], name[24], name[25], name[26], name[27], name[28], name[29], name[30],
              name[31])
        file.write(chaves)
else:                                   #Se quantidade de inscritos for maior do que 32, imprima chave para 32 confrontos.
        while (number_of_lines < 64):
                name.append("ninguem")
                number_of_lines += 1
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
[/fase]""" % (name[0], name[1], name[2], name[3], name[4], name[5], name[6], name[7], name[8], name[9], name[10], name[11], name[12], name[13], name[14], name[15],
              name[16], name[17], name[18], name[19], name[20], name[21], name[22], name[23], name[24], name[25], name[26], name[27], name[28], name[29], name[30],
              name[31], name[32], name[33], name[34], name[35], name[36], name[37], name[38], name[39], name[40], name[41], name[42], name[43], name[44], name[45],
              name[46], name[47], name[48], name[49], name[50], name[51], name[52], name[53], name[54], name[55], name[56], name[57], name[58], name[59], name[60],
              name[61], name[62], name[63])
        file.write(chaves)
file.close()
