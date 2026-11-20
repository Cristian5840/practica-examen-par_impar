


#primera solucion
#  Uso notacion snake case--> par_impar
def par_impar(num):
 if num == 0:
   return "Cero"
 if num % 2 == 0:
   return "par"
 if num % 2!= 0:
  return "impar"


#segunda soluciom

def parimpar(num):
    if num == 0:
        return "Cero"
    if num % 2 == 0:
        return "Par"
    if num%2 == 1:
        return "Impar"


#tercera solucion
#  Uso notacion snake case
def par_impar(num):
  if num == 0:
     return "cero"
  if num%2 == 0:
     return "par"
  return "impar"







#import unittest
#from funciones import par_impar

#class Testpar_impar(unittest.Testcase):
 
def par_impar(num):
    """
    Indica si un número entero es par, impar o cero.

    Parámetros:
        num (int): Número entero a evaluar.

    Retorna:
        str:
            - "Cero" si num es 0.
            - "par" si num es divisible por 2.
            - "impar" si num no es divisible por 2.

    Ejemplos:
        >>> par_impar(0)
        'Cero'
        >>> par_impar(4)
        'par'
        >>> par_impar(7)
        'impar'
        >>> par_impar(-3)
        'impar'
    """
    if num == 0:
        return "Cero"
    if num % 2 == 0:
        return "par"
    if num % 2 != 0:
        return "impar"

#Un docstring (cadena de documentación) es un texto escrito entre triples comillas """ """ 
# que se coloca justo debajo de la definición de una función, clase o módulo. Sirve para explicar qué hace ese código, sin ser parte de la lógica.

#Ejemplo con tu función:
def par_impar(num):
    """Indica si un número entero es par, impar o cero."""
    if num == 0:
        return "Cero"
    ...
#Para qué sirve:

#Documentar: cualquiera que lea tu código entiende qué hace la función, qué recibe y qué devuelve, sin tener que descifrar la lógica.
#Ayuda en Python: el docstring queda guardado en la función y se puede consultar con help(par_impar) o con par_impar.__doc__.
#Editores: programas como VS Code o PyCharm lo muestran cuando pasás el mouse sobre la función.
#Doctests: los ejemplos que empiezan con >>> se pueden ejecutar automáticamente para verificar que la documentación es correcta (python -m doctest archivo.py).

