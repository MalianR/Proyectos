#Definimos  la clase animal
#Atributo -> Hace sonidos
#Método -> hacer sonido

class Animal(object):
    #Objeto de tipo booleano
    makes_noise: bool = False

    #Función "Hace ruido"
    #Self -> Referencia POO del objeto
    def make_noise(self: "Animal") -> object:
        #Si hace ruido
        if self.makes_noise:
            print(self.sound())

    def sound(self: "Animal") -> str:
        return "???"

#Definimos la clase vaca
class Cow(Animal):
    #Inicializar la clase
    def _init_(self: "Cow"):    
    #Establecemos el atributo de hace sonido    
        self.makes_noise = True
    #Propiedad del sonido del animal
    def sound(self: "Cow") -> str:
        return "moo"

#Llamar al objeto y crear una instancia del mismo
vaca = Cow()
#Llmar al método "Hace un sonido"
vaca.make_noise()
