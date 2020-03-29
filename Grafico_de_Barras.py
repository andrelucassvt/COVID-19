##Grafico de barras
import matplotlib.pyplot as plt

##Valores
cidades = ['0','Parauapebas','Itaituba','Castanhal','Marabá','Ananindeua','Belém']
casos = ['0','1','1','1','1','4','10']


##Legendar o grafico
titulo = "Casos confirmados de COVID-19 no Estado do PA (Casos: 18)"
cidadesx = "Quantidade de infectados"
casosy = "Cidades do Estado"

##Operações
plt.title(titulo)
plt.xlabel(cidadesx)
plt.ylabel(casosy)

plt.barh(cidades,casos)
plt.legend()

plt.show()