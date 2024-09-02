import matplotlib.pyplot as plt

# Data from the provided table
minutes = [23, 25, 26, 27, 27, 29, 32, 32, 46, 53, 55, 56, 56, 60, 70, 71, 74, 75, 76, 76]
players = [
    "Wilson Odobert", "Pape Matar Sarr", "Dejan Kulusevski", "Wilson Odobert", "Pape Matar Sarr", 
    "Pedro Porro", "Pedro Porro", "Pedro Porro", "Dejan Kulusevski", "Wilson Odobert", 
    "Son Heung-min", "James Maddison", "Brennan Johnson", "Pedro Porro", "Wilson Odobert", 
    "Radu Drăgușin", "James Maddison", "Pedro Porro", "Pedro Porro", "Brennan Johnson"
]
xG = [0.03, 0.04, 0.03, 0.08, 0.03, 0.01, 0.04, 0.03, 0.05, 0.17, 0.10, 0.03, 0.27, 0.08, 0.06, 0.02, 0.04, 0.02, 0.03, 0.09]

# Highlight Brennan Johnson's shot
colors = ['green' if player == 'Brennan Johnson' and shot == 0.27 else 'blue' for player, shot in zip(players, xG)]
sizes = [x * 500 for x in xG]

# Create a timeline plot
plt.figure(figsize=(12, 6))
plt.scatter(minutes, xG, c=colors, s=sizes, edgecolor='black', alpha=0.7)

# Annotate Brennan Johnson's shot
for i, txt in enumerate(players):
    if txt == 'Brennan Johnson' and xG[i] == 0.27:
        plt.annotate(f'{txt} - {xG[i]} xG', (minutes[i], xG[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.title('Tottenham Shots xG Timeline')
plt.xlabel('Minute')
plt.ylabel('xG Value')
plt.grid(True)
plt.show()