# Creating a pass map for Lionel Messi vs Real Betis using python
import pandas as pd
from matplotlib import pyplot as plt
from mplsoccer.pitch import Pitch
import seaborn as sns

df = pd.read_csv('./data/messibetis.csv')
df['x'] = df['x']*1.2
df['y'] = df['y']*.8
df['endX'] = df['endX']*1.2
df['endY'] = df['endY']*.8
fig, ax = plt.subplots(figsize=(13.5, 8))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')
pitch = Pitch(pitch_color='#22312b', line_color='white', stripe=False)
pitch.draw(ax=ax)
plt.gca().invert_yaxis()
for x in range(len(df['x'])):
    if df['outcome'][x] == 'Successful':
        plt.plot((df['x'][x], df['endX'][x]), (df['y'][x], df['endY'][x]), color='green')
        plt.scatter(df['x'][x], df['y'][x], color='green')
        plt.scatter(df['endX'][x], df['endY'][x], color='green')
    else:
        plt.plot((df['x'][x], df['endX'][x]), (df['y'][x], df['endY'][x]), color='red')
        plt.scatter(df['x'][x], df['y'][x], color='red')
        plt.scatter(df['endX'][x], df['endY'][x], color='red')
plt.title('Messi vs Real Betis', color='white', size=20)
plt.show()
