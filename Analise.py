####Casos confirmados no Pará####

import matplotlib.pyplot as plt

##Belém
x = ["17","18","19","20","21","22","23"]
y = ["0","1","1","2","2","4","4"]
tamanhoB = [0,50,0,50,0,50,50]

##Marabá
x2 = ["17","18","19","20","21","22","23"]
y2 =["0","0","0","0","0","0","1"]
tamanhoM = [0,0,0,0,0,0,50]

##Legendas do grafico
titulo ="Casos confirmado do COVID-19 PA"
Labx = "Dias de Março"
laby = "Quantidade de infectados"

##Processamento
plt.title(titulo)
##Criando grafico de linha de Belém
plt.plot(x,y, label = "Belém")
##Criando grafico de linha Marabá
plt.plot(x2,y2, label = "Marabá")
##Pontos no grafico
plt.scatter(x,y, color = "r", s= tamanhoB)
plt.scatter(x2,y2, s= tamanhoM)

##Legendando de fato o grafico
plt.xlabel(Labx)
plt.ylabel(laby)

##Aplicando as legendas
plt.legend()

##Salvanod imagem
plt.savefig("COVID-19.png")

##Montando o gráfico
plt.show()


