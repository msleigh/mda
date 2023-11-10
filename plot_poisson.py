#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

count = np.arange(70, 130, 0.1)
PDF = np.exp(-100) * np.power(100, count) / factorial(count)

plt.plot(count, PDF, ".")
plt.xlabel("counts")
plt.ylabel("P(counts)")
plt.title("Poisson distribution for a sample in an ideal detector")
plt.annotate("$\mu_S = 100$", (110.0, 1.0 / 30.0))
plt.savefig("poisson.png")

# Background
bg = 50.0
sig0 = np.sqrt(bg)

# Gross - set this to the background plus the MDA
k1 = 1.645
k2 = 1.645

a = 1
b = -(2 * k1 * sig0 + k2 * k2)
c = (k1 * k1 - k2 * k2) * sig0 * sig0

mda = (-b + np.sqrt(b * b - 4 * a * c)) / (2 * a)
gr = bg + mda

print(mda)
print(bg + 1.645 * np.sqrt(bg))
print(gr - 1.645 * np.sqrt(gr))

count = np.arange(30, 100, 0.1)
bgPDF = np.exp(-bg) * np.power(bg, count) / factorial(count)
grPDF = np.exp(-gr) * np.power(gr, count) / factorial(count)

plt.clf()
plt.plot(count, bgPDF, ".", label="Background ($\mu_B = 50$)")
plt.plot(count, grPDF, ".", label="Gross ($\mu_G = 76$)", color="Orange")
plt.legend()
plt.xlabel("counts")
plt.ylabel("P(counts)")
plt.title("Poisson distribution of a sample in a real detector")
plt.savefig("poisson_background_gross.png")

LDb = bg + 1.645 * np.sqrt(bg)

plt.clf()
plt.plot(count, bgPDF, ".", label="Background ($\mu_B = 50$)")
plt.axvline(x=LDb, color="black", linestyle="--", linewidth=0.75)
plt.legend()
plt.xlabel("counts")
plt.ylabel("P(counts)")
plt.annotate("$L_D$", (1.01 * LDb, 1.0 / 30.0))
plt.annotate(
    "$\\alpha$",
    xy=(64.0, 0.002),
    xytext=(70.0, 0.02),
    textcoords="data",
    arrowprops=dict(facecolor="black", arrowstyle="->", connectionstyle="arc3"),
    horizontalalignment="right",
    verticalalignment="top",
)
plt.annotate(
    "$1-\\alpha$",
    xy=(50.0, 0.02),
    xytext=(36.0, 0.02),
    textcoords="data",
    arrowprops=dict(facecolor="black", arrowstyle="->", connectionstyle="arc3"),
    horizontalalignment="right",
    verticalalignment="top",
)
plt.title("Detection threshold for a detector")
plt.savefig("poisson_detection_thresh.png")

LDg = gr - 1.645 * np.sqrt(gr)

plt.clf()
plt.plot(count, grPDF, ".", label="Gross ($\mu_G = 76$)", color="orange")
plt.axvline(x=LDg, color="red", linestyle="-.", linewidth=0.5)
plt.legend()
plt.xlabel("counts")
plt.ylabel("P(counts)")
plt.annotate("$L_D$", (1.01 * LDg, 1.0 / 30.0))
plt.annotate(
    "$\\beta$",
    xy=(59, 0.002),
    xytext=(52.0, 0.02),
    textcoords="data",
    arrowprops=dict(facecolor="black", arrowstyle="->", connectionstyle="arc3"),
    horizontalalignment="right",
    verticalalignment="top",
)
plt.annotate(
    "$1-\\beta$",
    xy=(76.0, 0.02),
    xytext=(100.0, 0.02),
    textcoords="data",
    arrowprops=dict(facecolor="black", arrowstyle="->", connectionstyle="arc3"),
    horizontalalignment="right",
    verticalalignment="top",
)
plt.title("Detection threshold for a detector")
plt.savefig("poisson_detection_sample.png")

plt.clf()
plt.plot(count, bgPDF, ".", label="Background ($\mu_B = 50$)")
plt.plot(count, grPDF, ".", label="Gross ($\mu_G = 76$)", color="Orange")
plt.axvline(x=LDb, color="black", linestyle="--", linewidth=0.75)
plt.axvline(x=LDg, color="red", linestyle="-.", linewidth=0.5)
plt.annotate("$L_D$", (1.01 * LDg, 1.0 / 30.0))
plt.legend()
plt.xlabel("counts")
plt.ylabel("P(counts)")
plt.title("Poisson distribution of a sample in a detector")
plt.savefig("poisson_final.png")
