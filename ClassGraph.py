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
        X = self.PageRank(v,8)
        Y = copy(X)
        Y.sort(reverse = True)
        PaginasResultados = []
        for i in Y:
            indice = X.index(i)
            PaginasResultados.append(self.nodos(i))
        stringResultados = []
        for i in PaginasResultados:
            stringResultados.append(i.to_string)

    def PageRank(self,v,n):
        # Retorna el  nuevo vector despues de multiplicar n veces P x v
        # n: numero de veces que se multiplica P*v
        if n == 0:
            return v
        else:
            resul = []
            matriz = self.Transpuesta()
            for i in  matriz:
                aux = 0
                print "i: ",i
                for j in range(len(v)):
                    aux = aux + i[j]*v[j]
                print "aux: ",aux
                resul.append(aux)
            return self.PageRank(resul,n-1)
        
    def Transpuesta(self):
        contador = 0
        trans = []
        matriz = self.MatrizDePesos()
        while(contador <= len(matriz) - 1):
            aux = []
            for i in matriz:
                aux.append(i[contador])
            trans.append(aux)
            contador = contador + 1
        return trans
    def copy(self,lista):
        aux = []
        for i in range(len(lista)):
            aux[i] = lista[i]
        return aux
    def InsertarPagina(self,pagina):
        self.nodos.append(pagina)
        for j in pagina.PesosANodos:
            aux = [(pagina.nombre,j),pagina.PesosANodos[j]]
            self.lados = lados.append(aux)
        
