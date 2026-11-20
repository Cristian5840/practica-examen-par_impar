
def par_impar(num):
    if num%2==0:
        return "par"
    if num %2!=0:
        return "impar"

def lista_par_impar(lista_nums):

    lista_resultados=[]
    for numero in lista_nums:
        lista_resultados.append(par_impar(numero))
    return lista_resultados




print(lista_par_impar([2,5,7,13,8,9,25]))

