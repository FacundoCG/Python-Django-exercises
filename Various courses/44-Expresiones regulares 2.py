import re

dominios = ['www.wikipedia.ar','www.facebook.com', 'www.facundo.org.ar','www.twitter.com']

for i in dominios:
    if re.findall('ar$',i): #El símbolo $ indica que la palabra tiene que estar al final de lo pedido
        print(i)

#if re.findall('^Sandra', i): #El símbolo ^ indica que la palabra tiene que comenzar con lo pedido
        #print(i)

dominios_es = ['http:///informáticaespaña.es','http:///informáticaargentina.ar','http:///informáticacolombia.co']

for i in dominios_es:
    if re.findall('[ñ]',i): #Los [] buscan que la palabra aparezca en alguna parte del texto
        print(i)

personas = ['Hombres','Mujeres','Mascotas','Niños',"Niñas"]

for i in personas:
    if re.findall('Niñ[oa]s', i): #Entre los [] se indica las letras que pueden aparecer
        print(i)

tildes = ['Camión','Camion']

for i in tildes:
    if re.findall('Cami[óo]n', i): #Entre los [] se indica los carácteres que pueden aparecer
        print(i)