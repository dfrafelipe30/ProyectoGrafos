# -*- coding: utf8 -*-
class Page:
    def __init__(self,nombre,Secciones,TemaPrin,URL,PesosANodos):
        #nombre: Nombre de la página
        self.nombre = nombre
        #secciones: lista con strings de las secciones de la pagina
        self.secciones= Secciones
        #temaPrin: String del tema principal de la pagina
        self.temaPrin = TemaPrin
        #URL: String del "URL" de la pagina
        self.URL = URL
        #PesosANodos: diciconario con llave los nodos a los que se llega y valor el peso del lado
        #A partir de cada diccionario se crean todos los lados de la red
        self.PesosANodos = PesosANodos
        
    def get_nombre(self):
        return self.nombre
    def get_secciones(self):
        return self.secciones
    def get_temaPrin(self):
        return self.temaPrin
    def get_URL(self):
        return self.URL

    def get_PesosANodos(self):
        return self.PesosANodos
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_Secciones(self,Secciones):
        self.secciones = Secciones
    def set_temaPrin(self,temaPrin):
        self.temaPrin = temaPrin
    def set_URL(self,URL):
        self.URL = URL
    def set_PesosANodos(self,pNodos):
        self.PesosANodos = pNodos
    def to_string(self):
        return [self.nombre,self.secciones,self.URL]
