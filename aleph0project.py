# coding=ansi

'''
    Atualiza��es:
    Corre��o de portugu�s
    Corrigido bugs de consist�ncia como falta de limpeza de tela em certas ocasi�es
    Adicionado op��es de explica��o em todas as solu��es
    Resolvido crash caso n�o escreva nada no menu
'''

    # Project of basic mathematical tools with or without formulas.
    # It will be my first project to challenge myself.

    # Projeto de ferramentas matem�ticas b�sicas tendo ou n�o f�rmulas
    # Ser� meu primeiro projeto a ser feito para me desafiar

import os
import random
import math

def menu():
    os.system ('cls')
    print ("\n######################################\n\n >  Project Aleph-0 (prototype) <\n\n######################################")
    
    print ("\n\nVamos come�ar")
    opcao_menu = input("\n\nEscolha as fun��es do projeto ^^ :\n\n(1) N�mero aleat�rio\n\n(2) Potencia��o\n\n(3) Velocidade m�dia constante (em breve)\n\n(4) Equa��o do primeiro grau\n\n(5) Equa��o do segundo grau\n\n-> ")
    if not opcao_menu:
        print ("\n\nVoc� n�o digitou nada")
        input()
        os.system('cls')
        menu()
    elif opcao_menu == '1':
        os.system('cls')
        randomfunc()
    elif opcao_menu == '2':
        os.system('cls')
        ptc_func()
    elif opcao_menu == '3':
        os.system('cls')
        vmc_func()
    elif opcao_menu == '4':
        os.system('cls')
        eq1()
    elif opcao_menu == '5':
        os.system('cls')
        eq2()
    else:
        print ("Para com isso cara")
        input()
        os.system('cls')
        menu()

def randomfunc():

    # Random numbers programming

    # Programa��o de n�meros aleat�rios

    rm1 = int(input("\n\nQual n�mero m�nimo para escolher?\n\n-> "))
    rm2 = int(input("\n\nQual n�mero m�ximo para escolher?\n\n-> "))
    print(f"\n\nEu escolho:\n-> {random.randint(rm1, rm2)}")
    rmopcao = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> ")
    if not rmopcao:
        print ("\n\nVoc� n�o digitou nada")
        input()
        os.system('cls')
        randomfunc()

    elif rmopcao == '1':
        os.system('cls')
        randomfunc()
    elif rmopcao == '2':
        os.system('cls')
        menu()
    elif rmopcao == '3':
         exit()
    else:
        input("\n\nvoc� � muito burro cara")
        randomfunc()

def ptc_func():

    # Potentiation programming

    # Programa��o de potencia��o

    ptcbase = float(input("\nqual o n�mero base?\n\n-> "))
    ptcexp = float(input("\nqual o expoente?\n\n-> "))
    ptcbase_exp = (ptcbase ** ptcexp)
    print (f"\n\nA resposta �: {ptcbase_exp}")
    ptcfinal = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
    if not ptcfinal:
        print ("\n\nVoc� n�o digitou nada")
        input()
        os.system('cls')
        ptc_func()
    elif ptcfinal == '1':
        os.system('cls')
        ptc_func()
    elif ptcfinal == '2':
        os.system('cls')
        menu()
    elif ptcfinal == '3':
        exit()
    elif ptcfinal == '4':
        os.system('cls')
        calculo = str(ptcbase)
        for i in range(int(ptcexp) - 1):
            calculo += " * " + str(ptcbase)
        print(f"Simples! Na potencia��o, a base que voc� escolheu � multiplicada por si mesma e o expoente s�o as vezes que a base � multiplicada.\n\nExemplo: {calculo}")
        input()
        os.system('cls')
        ptcfinal = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> ")
        if ptcfinal == '1':
            os.system('cls')
            ptc_func()
        elif ptcfinal == '2':
            os.system('cls')
            menu()
        elif ptcfinal == '3':
            exit()
        else:
            input("\n\nvoc� � muito burro cara")
            exit()

