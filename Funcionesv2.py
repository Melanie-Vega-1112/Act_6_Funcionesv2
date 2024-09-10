print ("mas sobre funciones")
# Aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s

# resta
def resta_cd(c,d):
    r=c-d
    return r 

# multiplicacion
def multiplicacion_ef(e,f):
    m=e*f
    return m

# Division
def division_gh(g,h):
    d=g/h
    return d

# llamadas a funciones
print("calculando suma")
n1=int(input("Ingresa el primer numero para sumarlo: "))
n2=int(input("Ingresa el segundo numero para sumarlo: "))
suma=suma_ab(n1,n2)
print(f"la suma de {n1} + {n2} es = {suma}")


# resta
n11=int(input("ingresa el primer numero para restarlo: "))
n22=int(input("ingresa el segundo numero para restarlo: "))
resta=resta_cd(n11, n22)
print(f"la resta de {n11} - {n22} es = {resta}")



# multiplicacion
n111=int(input("Ingresa el primer numero paara multiplicarlo: "))
n222=int(input("Ingresa el segundo numero para multiplicarlo: "))
multiplicacion=multiplicacion_ef(n111, n222)
print(f"la multiplicacion de {n111} * {n222} es:  {multiplicacion}")




# Division
n1111=int(input("ingresa el primer numero para dividirlo: "))
n2222=int(input("Ingresa el segundo numero para dividirlo: "))
division=division_gh(n1111, n2222)
print(f"division de {n1111} * {n2222} es:  {division}")