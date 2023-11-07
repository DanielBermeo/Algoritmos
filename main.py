# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def empacar(objetos, bolsas, w_max):
    bolsas_final=[]
    #objetos = objetos.sort(reverse = True)
    i = len(objetos)
    inx_disp = []

    # Encuentra las bolsas aun no llenas
    j = 0
    for x in bolsas:
        if(x < w_max):
            inx_disp.append(j)
        j += 1

   #Condicion de salida
    print(bolsas)
    if i == 0:
        return bolsas_final

    objeto = objetos[0]
    bolsa_act = encontrar_indice(w_max, objeto, inx_disp, bolsas)

    if(bolsa_act == -1):
        bolsas.append(0)
        bolsa_act = len(bolsas) -1

    w = bolsas[bolsa_act]

    # Primer caso, que no quepa en la bolsa actual = abrir bolsa

    if (objeto > w_max - w):

        if(len(inx_disp)>1):
            guardar = bolsas.pop(bolsa_act)
            return [guardar] + empacar(objetos,bolsas,w_max)
        # Crear una nueva bolsa con el objeto
        bolsas.append(objeto)
        if(bolsas[-1] < w_max):
            inx_disp.append(len(bolsas) - 1)
        bolsas_final.append(empacar(objetos[1:], bolsas, w_max))


    # Segundo caso, meter y no meter
    else:
        # Preparacion de estado en caso de meter el objeto
        bolsas_aux = bolsas.copy()
        bolsas_aux[bolsa_act] = bolsas_aux[bolsa_act] + objeto

        # meter el objeto
        bolsas_final.append(empacar(objetos[1:], bolsas_aux, w_max))

        # No meter el objeto

        # retirar bolsa
        guardar = bolsas.pop(bolsa_act);
        bolsas_final.append([guardar] + empacar(objetos, bolsas, w_max))

        return bolsas_final

def encontrar_indice(w_max,objeto,inx_disp,bolsas):


    if not inx_disp:
        return - 1
    else:
        i=0
        for x in bolsas:
            if(x+objeto <= w_max):
                return i
            i+=1
        return -1




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lista = [5, 4, 3, 2, 1]
    w = 5
    bolsas = [0]

    print(empacar(lista, bolsas, w))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
