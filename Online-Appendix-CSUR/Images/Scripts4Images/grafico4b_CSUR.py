import matplotlib.pyplot as plt
import numpy as np

# Dati
categories = ["A*", "A", "C", "Conf. Not Ranked", "Q1", "Q2", "Journ. Not Ranked"]
conference_values = [4, 1, 1, 25, 0, 0, 0]
journal_values = [0, 0, 0, 0, 19, 10, 3]

# Colori personalizzati
colors = {"Conference": "#FFB000", "Journal": "#FE6100"}


x = np.arange(len(categories))
bar_width = 0.5

fig, ax = plt.subplots(figsize=(9, 6))

# Disegna le barre con bordo
bars1 = ax.bar(
    x, conference_values, width=bar_width, label='Conference',
    color=colors["Conference"], edgecolor='black', linewidth=1
)
bars2 = ax.bar(
    x, journal_values, width=bar_width, label='Journal',
    color=colors["Journal"], edgecolor='black', linewidth=1
)

# Aggiungi etichette con valori sopra le barre, in grassetto
for bar in bars1 + bars2:
    height = bar.get_height()
    if height > 0:
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontweight='bold')

# Etichette asse X in grassetto
ax.set_xticks(x)
ax.set_xticklabels(categories, ha='center', fontweight='bold')

# Griglia orizzontale tratteggiata
ax.yaxis.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)
ax.set_axisbelow(False)  # per disegnare la griglia sotto le barre

# Impostazioni generali
ax.set_xlabel('Ranking Category')
ax.set_ylabel('Papers')
ax.set_title('Distribution of Venue Rankings')
ax.legend()

plt.tight_layout()
plt.show()