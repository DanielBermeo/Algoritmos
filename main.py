def empacar(objetos, bolsas, w_max):
    bolsas_final=[]
    #objetos = objetos.sort(reverse = True)
    i = len(objetos)

    # Encuentra cuantas bolsas no llenas hay
    inx_disp = 0
    for x in bolsas:
        if(x < w_max):
            inx_disp += 1

   #Condicion de salida
    if i == 0:
        return bolsas

    objeto = objetos[0]
    bolsa_act = encontrar_indice(w_max, objeto, inx_disp, bolsas)

    if(bolsa_act == -1):
        bolsas.append(0)
        bolsa_act = len(bolsas) -1

    w = bolsas[bolsa_act]

    # Primer caso, que no quepa en la bolsa actual = abrir bolsa

    if (objeto > w_max - w):

        if(inx_disp>1):
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


if __name__ == '__main__':
    lista = [12,7,5, 4, 3, 2,2, 1]
    w = 15
    bolsas = [0]

    print(empacar(lista, bolsas, w))
