import math

def suma():
    try:
        r =a+b
    except ValueError:
        print('you have to enter an interger value')
    return r
def resta():
    try:
        r =a-b
    except ValueError:
        print('you have to enter an interger value')
    return r
def multi():
    try:
        r=a*b
    except ValueError:
        print('you have to enter an interger value')
    return r
def divi():
    try:
        r =a/b
    except ZeroDivisionError:
        print("Cannot divide by Zero")
    except ValueError:
        print('you have to enter an interger value')
    except:
        print('Failed¡¡¡')
    return r
def exp():
    try:
        r =math.pow(a,b)
    except ValueError:
        print('you have to enter an interger value')
    except:
        print('Failed¡¡¡')
    return r

listA = []
listB = []
listC = []
listRe = []
resolution = {}


while True:
    on = input('Siguiente presione ENTER , para salir 0')
    listA = []
    listB = []
    listC = []
    listRe = []
    resolution = {}
    try:
        if on == '':
            number_operation = 1
            print("*"*100)
            print("*"*45+"CALCULATOR"+"*"*45)
            try:
                a = float(input("Introduce un número A:  "))
                ope = int(input("Selecciona operación:\n+(1)\n-(2)\n*(3)\n/(4)\n^(5)\nResultados de operaciones(6):\n   "))
                b = float(input("Introduce un número B:  "))
                listA.append(a)
                listB.append(b)
            except ValueError:
                print('Introduce numero A/numero B y seleccione un numero para la operacion 1, 2,3,4,5')


            if ope == 1:
                C=listC.append('+')
                print("A=",a,'+',"B=",b,"=",suma())
                listRe.append(suma())
                for i in range(len(listA)):
                    resolution[listA[i],listC[i],listB[i]]=(listRe[i])
                    print('i',i,':',listA[i],listC[i],listB[i],"=",listRe[i])
                    print(resolution)

            elif ope == 2:
                C=listC.append('-')
                print("A=",a,'-',"B=",b,"=",resta())
                listRe.append(resta())
                for i in range(len(listA)):
                    resolution[listA[i],listC[i],listB[i]]=(listRe[i])
                    print('i',i,':',listA[i],listC[i],listB[i],"=",listRe[i])
            elif ope == 3:
                C=listC.append('*')
                print("A=",a,'*',"B=",b,"=",multi())
                listRe.append(multi())
                for i in range(len(listA)):
                    resolution[listA[i],listC[i],listB[i]]=(listRe[i])
                    print('i',i,':',listA[i],listC[i],listB[i],"=",listRe[i])
            elif ope == 4:

                C=listC.append('/')
                print("A=",a,'/',"B=",b,"=",divi())
                listRe.append(divi())
                for i in range(len(listA)):
                    resolution[listA[i],listC[i],listB[i]]=(listRe[i])
                    print('i',i,':',listA[i],listC[i],listB[i],"=",listRe[i])
            elif ope ==5:
                C=listC.append('^')
                print("A=",a,'^','B=',b,'=',exp())
                listRe.append(exp())
                for i in range(len(listA)):
                    resolution[listA[i],listC[i],listB[i]]=(listRe[i])
                    print('i',i,':',listA[i],listC[i],listB[i],"=",listRe[i])
            else:
                print('Selección de operacion no valida.')
    except:
        print('ERROR¡¡¡')
    print("*"*100)