def vmc_func():

    # Constant average speed programming

    # Programa��o da velocidade m�dia constante

    grandeza = input("Voc� quer descobrir qual grandeza?:\n\n(1) Velocidade\n\n(2) Tempo\n\n(3) Dist�ncia (em breve)\n\n-> ")
    if not grandeza:
        print ("\n\nVoc� n�o digitou nada")
        input()
        os.system('cls')
        vmc_func()
    elif grandeza == '1':
        os.system('cls')
        velocidade_distancia = float(input("Qual o tempo em segundos?\n\n-> "))
        tempo_distancia = float(input("Qual a distancia em metros?\n\n-> "))
        t_resultado_m = (velocidade_distancia / tempo_distancia)
        t_resultado_km = (t_resultado_m * 3.6)
        print ("A resposta em m/s �:", t_resultado_m,"\nAgora em Km/h �:", t_resultado_km)
        vmcfinal_v = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
        if not vmcfinal_v:
            print ("\n\nVoc� n�o digitou nada")
            input()
            os.system('cls')
            vmc_func()
        elif vmcfinal_v == '1':
            os.system('cls')
            vmc_func()
        elif vmcfinal_v == '2':
            os.system('cls')
            menu()
        elif vmcfinal_v == '3':
            exit()
        elif vmcfinal_v == '4':
            os.system('cls')
            print (f"Simples! Para descobrir a velocidade, devemos dividir o tempo em segundos pela dist�ncia em metros\nSendo que Vm = {velocidade_distancia} / {tempo_distancia}\nDando a resposta abaixo:\n\nm/s -> {t_resultado_m}\nkm/h -> {t_resultado_m} x 3.6 = {t_resultado_km}")
            input()
            os.system('cls')
            vmcfinal_v = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> ")
            if not vmcfinal_v:
                print ("\n\nVoc� n�o digitou nada")
                input()
                os.system('cls')
                vmc_func()
            elif vmcfinal_v == '1':
                os.system('cls')
                vmc_func()
            elif vmcfinal_v == '2':
                os.system('cls')
                menu()
            elif vmcfinal_v == '3':
                exit()
    elif grandeza == '2':
        os.system('cls')
        velocidade_tempo = float(input("qual a velocidade em m/s?\n\n-> "))
        distancia_tempo = float(input("Qual a distancia em metros?\n\n-> "))
        t_resultado_segundos = (distancia_tempo / velocidade_tempo)
        t_resultado_minutos = (t_resultado_segundos / 60)
        t_resultado_horas = (t_resultado_segundos / 3600)
        print (f"A resposta em segundos �: {t_resultado_segundos}\nEm minutos �: {t_resultado_minutos}\nAgora em horas �: {t_resultado_horas}")
        vmcfinal_t = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
        if not vmcfinal_t:
            print ("\n\nVoc� n�o digitou nada")
            input()
            os.system('cls')
            vmc_func()
        elif vmcfinal_t == '1':
            os.system('cls')
            vmc_func()
        elif vmcfinal_t == '2':
            os.system('cls')
            menu()
        elif vmcfinal_t == '3':
            exit()
        elif vmcfinal_t == '4':
            os.system('cls')
            print (f"Simples! Para descobrir o tempo, devemos dividir a velocidade em m/s pela dist�ncia em metros\nSendo que T = {distancia_tempo} / {velocidade_tempo}\nDando a resposta abaixo:\n\nsegundos -> {t_resultado_segundos}\nminutos -> {t_resultado_segundos} / 60 = {t_resultado_minutos}\nhoras -> {t_resultado_segundos} / 3600 = {t_resultado_horas}")
            input()
            os.system('cls')
            vmcfinal_t = (input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> "))
            if vmcfinal_t == '1':
                os.system('cls')
                vmc_func()
            elif vmcfinal_t == '2':
                os.system('cls')
                menu()
            elif vmcfinal_t == '3':
                exit()
            else:
                input("\n\nvoc� � muito burro cara")
                exit()
    elif grandeza == '3':
        os.system('cls')
        velocidade_distancia = float(input("Qual a velocidade em m/s?\n\n-> "))
        tempo_distancia = float(input("Qual o tempo em segundos?\n\n-> "))
        t_resultado_m = (velocidade_distancia * tempo_distancia)
        t_resultado_km = (t_resultado_m / 1000)
        print ("A resposta em metros �:", t_resultado_m,"\nAgora em km �:", t_resultado_km)
        vmcfinal_v = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
        if not vmcfinal_v:
            print ("\n\nVoc� n�o digitou nada")
            input()
            os.system('cls')
            vmc_func()
        elif vmcfinal_v == '1':
            os.system('cls')
            vmc_func()
        elif vmcfinal_v == '2':
            os.system('cls')
            menu()
        elif vmcfinal_v == '3':
            exit()
        elif vmcfinal_v == '4':
            os.system('cls')
            print (f"Simples! Para descobrir a dist�ncia, devemos multiplicar a velocidade pelo tempo\nSendo que Dm = {velocidade_distancia} * {tempo_distancia}\nDando a resposta abaixo:\n\nmetros -> {t_resultado_m}\nkm -> {t_resultado_m} / 1000 = {t_resultado_km}")
            input()
            os.system('cls')
            vmcfinal_v = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> ")
            if not vmcfinal_v:
                print ("\n\nVoc� n�o digitou nada")
                input()
                os.system('cls')
                vmc_func()
            elif vmcfinal_v == '1':
                os.system('cls')
                vmc_func()
            elif vmcfinal_v == '2':
                os.system('cls')
                menu()
            elif vmcfinal_v == '3':
                exit()

def eq1():

    # linear equation solver

    # solu��o de equa��o linear

    co_a = float(input("digite o coeficiente A: "))
    co_b = float(input("digite o coeficiente B: "))
    r = (-co_b) / co_a
    print (f"A raiz �: {r}")
    eq1final = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
    if not eq1final:
        print ("\n\nVoc� n�o digitou nada")
        input()
        os.system('cls')
        eq1()
    elif eq1final == '1':
        os.system('cls')
        eq1()
    elif eq1final == '2':
        os.system('cls')
        menu()
    elif eq1final == '3':
        exit()
    elif eq1final == '4':
        os.system('cls')
        print(f"\n\nEsta � uma equa��o do primeiro grau (linear) do tipo ax + b = 0, onde 'a' � o coeficiente de x e 'b' � uma constante.\nA solu��o para essa equa��o � dada por x = -b/a.\nNo caso, {co_a} � o coeficiente 'a' e {co_b} � a constante 'b'.\nA raiz 'r' � calculada como r = {-co_b}/{co_a}, que � a solu��o da equa��o")
        input()
        os.system('cls')
        op_eq1 = int(input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> "))
        if op_eq1 == 1:
            os.system('cls')
            eq1()
        elif op_eq1 == 2:
            os.system('cls')
            menu()
        elif op_eq1 == 3:
            exit()
        else:
            input("\n\nvoc� � muito burro cara")
            exit()

    else:
        input("\n\nvoc� � muito burro cara")
        exit()

def eq2():

    # quadratic equation solver

    # solu��o de equa��o quadr�tica
    
    co_a = float(input("digite o coeficiente A: "))
    co_b = float(input("digite o coeficiente B: "))
    co_c = float(input("digite o coeficiente C: "))

    delta = (co_b ** 2) - (4 * co_a * co_c)
    if delta < 0:
        print ("\n\nA equa��o n�o tem raizes reais")
        op_eq2 = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
        if not op_eq2:
            print ("\n\nVoc� n�o digitou nada")
            input()
            os.system('cls')
            eq2()
        elif op_eq2 == '1':
            os.system('cls')
            eq2()
        elif op_eq2 == '2':
            os.system('cls')
            menu()
        elif op_eq2 == '3':
            exit()
        elif op_eq2 == '4':
            os.system('cls')
            print("\n\nA equa��o � uma equa��o quadr�tica do tipo ax^2 + bx + c = 0.\nOnde 'a' � o coeficiente de x^2, 'b' � o coeficiente de x e 'c' � uma constante.\nO 'delta' � calculado como b^2 - 4ac. Se o delta � menor que zero, a equa��o n�o tem ra�zes reais.")
            input()
            os.system('cls')
            op_eq2 = int(input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> "))
            if op_eq2 == 1:
                os.system('cls')
                eq2()
            elif op_eq2 == 2:
                os.system('cls')
                menu()
            elif op_eq2 == 3:
                exit()
            else:
                input("\n\nvoc� � muito burro cara")
                exit()
        else:
            input("\n\nvoc� � muito burro cara")
            exit()

    elif delta == 0:
        x0 = (-co_b) / (2 * co_a)
        print (f'\n\nA �nica raiz � essa: {x0}')
        op_eq2 = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
        if not op_eq2:
            print ("\n\nVoc� n�o digitou nada")
            input()
            os.system('cls')
            eq2()
        elif op_eq2 == '1':
            os.system('cls')
            eq2()
        elif op_eq2 == '2':
            os.system('cls')
            menu()
        elif op_eq2 == '3':
            exit()
        elif op_eq2 == '4':
            os.system('cls')
            print ("\n\nA equa��o � uma equa��o quadr�tica do tipo ax^2 + bx + c = 0.\nOnde 'a' � o coeficiente de x^2, 'b' � o coeficiente de x e 'c' � uma constante.\nO 'delta' � calculado como b^2 - 4ac. Se o delta � igual a zero, a equa��o tem uma �nica raiz real, que � calculada como x = -b/2a.")
            input()
            os.system('cls')
            op_eq2 = int(input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> "))
            if op_eq2 == 1:
                os.system('cls')
                eq2()
            elif op_eq2 == 2:
                os.system('cls')
                menu()
            elif op_eq2 == 3:
                exit()
            else:
                input("\n\nvoc� � muito burro cara")
                exit()
        else:
            input("\n\nvoc� � muito burro cara")
            exit()
    else:
        x1 = ((-co_b) + math.sqrt(delta)) / (2 * co_a)
        x2 = ((-co_b) - math.sqrt(delta)) / (2 * co_a)
        print (f"\n\nPrimeira raiz � {x1} e a Segunda raiz � {x2}")
        op_eq2 = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
        if not op_eq2:
            print ("\n\nVoc� n�o digitou nada")
            input()
            os.system('cls')
            eq2()
        elif op_eq2 == '1':
            os.system('cls')
            eq2()
        elif op_eq2 == '2':
            os.system('cls')
            menu()
        elif op_eq2 == '3':
            exit()
        elif op_eq2 == '4':
            os.system('cls')
            print ("\n\nA equa��o � uma equa��o quadr�tica do tipo ax^2 + bx + c = 0.\nOnde 'a' � o coeficiente de x^2, 'b' � o coeficiente de x e 'c' � uma constante.\nO 'delta' � calculado como b^2 - 4ac. Se o delta � maior que zero, a equa��o tem duas ra�zes reais, que s�o calculadas como x1 = -b + raiz de delta / 2a e x2 = -b - raiz de delta /2a.")
            input()
            os.system('cls')
            op_eq2 = int(input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> "))
            if op_eq2 == 1:
                os.system('cls')
                eq2()
            elif op_eq2 == 2:
                os.system('cls')
                menu()
            elif op_eq2 == 3:
                exit()
            else:
                input("\n\nvoc� � muito burro cara")
                exit()
        else:
            input("\n\nvoc� � muito burro cara")
            exit()
menu()