import os

class lista:
    def __init__(self, lista_original):
        self.lista_original = lista_original

    # Ordenar lista
    def ordenar_lista(self):
        lista_ordenada = sorted(self.lista_original)
        print("la lista ordenada es: ", lista_ordenada)

    # Listas pares e impares
    def lista_par_e_impar(self):
        lista_pares = []
        lista_impares = []
        for i in self.lista_original:
            if i % 2 == 0:
                if i not in lista_pares:
                 lista_pares.append(i)
            else:
                 if i not in lista_impares:
                  lista_impares.append(i)
        print("Los numeros pares son: ",lista_pares,"Los numeros impares son: ",lista_impares)

    # Numeros Repetidos
    def numeros_repetidos(self):
        repetidos = {}
        for i in self.lista_original:
            if i in repetidos:
                repetidos[i] += 1
            else:
                repetidos[i] = 1
        for i, cantidad in repetidos.items():
            if cantidad > 1:
                print(f"El número {i} se repite {cantidad} veces.")

def main():
    os.system('cls')
    obj = lista([1, 2, 3, 1, 4, 7, 1, 2, 10, 4])
    obj.ordenar_lista()
    obj.lista_par_e_impar()
    obj.numeros_repetidos()

if __name__ == "__main__":
    main()
