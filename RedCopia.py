from ClassPage import Page
from ClassGraph import Graph
# LA RED ES FUERTEMENTE CONECTADA

#Nombres
n = ['Facebook','Twitter','Instagram','SnapChat',\
     'Caracol','El Espectador','BBC News','Le Monde','The Guardian',\
     'ESPN','Fox Sports','NBA']
l_a = [n[i] for i in range(len(n))]
wa = 1/float(len(l_a))

#Temas: redes sociales,noticias, deporte, universidades, aprender a programar
#A = Facebook
d1 = {'Instagram': 1./3.,
      'Twitter': 1./3.,
      'SnapChat': 1./3.}
p1 = Page('Facebook',['Amigos','Fotos'],'Red social','www.facebook.com',d1)

# B = Twitter
d2 = {'Instagram':1./2.,
      'SnapChat': 1./2.}
p2 = Page('Twitter',['Amigos','Fotos'],'Red social','www.twitter.com',d2)

#C = Instagram
d3 = {'Facebook':1}
p3 = Page('Instagram',['Amigos','Fotos'],'Red social','www.instagram.com',d3)

#D = SnapChat
d4 = {'Facebook': 1./2.,
      'Instagram': 1./2.}
p4 = Page('SnapChat',['Amigos','Fotos'],'Red social','www.snapchat.com',d4)

Paginas = [p1,p2,p3,p4]

# a,b,c,d
red = Graph(Paginas)
#print red.MatrizDePesos()

v = [1/4.,1/4.,1/4.,1/4.]
print red.PageRank(v,3)
