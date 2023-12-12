# coding=utf-8
import math
import os

print ("equação")
def menu():
    os.system ("cls")
    esc = int(input("Escolha as equações:\n(1) Primeiro grau\n(2) Segundo grau\n(3) Sair\n-> "))
    if esc == 1:
        eq1()
    elif esc == 2:
        eq2()
    elif esc == 3:
        exit()
    else:
        os.system ("cls")
        print ("para de putaria cara")
        input()
        menu()
def eq1():
    # linear equation solver
    co_a = float(input("digite o coeficiente A: "))
    co_b = float(input("digite o coeficiente B: "))
    r = (-co_b) / co_a
    print (f"a raiz é: {r}")
    input()
    menu()

def eq2():
    # quadratic equation solver
    co_a = float(input("digite o coeficiente A: "))
    co_b = float(input("digite o coeficiente B: "))
    co_c = float(input("digite o coeficiente C: "))

    delta = (co_b ** 2) - (4 * co_a * co_c)
    if delta < 0:
        print (f" A equação {co_a}x^2+{co_b}x+{co_c}=0 não tem raízes reais")
        input()
        menu()
    elif delta == 0:
        x0 = (-co_b) / (2 * co_a)
        print (x0)
        input()
        menu()
    else:
        x1 = ((-co_b) + math.sqrt(delta)) / (2 * co_a)
        x2 = ((-co_b) - math.sqrt(delta)) / (2 * co_a)
        print (f"primeira raiz é {x1} e a segunda raíz é {x2}")
        input()
        menu()
menu() 
