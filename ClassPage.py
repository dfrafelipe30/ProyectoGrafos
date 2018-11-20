class Page:
    def __init__(self,nombre,Secciones,TemaPrin,URL,RefSalientes,RefEntrantes):
        self.monbre = nombre
        self.secciones= Secciones
        self.temaPrin = TemaPrin
        self.URL = URL
        self.refSalientes = RefSalientes
        self.refEntrantes = RefEntra
    def get_nombre(self):
        return self.nombre
    def get_secciones(self):
        return self.secciones
    def get_temaPrin(self):
        return self.temaPrin
    def get_URL(self):
        return self.URL
    def get_refSalientes(self):
        return self.nombre
    def get_refEntrantes(self):
        return self.refEntrantes
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_Secciones(self,Secciones):
        self.secciones = Secciones
    def set_temaPrin(self,temaPrin):
        self.temaPrin = temaPrin
    def set_URL(self,URL):
        self.URL = URL
    def set_refSalientes(self,refSalientes):
        self.nombre.append(refSalientes)
    def set_refEntrantes(self,refEntrantes):
        self.refEntrantes.append(refEntrantes)
    
