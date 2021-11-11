#!/usr/bin/env python
# coding: utf-8

# ## Manifesto do TPC4
# * **Identificador:** Algoritmos e Técnicas de Programação
# * **Título:** Calculadora de Frações
# * **Data de início:** 2021-11-09
# * **Data de fim:** 2021-11-11
# * **Supervisor:** José Carlos Leite Ramalho, jcr@di.uminho.pt
# * **Autor:** Amanda Maria de Melo Vieira, A88312
# * **Resumo:** Neste trabalho é pretendida a criação de um aplicativo de manipulação de frações, contendo as operações soma, subtração, multiplicação e divisão.

# In[3]:


import math
n1 = int(input("Insira o primeiro numerador: 1\n"))
d1 = int(input("Insira o primeiro denominador: 1\n"))
n2 = int(input("Insira o segundo numerador: 2\n"))
d2 = int(input("Insira o segundo denominador: 2\n"))
operacao = input("1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n0 - Sair\n")

if(operacao == "1"):
    # esmo denominador
    if(d1 == d2):
        numerador = n1+n2
        denominador = d1
        
    # denominador diferente
    else:
        numerador = (n1*d2)+(n2*d1)
        denominador = d1*d2
        
    # divisor comum
    div_comum = math.gcd(numerador,denominador)
    numerador = numerador//div_comum
    denominador = denominador//div_comum

    # resultado 
    fracao = str(numerador)+"/"+str(denominador)
    print("O resultado da operação é "+fracao)

elif(operacao == "2"):
    # mesmo denominador
    if(d1 == d2):
        numerador = n1-n2
        denominador = d1
        
    # denominador diferente
    else:
        numerador = (n1*d2)-(n2*d1)
        denominador = d1*d2
        
    # se possui um divisor comum
    div_comum = math.gcd(numerador,denominador)
    numerador = numerador//div_comum
    denominador = denominador//div_comum

    # Resultado 
    fracao = str(numerador)+"/"+str(denominador)
    print("O resultado da operação é "+fracao)

elif (operacao == "3"):
    numerador = n1*n2
    denominador = d1*d2

    # divisor comum
    div_comum = math.gcd(numerador,denominador)
    numerador = numerador//div_comum
    denominador = denominador//div_comum

    # Resultado 
    fracao = str(numerador)+"/"+str(denominador)
    print("O resultado da operação é "+fracao)

elif (operacao == "4"):
    numerador = n1*d2
    denominador = n2*d1

    # divisor comum
    div_comum = math.gcd(numerador,denominador)
    numerador = numerador//div_comum
    denominador = denominador//div_comum

    # Resultado 
    fracao = str(numerador)+"/"+str(denominador)
    print("O resultado da operação é "+fracao)

else:
    print("Operação Interrompida")


# In[ ]:




