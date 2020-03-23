####Casos confirmados no Pará####

import matplotlib.pyplot as plt

x = ["18","19","20","21","22","23"]
y = ["1","1","2","2","4","4"]

##Legendas do grafico
titulo ="Casos confirmado do COVID-19 PA"
Labx = "Dias de Março"
laby = "Quantidade de infectados"

##Processamento
plt.title(titulo)
##Criando grafico de linha
plt.plot(x,y, label = "Belém")
##Pontos no grafico
plt.scatter(x,y, color = "r")

##Legendando de fato o grafico
plt.xlabel(Labx)
plt.ylabel(laby)

##Aplicando as legendas
plt.legend()

##Salvanod imagem
plt.savefig("COVID-19.png")

##Montando o gráfico
plt.show()


