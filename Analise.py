####Casos confirmados no Pará####

import matplotlib.pyplot as plt

##Belém
x = ["17","18","19","20","21","22","23","24","25"]
y = ["0","1","1","2","2","4","4","4","4"]
tamanhoB = [0,50,0,50,0,50,0,0,50]

##Marabá
x2 = ["17","18","19","20","21","22","23","24","25"]
y2 =["0","0","0","0","0","0","1","1","1"]
tamanhoM = [0,0,0,0,0,0,50,0,50]

##Ananindeua
x3 = ["17","18","19","20","21","22","23","24","25"]
y3 = ["0","0","0","0","0","0","0","0","2"]
tamanhoA = [0,0,0,0,0,0,0,0,50]
##Legendas do grafico
titulo ="Casos confirmado do COVID-19 PA (CASOS: 7)"
Labx = "Dias de Março"
laby = "Quantidade de infectados"

##Processamento
plt.title(titulo)
##Criando grafico de linha de Belém
plt.plot(x,y, label = "Belém")
##Criando grafico de linha Marabá
plt.plot(x2,y2, label = "Marabá")
##Criando grafico de linha Ananindeua
plt.plot(x3,y3, label = "Ananindeua")

##Pontos no grafico
plt.scatter(x,y, color = "r", s= tamanhoB)
plt.scatter(x2,y2, s= tamanhoM)
plt.scatter(x3,y3, s= tamanhoA , color = "m")

##Legendando de fato o grafico
plt.xlabel(Labx)
plt.ylabel(laby)

##Aplicando as legendas
plt.legend()

##Salvanod imagem
plt.savefig("COVID-19.png")

##Mostrar grafico
plt.show()


