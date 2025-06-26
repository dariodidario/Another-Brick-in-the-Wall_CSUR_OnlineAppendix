import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

# Dati unificati: autore e numero di pubblicazioni
data = [
    {"Author": "Zehui Xiong", "Publications": 4},
    {"Author": "Jiawen Kang", "Publications": 3},
    {"Author": "Dusit Niyato", "Publications": 3},
    {"Author": "Nicholas Polys", "Publications": 2},
    {"Author": "Olga Sourina", "Publications": 2},
    {"Author": "Lik-Hang Lee", "Publications": 2},
    {"Author": "Alexei Sourin", "Publications": 2},
    {"Author": "Pan Hui", "Publications": 2},
    {"Author": "Xuemin Shen", "Publications": 2},
    {"Author": "Yasushi Ikei", "Publications": 1}
]

# Creazione del DataFrame direttamente dalla struttura unificata
df = pd.DataFrame(data)

# Colore delle barre
color = "#648FFF"

# Creazione del grafico
plt.figure(figsize=(10, 6))
bars = plt.barh(df["Author"], df["Publications"],
                color=color, edgecolor='black', linewidth=1)
plt.title("Top 10 Authors by Number of Publications", fontsize=14)
plt.xlabel("Number of Publications", fontsize=12)
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# Etichette accanto alle barre in grassetto
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.1, bar.get_y() + bar.get_height()/2,
             str(int(width)), va='center', ha='left',
             fontsize=10, weight='bold')

# Etichette asse Y in grassetto
plt.yticks(fontsize=10, weight='bold')

plt.tight_layout()
plt.savefig("Figure3_final_corrected.pdf", format='pdf')
plt.show()