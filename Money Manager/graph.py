import matplotlib.pyplot as plot
import numpy as np

plot.style.use("_mpl-gallery-nogrid")

x = [1,2,3,4]
colors = plot.get_cmap("Blues")(np.linspace(.2,.7,len(x)))

fig, ax = plot.subplots()
ax.pie(x, colors=colors, radius=3, center=(4,4), wedgeprops={"linewidth":1,"edgecolor":"white"}, frame=True)

ax.set(xlim = (0,8), xticks = np.arange(1,8),
       ylim = (0,8), yticks = np.arange(1,8))

plot.savefig("pie_chart.png")

plot.show()