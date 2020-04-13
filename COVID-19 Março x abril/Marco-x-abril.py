import matplotlib.pyplot as plt 

Marco = ["Março"]
Abril = ["Abril"]

casosMarco = [227]
casosAbril = [32]

titulo = "Comparação de casos COVID-19: Março x Abril"


plt.title(titulo)

plt.bar(Abril,casosAbril)
plt.bar(Marco,casosMarco)

plt.legend()
plt.show()