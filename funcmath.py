def valida_number (n):
    if n.isnumeric(): return True
    else: return False

def fatorial (x):
    if x == 1: return 1
    else: return x * fatorial(x-1)

def randomfunc():
    inf = 0
    sup = 0
    from random import randint
    min = input('Digite o valor mínimo ou enter para sair: ')
    if valida_number(min):
        inf = int(min)
    else: return False
    max = input('Digite o valor máximo ou enter para sair: ')
    if valida_number(max):
        sup = int(max)
    else: return False
    return randint(inf, sup)

def ptc():
    base = input('Digite o valor da base ou enter para sair: ')
    if not valida_number(base): return False
    exp = input('Valor do expoente ou enter para sair: ')
    if not valida_number(exp): return False
    return int(base) ** int(exp)