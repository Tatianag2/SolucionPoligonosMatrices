import numpy as np
def funciones():
    operacion = int(input("\n1. Resolver polinomios\n2. Resolver sistemas de ecuaciones\n Escoja la operación a realizar: "))
    if operacion == 1:
        def funcion_poligono():
            grado_poligono = int(input("Escriba por favor el grado del poligono que desea resolver:"))
            coeficientes = []
            for i in range(grado_poligono+1): 
                coef = int(input(f"Ingrese el coeficiente que acompaña x^{i}: "))
                coeficientes.append(coef)
            coeficientes = coeficientes[::-1]
            solucion = np.roots(coeficientes)
            f = np.poly1d(coeficientes)
            print("Su polinomio es:\n ",f)
            print("La solución para x es: ",solucion)
            print("")
        funcion_poligono()
    elif operacion == 2:
        def sistema_ecuaciones():
            tamaño = int(input("\n1. Matriz 2x2\n2. Matriz 3x3\n Escoja tipo de matriz: "))
            if tamaño == 1:
                lista1 = []
                lista2 = []
                i = 0
                for i in range(2):
                    primera_fila = int(input(f"Ingrese el elemento a1,{i+1}: "))
                    lista1.append(primera_fila)
                    segunda_fila = int(input(f"Ingrese el elemento a2,{i+1}: "))
                    lista2.append(segunda_fila)
                    i += 1
                    matriz = np.array([lista1,lista2])
            
                x = int(input("Ingrese primer valor columna terminos independientes (x): "))
                y = int(input("Ingrese segundo valor columna terminos independientes (y): "))
                terminos_independientes = np.array([x,y])

                print(f"Matriz = {matriz}\n \n Vector terminos independientes = {terminos_independientes}")
                solucion = np.linalg.solve(matriz,terminos_independientes)
                print("=====================SOLUCION==========================")
                print("La solución para el sistema de ecuaciones es [x,y]= ",solucion)
                print("=======================================================")

            elif tamaño == 2:
                lista1 = []
                lista2 = []
                lista3 = []
                j = 0
                for j in range(3):
                    primera_fila = int(input(f"Ingrese el elemento a1,{j+1}: "))
                    lista1.append(primera_fila)
                    segunda_fila = int(input(f"Ingrese el elemento a2,{j+1}: "))
                    lista2.append(segunda_fila)
                    tercer_fila = int(input(f"Ingrese el elmento a3,{j+1}: "))
                    lista3.append(tercer_fila)
                    j += 1
                    matriz = np.array([lista1,lista2,lista3])
        
                x = int(input("Ingrese primer valor columna terminos independientes (x): "))
                y = int(input("Ingrese segundo valor columna terminos independientes (y): "))
                z = int(input("Ingrese segundo valor columna terminos independientes (z): "))
                terminos_independientes = np.array([x,y,z])

                print(f"Matriz = {matriz}\n \n Vector terminos independientes = {terminos_independientes}")
                solucion = np.linalg.solve(matriz,terminos_independientes)
                print("=====================SOLUCION==========================")
                print("La solución para el sistema de ecuaciones es [x,y,z]= ",solucion)
                print("=======================================================")
            else:
                print("Ingrese un número valido")
        sistema_ecuaciones()
    else:
        print("Ingrese un número valido")
funciones()

