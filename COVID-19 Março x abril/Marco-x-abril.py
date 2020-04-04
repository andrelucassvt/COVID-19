import matplotlib.pyplot as plt 

meses = ["Março","Abril"]
casos = ["32","43"]

titulo = "Comparação: Março e Abril"
EixoX = "Meses"
EixoY = "Casos confirmados"

plt.title(titulo)
plt.xlabel(EixoX)
plt.ylabel(EixoY)

plt.plot(meses,casos, label = "Aumento")
plt.legend()
plt.show()

