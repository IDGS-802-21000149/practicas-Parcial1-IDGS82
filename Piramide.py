import os

class Torre:
#declaracion de propiedades
    numero = 0
#declaracion del constructor
    def __init__(self,numero):
        self.numero = numero
        
#Delcaracion de los metodos de clase 
    def piramide_estrellas(self):
     for i in range(1, self.numero + 1):
        for j in range(i):
            print("*", end="")
        print()


    
def main():
     os.system('cls')
     estrellas = int(input("Dame el numero de niveles: "))
     obj = Torre(estrellas)
     obj.piramide_estrellas()
        
if __name__ == "__main__":
      main()
    
