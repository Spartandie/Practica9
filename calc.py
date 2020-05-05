
def sumar(a, b):
    c=a+b
    return c

def restar(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def div_int(a, b):#divison entera
    if b==0:
        print("Error")
        return
    return a//b

def div_float(a, b):#division de reales
    if b==0:
        print("Error")
        return
    return a/b

def modulo(a, b):
    if b==0:
        print("Error")
        return
    return a%b

def potencia(a, b):
    return a**b

def main():
    rep=1
    while rep==1:
        print("Ingresa dos valores")
        x= int(input())
        y= int(input())
        print("1. Sumar\n2. Restar\n3. Dividir (entero)")
        print("4. Dividir(Real)\n5. Modulo\n6. Potencia\n7. Mulitplicar\n8.Salir")

        op =int(input())
        if op == 1:
            print(sumar(x, y))
            print("Repetir programa? Si=1")
            rep=int(input())
        elif op==2:
            print(restar(x, y))
            print("Repetir programa? Si=1")
            rep=int(input())
        elif op==3:
            print(div_int(x, y))
            print("Repetir programa? Si=1")
            rep=int(input())
        elif op==4:
            print(div_float(x, y))
            print("Repetir programa? Si=1")
            rep=int(input())
        elif op==5:
            print(modulo(x, y))
            print("Repetir programa? Si=1")
            rep=int(input())
        elif op==6:
            print(potencia(x, y))
            print("Repetir programa? Si=1")
            rep=int(input())
        elif op==7:
            print(multiplicar(x, y))
            print("Repetir programa? Si=1")
            rep=int(input())
        elif op==8:
            return
        else:
            print("Opcion no valida\n\n")
            print("Repetir programa? Si=1")
            rep=int(input())

 
if __name__ == "__main__":
    main()



