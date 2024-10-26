
import matplotlib.pyplot as plt
import numpy as np


dni = ["2024-10-15", "2024-10-16", "2024-10-17", "2024-10-18", "2024-10-19"]
dlugosc_spania = [8, 7.5, 6, 8.5, 7] 
dlugosc_dobrego_spania = [6, 5.5, 4, 6.5, 5]  


x = np.arange(len(dni))


width = 0.4


fig, ax = plt.subplots()

ax.bar(x, dlugosc_dobrego_spania, width, label="Dobry sen", color="skyblue")

ax.bar(x, dlugosc_spania, width, label="Calkowity sen", color="steelblue", bottom=dlugosc_dobrego_spania)


ax.set_xlabel("Dzien")
ax.set_ylabel("Czas spania (godziny)")
ax.set_title("Dlugosc snu i dlugosc dobrego snu na przestrzeni dni")
ax.set_xticks(x)
ax.set_xticklabels(dni, rotation=45)


ax.legend()


plt.tight_layout()
plt.show()  
plot_image_path = "api/data/plot.png"
plt.savefig(plot_image_path)
plt.close()