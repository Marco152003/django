from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hola mundo</h1>")

def about(request):
    return HttpResponse("Hola profesor")
def suma(request):
    #Suma de los 20 primeros números
    n=20
    acum=0
    for i in range (n+1):
        acum=acum+i

    return render(request,"ejercicio1.html",{"suma":acum})
def factorial(request):
    #El factorial de 10
    numero=10
    fact=1
    for i in range(1,numero+1):
        fact=fact*i
    
    return render(request,"ejercicio2.html",{"factorial":fact})
def promedio(request):
    #El promedio aritmético de los 10 primeros números
    numero=10
    acum=0
    for i in range(numero+1):
        acum=acum+i
    prom=acum/10

    return render(request,"ejercicio3.html",{"promedio":prom})
def geo(request):
    #El promedio geométrico de los 10 primeros números
    n=10
    acum=1
    for i in range(1,n+1):
        acum=acum*i
    pt=acum**(1/10)

    return render(request,"ejercicio4.html",{"tabla":pt})
def ejercicio(request): 
    #La multiplicación de la inversa de los 5 primeros numeros 
    numero=5
    multi=1
    for i in range(1,numero+1):
        multi=multi*i
    resul=1/(multi)

    return render(request,"ejercicio5.html",{"ejercicio":resul})
def ejer6(request):
    #Suma de los 20 primeros numeros usando while
    n=0
    i=0
    while i<20:
        i=i+1
        n=n+i
    return render(request,"ejercicio6.html",{"ejer6":n})
def ejer7(request):
    #Factorial de 10 usando while
    n=1
    i=0
    while i<10:
        i=i+1
        n=n*i
    return render(request,"ejercicio7.html",{"ejer7":n})
def ejer8(request):
    #Promedio aritmetico de los 10 primeros numeros usando while 
    n=0
    i=0
    while i<10:
        i=i+1
        n=n+i
        prom=n/10
    return render(request,"ejercicio8.html",{"ejer8":prom})
def ejer9(request):
    #Promedio geometrico de los 10 primeros numeros usando while 
    n=1
    i=0
    while i<10:
        i=i+1
        n=n*i
        geo=n**(1/10)
    return render(request,"ejercicio9.html",{"ejer9":geo})
def ejer10(request):
    #La inversa de la multiplicación de los 5 primeros números usando while
    n=1
    i=0
    while i<5:
        i=i+1
        n=n*i
        inver=1/(n)
    return render(request,"ejercicio10.html",{"ejer10":inver})
def ejer11(request):
    #Suma de los 10 primeros números usando do while
    acum=0
    i=1
    while True:
        acum=acum+i
        i=i+1
        if i>10:
          break
    print (acum)
    return render(request,"ejercicio11.html",{"ejercicio11":acum})
def ejer12(request):
    #Factorial de 10 usando do while
    fact=1
    i=1
    while True:
        fact=fact*i
        i=i+1
        if i>10:
            break
    print(fact)
    return render(request,"ejercicio12.html",{"ejer12":fact})
def ejer13(request):
    #Promedio aritmetico de los 10 primeros números usando do while
    acum=0
    i=1
    while True:
        acum=acum+i
        i=i+1
        if i>10:
          break
    print (acum)
    prom=acum/10
    return render(request,"ejercicio13.html",{"ejer13":prom})
def ejer14(request):
    #Promedio Geométrico de los 10 primeros numeros usando do while
    fact=1
    i=1
    while True:
        fact=fact*i
        i=i+1
        if i>10:
            break
    print(fact)
    geom=fact**(1/10)
    return render(request,"ejercicio14.html",{"ejer14":geom})
def ejer15(request):
    #La inversa de la multiplicación de los 5 primeros numeros usando do while
    mult=1
    i=1
    while True:
        mult=mult*i
        i=i+1
        if i>5:
            break
    print(mult)
    inver=1/(mult)
    return render(request,"ejercicio15.html",{"ejer15":inver})

