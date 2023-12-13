# coding=ansi
import os
import random
import math

def menu():
    print ("\n######################################\n\n >  Project Aleph-0 (prototype) <\n\n######################################")

    """
    Projeto de ferramentas matem�ticas b�sicas tendo ou n�o f�rmulas
    Ser� meu primeiro projeto a ser feito para me desafiar
    """
    print ("\n\nVamos come�ar")
    fun = int(input("\n\nEscolha as fun��es do projeto ^^ :\n\n(1) aleat�rio\n\n(2) Potencia��o\n\n(3) Velocidade m�dia constante (em breve)\n\n(4) Equa��o do primeiro grau\n\n(5) Equa��o do segundo grau\n\n-> "))
    if fun == 1:
        os.system('cls')
        rmf()
    elif fun == 2:
        os.system('cls')
        ptc()
    elif fun == 3:
        os.system('cls')
        vmc()
    elif fun == 4:
        os.system('cls')
        eq1()
    elif fun == 5:
        os.system('cls')
        eq2()
    else:
        print ("Para com isso cara")
        input()
        menu()

"""
Programa��o de n�mero aleat�rio
(FUNCIONOU KCT :D)
"""
def rmf():
    rm1 = int(input("\nqual n�mero m�nimo para escolher?\n\n-> "))
    rm2 = int(input("\nqual n�mero m�ximo para escolher?\n\n-> "))
    print("\n\neu escolho:\n->",random.randint(rm1, rm2))
    rmfinal = int(input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> "))
    if rmfinal == 1:
        os.system('cls')
        rmf()
    elif rmfinal == 2:
        os.system('cls')
        menu()
    elif rmfinal == 3:
         exit()
    else:
        input("\n\nvoc� � muito burro cara")
        exit()

def ptc():
    ptcbase = float(input("\nqual o n�mero base?\n\n-> "))
    ptcexp = float(input("\nqual o expoente?\n\n-> "))
    pctbaxp = (ptcbase ** ptcexp)
    print ("\n\nA resposta �: ", pctbaxp)
    pctfinal = int(input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> "))
    if pctfinal == 1:
        os.system('cls')
        ptc()
    elif pctfinal == 2:
        os.system('cls')
        menu()
    elif pctfinal == 3:
        exit()
    else:
        input("\n\nvoc� � muito burro cara")
        exit()

def vmcfinal():
    vmcf = int(input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> "))
    if vmcf == 1:
        os.system('cls')
        vmc()
    elif vmcf == 2:
        os.system('cls')
        menu()
    elif vmcf == 3:
        exit()
    else:
        input("\n\nvoc� � muito burro cara")
        exit()

def vmc():
    desc = int(input("Voc� quer descobrir qual grandeza?:\n\n(1) Velocidade\n\n(2) Tempo\n\n(3) Dist�ncia (em breve)\n\n-> "))
    if desc == 1:
        os.system('cls')
        tv = float(input("qual o tempo em segundos?\n\n-> "))
        dv = float(input("Qual a distancia em metros?\n\n-> "))
        vrms = (tv / dv)
        vrkmh = (vrms * 3.6)
        print ("A resposta em m/s �:", vrms,"\nAgora em Km/h �:", vrkmh)
        vmcfinal()
    if desc == 2:
        dt = float(input("qual a velocidade em m/s?\n\n-> "))
        vt = float(input("Qual a distancia em metros?\n\n-> "))
        trs = (vt / dt)
        trm = (trs / 60)
        trh = (trs / 3600)
        print (f"A resposta em segundos �: {trs}\nEm minutos �: {trm}\nAgora em horas �: {trh}")
        vmcfinal()

def eq1():
    """
    linear equation solver
    solu��o de equa��o linear
    """
    co_a = float(input("digite o coeficiente A: "))
    co_b = float(input("digite o coeficiente B: "))
    r = (-co_b) / co_a
    print (f"a raiz �: {r}")
    eqfinal = int(input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> "))
    if eqfinal == 1:
        os.system('cls')
        eq1()
    elif eqfinal == 2:
        os.system('cls')
        menu()
    elif eqfinal == 3:
        exit()
    else:
        input("\n\nvoc� � muito burro cara")
        exit()

def eq2():
    """
    quadratic equation solver
    solu��o de equa��o quadr�tica
    """
    def eqfinal():
        eqfinal = int(input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> "))
        if eqfinal == 1:
            os.system('cls')
            eq2()
        elif eqfinal == 2:
            os.system('cls')
            menu()
        elif eqfinal == 3:
            exit()
        else:
            input("\n\nvoc� � muito burro cara")
            exit()

    co_a = float(input("digite o coeficiente A: "))
    co_b = float(input("digite o coeficiente B: "))
    co_c = float(input("digite o coeficiente C: "))

    delta = (co_b ** 2) - (4 * co_a * co_c)
    if delta < 0:
        print ("A equa��o n�o tem raizes reais")
        eqfinal()
    elif delta == 0:
        x0 = (-co_b) / (2 * co_a)
        print (x0)
        eqfinal()
    else:
        x1 = ((-co_b) + math.sqrt(delta)) / (2 * co_a)
        x2 = ((-co_b) - math.sqrt(delta)) / (2 * co_a)
        print (f"primeira raiz � {x1} e a segunda ra�z � {x2}")
        eqfinal()
menu()
