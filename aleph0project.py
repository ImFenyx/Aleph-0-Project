# coding=ansi

'''
    Atualizações:
    Correção de português
    Corrigido bugs de consistência como falta de limpeza de tela em certas ocasiões
    Adicionado opções de explicação em todas as soluções
    Resolvido crash caso não escreva nada no menu
'''

    # Project of basic mathematical tools with or without formulas.
    # It will be my first project to challenge myself.

    # Projeto de ferramentas matemáticas básicas tendo ou não fórmulas
    # Será meu primeiro projeto a ser feito para me desafiar

import os
import random
import math

def menu():
    os.system ('cls')
    print ("\n######################################\n\n >  Project Aleph-0 (prototype) <\n\n######################################")
    
    print ("\n\nVamos começar")
    opcao_menu = input("\n\nEscolha as funções do projeto ^^ :\n\n(1) Número aleatório\n\n(2) Potenciação\n\n(3) Velocidade média constante (em breve)\n\n(4) Equação do primeiro grau\n\n(5) Equação do segundo grau\n\n-> ")
    if not opcao_menu:
        print ("\n\nVocê não digitou nada")
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

    # Programação de números aleatórios

    rm1 = int(input("\n\nQual número mínimo para escolher?\n\n-> "))
    rm2 = int(input("\n\nQual número máximo para escolher?\n\n-> "))
    print(f"\n\nEu escolho:\n-> {random.randint(rm1, rm2)}")
    rmopcao = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> ")
    if not rmopcao:
        print ("\n\nVocê não digitou nada")
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
        input("\n\nvocê é muito burro cara")
        randomfunc()

def ptc_func():

    # Potentiation programming

    # Programação de potenciação

    ptcbase = float(input("\nqual o número base?\n\n-> "))
    ptcexp = float(input("\nqual o expoente?\n\n-> "))
    ptcbase_exp = (ptcbase ** ptcexp)
    print (f"\n\nA resposta é: {ptcbase_exp}")
    ptcfinal = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
    if not ptcfinal:
        print ("\n\nVocê não digitou nada")
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
        print(f"Simples! Na potenciação, a base que você escolheu é multiplicada por si mesma e o expoente são as vezes que a base é multiplicada.\n\nExemplo: {calculo}")
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
            input("\n\nvocê é muito burro cara")
            exit()

def vmc_func():

    # Constant average speed programming

    # Programação da velocidade média constante

    grandeza = input("Você quer descobrir qual grandeza?:\n\n(1) Velocidade\n\n(2) Tempo\n\n(3) Distância (em breve)\n\n-> ")
    if not grandeza:
        print ("\n\nVocê não digitou nada")
        input()
        os.system('cls')
        vmc_func()
    elif grandeza == '1':
        os.system('cls')
        velocidade_distancia = float(input("Qual o tempo em segundos?\n\n-> "))
        tempo_distancia = float(input("Qual a distancia em metros?\n\n-> "))
        t_resultado_m = (velocidade_distancia / tempo_distancia)
        t_resultado_km = (t_resultado_m * 3.6)
        print ("A resposta em m/s é:", t_resultado_m,"\nAgora em Km/h é:", t_resultado_km)
        vmcfinal_v = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
        if not vmcfinal_v:
            print ("\n\nVocê não digitou nada")
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
            print (f"Simples! Para descobrir a velocidade, devemos dividir o tempo em segundos pela distância em metros\nSendo que Vm = {velocidade_distancia} / {tempo_distancia}\nDando a resposta abaixo:\n\nm/s -> {t_resultado_m}\nkm/h -> {t_resultado_m} x 3.6 = {t_resultado_km}")
            input()
            os.system('cls')
            vmcfinal_v = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> ")
            if not vmcfinal_v:
                print ("\n\nVocê não digitou nada")
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
        print (f"A resposta em segundos é: {t_resultado_segundos}\nEm minutos é: {t_resultado_minutos}\nAgora em horas é: {t_resultado_horas}")
        vmcfinal_t = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
        if not vmcfinal_t:
            print ("\n\nVocê não digitou nada")
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
            print (f"Simples! Para descobrir o tempo, devemos dividir a velocidade em m/s pela distância em metros\nSendo que T = {distancia_tempo} / {velocidade_tempo}\nDando a resposta abaixo:\n\nsegundos -> {t_resultado_segundos}\nminutos -> {t_resultado_segundos} / 60 = {t_resultado_minutos}\nhoras -> {t_resultado_segundos} / 3600 = {t_resultado_horas}")
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
                input("\n\nvocê é muito burro cara")
                exit()
    elif grandeza == '3':
        os.system('cls')
        velocidade_distancia = float(input("Qual a velocidade em m/s?\n\n-> "))
        tempo_distancia = float(input("Qual o tempo em segundos?\n\n-> "))
        t_resultado_m = (velocidade_distancia * tempo_distancia)
        t_resultado_km = (t_resultado_m / 1000)
        print ("A resposta em metros é:", t_resultado_m,"\nAgora em km é:", t_resultado_km)
        vmcfinal_v = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
        if not vmcfinal_v:
            print ("\n\nVocê não digitou nada")
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
            print (f"Simples! Para descobrir a distância, devemos multiplicar a velocidade pelo tempo\nSendo que Dm = {velocidade_distancia} * {tempo_distancia}\nDando a resposta abaixo:\n\nmetros -> {t_resultado_m}\nkm -> {t_resultado_m} / 1000 = {t_resultado_km}")
            input()
            os.system('cls')
            vmcfinal_v = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n-> ")
            if not vmcfinal_v:
                print ("\n\nVocê não digitou nada")
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

    # solução de equação linear

    co_a = float(input("digite o coeficiente A: "))
    co_b = float(input("digite o coeficiente B: "))
    r = (-co_b) / co_a
    print (f"A raiz é: {r}")
    eq1final = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
    if not eq1final:
        print ("\n\nVocê não digitou nada")
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
        print(f"\n\nEsta é uma equação do primeiro grau (linear) do tipo ax + b = 0, onde 'a' é o coeficiente de x e 'b' é uma constante.\nA solução para essa equação é dada por x = -b/a.\nNo caso, {co_a} é o coeficiente 'a' e {co_b} é a constante 'b'.\nA raiz 'r' é calculada como r = {-co_b}/{co_a}, que é a solução da equação")
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
            input("\n\nvocê é muito burro cara")
            exit()

    else:
        input("\n\nvocê é muito burro cara")
        exit()

