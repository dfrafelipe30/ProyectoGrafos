# -*- coding: utf8 -*-
from ClassPage import Page
from ClassGraph import Graph

def secciones(secciones,nombres):
    #retorna diccionario de secciones de cada pagina
    d = {}
    for i in range(len(nom)):
        if i <4:
            d[nom[i]] = secciones[0]
        elif(i >= 4 and i < 9):
            d[nom[i]] = secciones[1]
        else:
            d[nom[i]] = secciones[2]
    return d

def crearPesosA(dic,n,nombres,Npag):
    idx = [1,5,7,10]
    for i in range(len(nom)):
        if(nom[i] == 'Facebook' or i in idx):
            dic[nom[i]] = 1./n

    dic.pop(Npag)

    return dic


def crearPesosB(dic,n,nombres,Npag):
    idx = [0,2,4,6]
    for i in range(len(nom)):
        if(nom[i] == 'Twitter' or i in idx):
            dic[nom[i]] = 1./n

    dic.pop(Npag)
    return dic


def crearPesosC(dic,n,nombres,Npag):
    #print dic
    idx = [7,8,9,11]
    for i in idx:
        #print "nom[i]: ",nom[i]
        #print"i: ",i
        dic[nom[i]] = 1./n

    #dic.pop('Instagram')
    return dic


def crearPesosD(dic,n,nombres,Npag):
    idx = [0,5,9,1]
    for i in range(len(nom)):
        if(nom[i] != 'SnapChat' and i in idx):
            dic[nom[i]] = 1./n

    #dic.pop(Npag)
    return dic
    
    

def crearPesos2(dic,n,nombres,Npag):
    idx = [6,5,2,9,10,11]
    for i in range(len(nom)):
        if i in idx:
            dic[nom[i]] = 1./n

    #dic.pop(Npag)
    return dic

def crearPesos3(dic,n,nombres,Npag):
    idx = [0,1]
    #Para Entretenimiento y programacion
    for i in range(len(nombres)):
        if i in idx:
            dic[nom[i]] = 1./n

    #dic.pop(Npag)
    return dic

def crearPesos4(dic,n,nombres,Npag):
    idx = [0,2,3]
    #NO ES PARA O
    for i in range(len(nombres)):
        if i in idx:
            dic[nom[i]] = 1./n

    #dic.pop(Npag)
    return dic
    

    
def paginas(nombres):
    #Retorna diccionario con llave nombre de pagina y valor su "URL"
    d = {}
    for n in nombres:
        if(' ' in n):
            palabras = n.split()
            output = ''
            for p in palabras:
                output = output + p.lower()

            url = 'www.'+ output + '.com'
        else:
            url = 'www.'+ n.lower() + '.com'
        d[n] = url

    return d


# LA RED ES FUERTEMENTE CONECTADA
nom = ['Facebook','Twitter','Instagram','SnapChat',\
       'Caracol','El Espectador','BBC News','Le Monde','The Guardian',\
       'ESPN','Fox Sports','Claro sports',\
       'cuevana2','Netflix','Skanime','Warner Bros',\
       'code academy','Datacamp']

#secciones
sec = [['amigos','perfil','notificaciones','cuenta'],\
       ['opinion','economia','deportes','internacional'],\
       ['futbol','ciclismo','baloncesto','atletismo'],\
       ['Peliculas','Series','anime'],\
       ['cursos','lenguajes de programacion']]

dSec = secciones(sec,nom)

#URL
dpag = paginas(nom)
        
#Temas principales
temasppl = {}
for i in range(len(nom)):
    if (i < 4):
        temasppl[nom[i]] = 'red social ' + nom[i]
    elif(i >= 4 and i < 9):
        temasppl[nom[i]] = 'noticias ' + nom[i]
    elif (i >= 9 and i < 12):
        temasppl[nom[i]] = 'deportes ' + nom[i]
    elif(i >= 12 and i < 16):
        temasppl[nom[i]] = 'peliculas y series ' + nom[i]
    else:
        temasppl[nom[i]] = 'cursos programacion ' + nom[i]




#A = Facebook
d1 = {'SnapChat':1/2.,
      'Instagram': 1./2.}
p1 = Page('Facebook',dSec['Facebook'],temasppl['Facebook'],dpag['Facebook'],d1)

#B = 'SnapChat'
d2 = {'Instagram':1./2.,
      'Facebook':1./2.}
