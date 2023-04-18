### Es un anagrama ###
"""
MEDIA | Publicación: 03/01/22 | Resolución: 10/01/22
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""
def palabra_anagramas():
    palabra_1=""
    palabra_2=""

    palabra_1 = input("Escribe la primera palabra: ")
    palabra_2 = input("Escribe la segunda palabra: ")
        
    print(f"Vamos a comprabar si la palabra: {palabra_1} y la palabra: {palabra_2} son anagramas")  

    if palabra_1 == palabra_2:
        print("Son la misma palabra, escribe otras 2")

    else:
        print(palabra_1, palabra_2)    
        set_palabra_1=set(palabra_1.lower())
        set_palabra_2=set(palabra_2.lower())
        print(set_palabra_1)
        print(set_palabra_2)

        if set_palabra_1==set_palabra_2:
            print("Las 2 palabras son anagramas")
        else:
            print("no son anagramas")

palabra_anagramas()