def eq2():

    # quadratic equation solver

    # solução de equação quadrática
    
    co_a = float(input("digite o coeficiente A: "))
    co_b = float(input("digite o coeficiente B: "))
    co_c = float(input("digite o coeficiente C: "))

    delta = (co_b ** 2) - (4 * co_a * co_c)
    if delta < 0:
        print ("\n\nA equação não tem raizes reais")
        op_eq2 = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
        if not op_eq2:
            print ("\n\nVocê não digitou nada")
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
            print("\n\nA equação é uma equação quadrática do tipo ax^2 + bx + c = 0.\nOnde 'a' é o coeficiente de x^2, 'b' é o coeficiente de x e 'c' é uma constante.\nO 'delta' é calculado como b^2 - 4ac. Se o delta é menor que zero, a equação não tem raízes reais.")
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
                input("\n\nvocê é muito burro cara")
                exit()
        else:
            input("\n\nvocê é muito burro cara")
            exit()

    elif delta == 0:
        x0 = (-co_b) / (2 * co_a)
        print (f'\n\nA única raiz é essa: {x0}')
        op_eq2 = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
        if not op_eq2:
            print ("\n\nVocê não digitou nada")
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
            print ("\n\nA equação é uma equação quadrática do tipo ax^2 + bx + c = 0.\nOnde 'a' é o coeficiente de x^2, 'b' é o coeficiente de x e 'c' é uma constante.\nO 'delta' é calculado como b^2 - 4ac. Se o delta é igual a zero, a equação tem uma única raiz real, que é calculada como x = -b/2a.")
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
                input("\n\nvocê é muito burro cara")
                exit()
        else:
            input("\n\nvocê é muito burro cara")
            exit()
    else:
        x1 = ((-co_b) + math.sqrt(delta)) / (2 * co_a)
        x2 = ((-co_b) - math.sqrt(delta)) / (2 * co_a)
        print (f"\n\nPrimeira raiz é {x1} e a Segunda raiz é {x2}")
        op_eq2 = input("\n\nQuer continuar?\n\n(1) Sim\n\n(2) Voltar para o menu\n\n(3) Sair\n\n(4) Me explique\n\n-> ")
        if not op_eq2:
            print ("\n\nVocê não digitou nada")
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
            print ("\n\nA equação é uma equação quadrática do tipo ax^2 + bx + c = 0.\nOnde 'a' é o coeficiente de x^2, 'b' é o coeficiente de x e 'c' é uma constante.\nO 'delta' é calculado como b^2 - 4ac. Se o delta é maior que zero, a equação tem duas raízes reais, que são calculadas como x1 = -b + raiz de delta / 2a e x2 = -b - raiz de delta /2a.")
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
                input("\n\nvocê é muito burro cara")
                exit()
        else:
            input("\n\nvocê é muito burro cara")
            exit()
menu()