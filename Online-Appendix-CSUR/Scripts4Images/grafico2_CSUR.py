import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

# Dati unificati da Figure 2
data = [
    {"Year": 2006, "Papers": 1},
    {"Year": 2008, "Papers": 1},
    {"Year": 2009, "Papers": 2},
    {"Year": 2013, "Papers": 2},
    {"Year": 2015, "Papers": 1},
    {"Year": 2019, "Papers": 1},
    {"Year": 2021, "Papers": 3},
    {"Year": 2022, "Papers": 34},
    {"Year": 2023, "Papers": 7},
    {"Year": 2024, "Papers": 11}
]

# Creazione DataFrame
df = pd.DataFrame(data)

# Colore coerente con Figure 3
color = "#648FFF"

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(df["Year"].astype(str), df["Papers"],
               color=color, edgecolor='black', linewidth=1)

plt.title("Number of Publications per Year", fontsize=14)
plt.xlabel("Year of Publication", fontsize=12)
plt.ylabel("Number of Papers", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Asse Y con numeri interi
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# Etichette sopra ogni barra in grassetto
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.3, int(yval),
             ha='center', va='bottom', fontsize=10, weight='bold')

# Etichette asse X centrate
plt.xticks(ha='center', fontsize=10)

plt.tight_layout()
plt.savefig("Figure2_final_corrected.pdf", format='pdf')
plt.show()