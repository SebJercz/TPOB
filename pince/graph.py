import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib
import numpy as np

x = [1.5, 2.0, 3.6, 4.1]
y = [3.4, 7.7, 26, 40]

# SKIIIIIIIA . boum
majorLocator1 = MultipleLocator(1)                       #gros intervalle axe x
majorFormatter1 = FormatStrFormatter('%d')
minorLocator1 = MultipleLocator(0.5)                       #petit intervalle axe x
majorLocator2 = MultipleLocator(10)                      # gros intervalle axe y
majorFormatter2 = FormatStrFormatter('%.1f')
minorLocator2 = MultipleLocator(5)                       #petit intervalle axe y


#reflexion = plt.plot(x, y, 'k--', marker="s", label = 'Résolution en y')
transmission = plt.plot(x, y, 'k', marker="o", markersize=6, markeredgewidth=1, markeredgecolor='k', markerfacecolor='k', label = 'Résolution en x')

plt.gca().xaxis.set_major_locator(majorLocator1)
plt.gca().tick_params(axis='both', labelsize = 14)    #tick size
plt.gca().xaxis.set_major_formatter(majorFormatter1)
plt.gca().xaxis.set_minor_locator(minorLocator1)
plt.gca().yaxis.set_major_locator(majorLocator2)
plt.gca().yaxis.set_major_formatter(majorFormatter2)
plt.gca().yaxis.set_minor_locator(minorLocator2)

plt.axis([1, 4.4, 0, 53])
plt.xlabel(r'Puissance du laser infrarouge [W]', fontsize=14)                        #nom axe x, font size
plt.ylabel(r'Constante de trappe $k_t$   [$\times 10^{-6}$]', fontsize=14)                              #nom axe y, font size
plt.rc('legend', fontsize=12)    # legend fontsize

#plt.legend(bbox_to_anchor=(0.4, 0.94), loc=2, borderaxespad=0., frameon=False)               #pos legende
plt.errorbar(x, y, xerr=[0.01, 0.01, 0.02, 0.03], yerr=[0.2, 1, 4, 8], fmt='ko', markersize=3, ecolor='k', capsize=6,)
#plt.errorbar(x, y, xerr=0.5, yerr=2, fmt='wo', markersize=4, ecolor='k', capsize=2,)
#plt.axhline(y=edge1, color='r', linestyle='-')
#plt.axhline(y=edge9, color='r', linestyle='-')
plt.savefig("fig1.png", dpi=700)
plt.tight_layout()
plt.show()


