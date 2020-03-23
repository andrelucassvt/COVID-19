####Casos confirmados no Pará####

import matplotlib.pyplot as plt

x = ["18","19","20","21","22"]
y = ["1","1","2","2","4"]


titulo ="Casos confirmado COVID-19 PA"
Labx = "Dias de Março"
laby = "Quantidade"

plt.title(titulo)
plt.plot(x,y, label = "Casos confirmados")
plt.scatter(x,y, color = "R")
plt.xlabel(Labx)
plt.ylabel(laby)

plt.legend()
plt.show()