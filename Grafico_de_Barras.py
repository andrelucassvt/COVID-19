##Grafico de barras
import matplotlib.pyplot as plt

##VAlores
cidades = ['0','Itaituba','Marabá','Castanhal','Não divulgado','Ananindeua','Belém']

casos = ['0','1','1','1','2','2','6']

titulo = "Casos confirmados de COVID-19 no Estado do PA (Casos: 13)"
cidadesx = "Quantidade de infectados"
casosy = "Cidades do Estado"

plt.title(titulo)
plt.xlabel(cidadesx)
plt.ylabel(casosy)

plt.barh(cidades,casos)
plt.legend()
plt.savefig("Grafico de Barras COVID-19")
plt.show()