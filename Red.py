from ClassPage import Page
from ClassGraph import Graph
# LA RED ES FUERTEMENTE CONECTADA
d1 = {'Instagram': 1./2.,
      'Twitter': 1./2.}
p1 = Page('Facebook',['Amigos','Fotos'],'Red social','www.facebook.com',d1)

d2 = {'Instagram':1}
p2 = Page('Twitter',['Amigos','Fotos'],'Red social','www.twitter.com',d2)

d3 = {'Facebook':1}
p3 = Page('Instagram',['Amigos','Fotos'],'Red social','www.instagram.com',d3)

Paginas = [p3,p1,p2]

red = Graph(Paginas)

print red.MatrizDePesos()
