
import matplotlib.pyplot as plt
import numpy as np

def generate_wykres_sleep_time(dni, dlugosc_spania, dlugosc_dobrego_spania, plot_image_path):

    x = np.arange(len(dni))
    width = 0.4
    fig, ax = plt.subplots()

    ax.bar(x, dlugosc_dobrego_spania, width, label="Dobry sen", color="skyblue")

    ax.bar(x, dlugosc_spania, width, label="Calkowity sen", color="steelblue", bottom=dlugosc_dobrego_spania)
    ax.set_xlabel("Dzien")
    ax.set_ylabel("Czas spania (godziny)")
    ax.set_title("Analiza jakosci snu zespolu")
    ax.set_xticks(x)
    ax.set_xticklabels(dni, rotation=45)
    ax.legend()
    plt.tight_layout()
    plt.savefig(plot_image_path)
    plt.close()

def generate_wykres_stress_time(dni, dlugosc_stressu, plot_image_path):
    x = np.arange(len(dni))
    
    plt.figure(figsize=(10, 6))
    
    # Plot total sleep duration
    plt.plot(x, dlugosc_stressu, marker='o', label="Calkowity sen", color="steelblue", linestyle='-')
    
    # Setting labels and title
    plt.xlabel("Dni")
    plt.ylabel("Czas stresu")
    plt.title("Anazliza stresu zespolu")
    plt.xticks(x, dni, rotation=45)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(plot_image_path)
    plt.close()