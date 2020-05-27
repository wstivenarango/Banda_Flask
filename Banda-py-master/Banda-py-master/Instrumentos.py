from abc import ABC, abstractmethod

class Instrumento(ABC):
    @abstractmethod
    def tocar(self):
       pass
    @abstractmethod
    def preparar(self):
       pass


class Guitarra(Instrumento):
    nombre = 'Guitarra'
    imagen = "/static/Guitarra.png" 
    def tocar(self):
        return("tocando Guitarra")
    def preparar(self):
        return ("afinando Guitarra")
    def __init__(self):
        self = self
   


class Bajo(Instrumento):
    nombre = 'Bajo'    
    imagen = "/static/Bajo.png"
    def tocar(self):
        return("tocando Bajo")
    def preparar(self):
        return ("afinando Bajo")
      


class Violin(Instrumento):
    nombre = 'Violin'  
    imagen = "/static/Violin.png"
    def tocar(self):
        return("tocando Violin")
    def preparar(self):
        return ("afinando Violin")
    
    def __init__(self):
        self = self


class Arpa (Instrumento):
    nombre = 'Arpa'  
    imagen = "/static/Arpa.png"
    def tocar(self):
        return("tocando Arpa")
    def preparar(self):
        return ("afinando Arpa")
    
    def __init__(self):
        self = self


class Viola (Instrumento):
    nombre = 'Viola' 
    imagen = "/static/Viola.png"
    def tocar(self):
        return("tocando Viola")
    def preparar(self):
        return ("afinando Viola ")
   
    def __init__(self):
        self = self


class Ukelele (Instrumento):
    nombre = 'Ukelele' 
    imagen = "/static/Ukelele.png"
    def tocar(self):
        return("tocando Ukelele")
    def preparar(self):
        return ("afinando Ukelele")
   
    def __init__(self):
        self = self

class Violin_Chelo (Instrumento):
    nombre = 'Violin Chelo'
    imagen = "/static/ViolinChelo.png"
    def tocar(self):
        return("tocando Chelo")
    def preparar(self):
        return ("afinando Chelo")
   
    def __init__(self):
        self = self        

class Contrabajo (Instrumento):
    nombre = 'Contrabajo'
    imagen = "/static/Contrabajo.png"
    def tocar(self):
        return("tocando Contrabajo")
    def preparar(self):
        return ("afinando Contrabajo")
   
    def __init__(self):
        self = self 
