"""
Escribe un programa que imprima los 50 primeros números de la sucesión
 de Fibonacci empezando en 0.
 La serie Fibonacci se compone por una sucesión de números en
 la que el siguiente siempre es la suma de los dos anteriores.
 0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci():
    j = 0 
    a1 = 0
    a2 = 0

    for i in range(1,51):
        
        
        if i == 2:
            j = 1
            a2 = a1
            a1 = j 
        else:
            j = a1 + a2
            a2 = a1
            a1 = j
                
        print(f"el número {i}, me sale la suma {j}")

fibonacci()
    