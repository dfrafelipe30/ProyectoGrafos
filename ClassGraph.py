from difflib import SequenceMatcher
def similar(a,b):
    return SequenceMatcher(None,a,b).ratio()

class Graph:
    def __init__(self,Paginas):
        #nodos: lista de paginas
        self.nodos = Paginas
        lados = []
        for p in Paginas:
            for j in p.PesosANodos:
                aux = [(p.nombre,j),p.PesosANodos[j]]
                lados.append(aux)

        self.lados = lados
        

    
                
    def MatrizDePesos(self):
        dicc = {}
        for v in self.lados:
            dicc[v[0]] = v[1]
        matriz = []
        print "Diccionario: ",dicc
        for i in self.nodos:
            aux = []
            for j in self.nodos:
                if(dicc.has_key((i.nombre,j.nombre))):
                    aux.append(dicc[(i.nombre,j.nombre)])
                elif(i == j):
                      aux.append(0)
                else:
                    aux.append(0)
            matriz.append(aux)
        return (matriz)

    def buscador(self,search):
        # search: lo que se va a buscar
        # EL INDICE DE LA POSICION CON NUMERO MAS GRANDE ES EL DE LA PAGINA EN self.nodos
        
        """ Este metodo crea el vector V0 antes de aplicar Page Rank"""
        #Luego llama a Page Rank, hace las n multiplicaciones
        #Page Rank retorna el vector de probabilidades con la importancia de cada pagina
        #Por ultimo retorna el orden de las paginas
        aux = []
        for n in self.nodos:
            sim = similar(n.get_temaPrin(),search)
            if sim >= 0.7:
                aux.append(sim)
            else:
                aux.append(0)

        s = sum(aux)
        v = [i/s for i in aux]

        #ACABAR RANKING

    def PageRank(self,v):
        # Retorna el  nuevo vector despues de multiplicar n veces P x v


    
        
        
