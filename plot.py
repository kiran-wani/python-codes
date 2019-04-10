from pylab import *

x = np.linspace(-np.pi, np.pi, 256)
y = []
for i in range(0, 7):
 y += [np.cos(x + i)]
fig,ax=subplots()
plot(x, y[0], color='red', linewidth=2.5, linestyle='-', label='linestyle="_"')
plot(x, y[1], color='blue', linewidth=5, alpha=0.5, linestyle='-', label='lines tyle="-"')
plot(x, y[2], color='#aa0000', linewidth=1, linestyle='--', label='linestyle="--"')
plot(x, y[3], color='black', linestyle=':', label='linestyle=":"')
plot(x, y[4], color='black', linewidth=2, linestyle='-.', label='linestyle="-."')

ax.tick_params(axis="y",direction="in", pad=10)
ax.tick_params(axis="x",direction="in", pad=10)
show()
