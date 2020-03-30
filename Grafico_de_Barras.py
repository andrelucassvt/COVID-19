##Grafico de barras
import matplotlib.pyplot as plt

##Valores
cidades = ['0','Parauapebas','Itaituba','Castanhal','Marabá','Ananindeua','Belém']
casos = ['0','1','1','1','1','4','12']


##Legendar o grafico
titulo = "Casos confirmados de COVID-19 no Estado do PA (Casos: 20)"
Legenda_x = "Quantidade de infectados"
Legenda_y = "Cidades do Estado"

##Operações
plt.title(titulo)
plt.xlabel(Legenda_x)
plt.ylabel(Legenda_y)

plt.barh(cidades,casos)
plt.legend()

plt.show()