from matplotlib.widgets import TextBox, Button
import seaborn as sns
import matplotlib.pyplot as plt
from solver import solve

sns.set_theme(style = "whitegrid")

fig, ax = plt.subplots(figsize = (10, 6))
plt.subplots_adjust(bottom = 0.25)
fig.canvas.manager.set_window_title('Electromagnetic potential FEM')
ax.set_title('Electromagnetic potential FEM', fontsize = 16, fontweight = 'bold', pad = 10)
fig.subplots_adjust(top = 0.85)

ax_box = plt.axes([0.45, 0.1, 0.1, 0.05])
text_box = TextBox(ax_box, 'Number of points: ', initial = '10')
text_box.label.set_fontsize(14)

ax_button = plt.axes([0.65, 0.1, 0.1, 0.05])
button = Button(ax_button, 'Draw')
button.label.set_fontsize(14)

def on_button_clicked(event):
    n = int(text_box.text)
    ax.clear()
    points = solve(n)
    x, y = zip(*points)
    sns.lineplot(x = x, y = y, ax = ax, label='Solution')
    ax.set_xlabel('x', fontsize = 14)
    ax.set_ylabel('y', fontsize = 14)
    ax.set_title(f'Electromagnetic potential FEM\nPlot for {n} points', fontsize = 16, fontweight = 'bold', pad = 20)
    ax.legend()
    fig.canvas.draw_idle()

button.on_clicked(on_button_clicked)
plt.show()