import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.collections import PatchCollection


class Visualizer:

    def __init__(self, array_polygons, x_lim, y_lim, title):
        self.__array_polygons = array_polygons
        self.__x_lim = x_lim
        self.__y_lim = y_lim
        self.__title = title
        self.__fig = plt.figure()
        self.__ax = plt.subplot()

    def plot_polygons(self):
        colors = 100 * np.random.rand(len(self.__array_polygons))
        p = PatchCollection(self.__array_polygons, alpha=0.4)
        p.set_array(np.array(colors))
        self.__ax.set_xlim((0, self.__x_lim))
        self.__ax.set_ylim((0, self.__y_lim))
        self.__ax.set_title(self.__title)
        self.__ax.add_collection(p)
        plt.show()

    def init(self):
        self.__ax.set_title(self.__title)
        self.__ax.set_xlim(self.__x_lim)
        self.__ax.set_ylim(self.__y_lim)

    def update(self, frame):
        colors = 100 * np.random.rand(len(self.__array_polygons))
        p = PatchCollection([self.__array_polygons[frame]], alpha=0.4)
        p.set_array(np.array(colors))
        self.__ax.add_collection(p)
        return

    def plot_animation(self):
        ani = animation.FuncAnimation(self.__fig,
                                      self.update,
                                      interval=500,
                                      frames=len(self.__array_polygons),
                                      init_func=self.init,
                                      repeat=False)
        plt.show()
