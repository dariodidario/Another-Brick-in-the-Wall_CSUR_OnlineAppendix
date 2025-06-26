import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

# Dati unificati
data = [
    {"Venue Type": "Conference", "Papers": 31},
    {"Venue Type": "Journal", "Papers": 32}
]

# Creazione DataFrame
df = pd.DataFrame(data)

# Colore arancione
colors= ["#FFB000", "#FE6100"]


# Plot
plt.figure(figsize=(8, 6))
bars = plt.bar(df["Venue Type"], df["Papers"],
               color=colors, edgecolor='black', linewidth=1, width = 0.6)

plt.title("Distribution of Venue Types", fontsize=14)
plt.ylabel("Papers", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Asse Y solo interi
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# Etichette sopra le barre in grassetto
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval),
             ha='center', va='bottom', fontsize=10, weight='bold')

plt.tight_layout()
plt.savefig("Figure4a_final.pdf", format='pdf')
plt.show()