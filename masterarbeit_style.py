# plot_style.py
import matplotlib.pyplot as plt

def set_plot_style():
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12
    plt.rcParams['grid.linestyle'] = '-'
    plt.rcParams['grid.linewidth'] = 0.5
    plt.rcParams['grid.color'] = 'gray'

def plot_with_style(x, y, title, xlabel, ylabel):
    set_plot_style()
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='blue', linewidth=2)
    plt.title(title, color='darkred')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()