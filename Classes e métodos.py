#Class
class Computador:
    def __init__(self,marca,placa_de_video,memoria_ram): #instanciando a classe com o construtor init;
        self.marca = marca
        self.placa_de_video = placa_de_video
        self.memoria_ram = memoria_ram

    def Ligar(self):
        print("Estou ligando")
    
    def Desligar(self):
        print("Estou desligando")

    def Info(self):
        print(self.marca , self.placa_de_video , self.memoria_ram)

computador1 = Computador("Asus" , "Nvidia" , "8gb")
computador2 = Computador("Sony" , "ATM" , "10gb")
computador3 = Computador("Apple" , "Geforce" , "16gb")

print(computador1.marca) #printagem na tela dos objetos referentes à classe.
print(computador2.memoria_ram)
print(computador3.placa_de_video)

computador1.Ligar()
computador2.Desligar()
computador3.Info()







