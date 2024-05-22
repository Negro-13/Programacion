print('Cuantas sublistas desea ingrezar:')
cantsublist = int(input())
finlist = []
def createlist(cantsublist):
    print('Ingrese la clave')
    clave = int(input())
    if clave != -1:
        print('Clave incorrecta, ingrese clave otra vez:')
        clave = int(inpu())
    else:
        for i in range(cantsublist):
            print('Cantidad de numeros que quiera ingresar en la sublista ' + str(i))
            numssublist = int(input())
            list = []
            finlist.append(list)
            for j in range(numssublist):
                print('Ingrese un numero:')
                num = int(input())
                list.append(num)
    return finlist

print('Su lista es: ' + str(createlist(cantsublist)))