p2 = Page('Instagram',dSec['Instagram'],temasppl['Instagram'],dpag['Instagram'],d2)

#C = Instagram
d3 = {'Caracol':1./2.,
      'SnapChat': 1./2.}
p3 = Page('Instagram',dSec['Instagram'],temasppl['Instagram'],dpag['Instagram'],d3)

#D = Caracol
d4 = {'Facebook':1}
p4 = Page('Caracol',dSec['Caracol'],temasppl['Caracol'],dpag['Caracol'],d4)




"""
d1 = {}
d1 = crearPesosA(d1,4,nom,'Facebook')
p1 = Page('Facebook',dSec['Facebook'],temasppl['Facebook'],dpag['Facebook'],d1)


# B = Twitter
d2 = {}
d2 = crearPesosB(d2,4,nom,'Twitter')
p2 = Page('Twitter',dSec['Twitter'],temasppl['Twitter'],dpag['Twitter'],d2)

#C = Instagram
d3 = {}
d3 = crearPesosC(d3,4,nom,'Instagram')
p3 = Page('Instagram',dSec['Instagram'],temasppl['Instagram'],dpag['Instagram'],d3)

#D = SnapChat
d4 = {}
d4 = crearPesosD(d4,4,nom,'SnapChat')
p4 = Page('SnapChat',dSec['SnapChat'],temasppl['SnapChat'],dpag['SnapChat'],d4)

#E = Caracol
d5 = {}
d5 = crearPesos2(d5,6,nom,'Caracol')
p5 = Page('Caracol',dSec['Caracol'],temasppl['Caracol'],dpag['Caracol'],d5)

#F = El Espectador
d6 = {}
d6 = crearPesos2(d6,6,nom,'El Espectador')
p6 = Page('El Espectador',dSec['El Espectador'],temasppl['El Espectador'],dpag['El Espectador'],d6)

#G = BBC News
d7 = {}
d7 = crearPesos2(d7,6,nom,'BBC News')
p7 = Page('BBC News',dSec['BBC News'],temasppl['BBC News'],dpag['BBC News'],d7)

#H = 'Le Monde'
d8 = {}
d8 = crearPesos2(d8,6,nom,'Le Monde')
p8 = Page('Le Monde',dSec['Le Monde'],temasppl['Le Monde'],dpag['Le Monde'],d8)

#I = 'The Guardian'
d9 = {}
d9 = crearPesos2(d9,6,nom,'The Guardian')
p9 = Page('The Guardian',dSec['The Guardian'],temasppl['The Guardian'],dpag['The Guardian'],d9)

#J ESPN
d10 = {}
d10 = crearPesos3(d10,2,nom,'ESPN')
p10 = Page('ESPN',dSec['ESPN'],temasppl['ESPN'],dpag['ESPN'],d10)

#K 'Fox Sports'
d11 = {}
d11 = crearPesos3(d11,2,nom,'Fox Sports')
p11 = Page('Fox Sports',dSec['Fox Sports'],temasppl['Fox Sports'],dpag['Fox Sports'],d11)

#L Claro Sports
d12 = {}
d12 = crearPesos3(d12,2,nom,'Claro sports')
p12 = Page('Claro sports',dSec['Claro sports'],temasppl['Claro sports'],dpag['Claro sports'],d12)
"""
"""
#M 'cuevana2'
d13 = {}
d13 = crearPesos4(d13,4,nom,'cuevana2')
p13 = Page('cuevana2',dSec['cuevana2'],temasppl['cuevana2'],dpag['cuevana2'],d13)


#N Netflix
d14 = {}
d14 = crearPesos4(d14,4,nom,'Netflix')
p14 = Page('Netflix',dSec['Netflix'],temasppl['Netflix'],dpag['Netflix'],d14)

#O Skanime
d15 = {'cuevana2':1./2.}

#P 'Warner Bros'
d16 = {}
d16 = crearPesos4(d16,4,nom,'Warner Bros')
p16 = Page('Warner Bros',dSec['Warner Bros'],temasppl['Warner Bros'],dpag['Warner Bros'],d16)
"""

Paginas = [p1,p2,p3,p4]
red = Graph(Paginas)
#print red.MatrizDePesos()
#print red.buscador('noticias ')

#print red.Transpuesta()
#print red.PageRank(v,8)
