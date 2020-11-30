import File

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches
from matplotlib import animation
from matplotlib.collections import PatchCollection
import os
import sys


def create_polygons_to_plot(polygons):
    polygons_object = []
    for polygon in polygons:
        polygons_object.append(matplotlib.patches.Polygon(np.array(polygon), True))
    return polygons_object


class Visualizer:

    def __init__(self, array_polygons, x_lim, y_lim, title):
        self.__array_polygons = create_polygons_to_plot(array_polygons)
        self.__x_lim = x_lim
        self.__y_lim = y_lim
        self.__title = title
        self.__fig = plt.figure(figsize=(10, 10))
        self.__ax = plt.subplot(aspect='equal')  # aspect='equal'

    def plot_polygons(self):
        colors = 100 * np.random.rand(len(self.__array_polygons))
        p = PatchCollection(self.__array_polygons, alpha=.5)
        p.set_array(np.array(colors))
        p.set_edgecolor([0, 0, 0])
        self.__ax.set_xlim((0, self.__x_lim))
        self.__ax.set_ylim((0, self.__y_lim))
        self.__ax.set_title(self.__title)
        self.__ax.add_collection(p)
        plt.show()

    def init(self):
        self.__ax.set_title(self.__title)
        plt.ylim(0, self.__y_lim)
        plt.xlim(0, self.__x_lim)

    def update(self, frame):
        color = (0, 0, 0)
        p = PatchCollection([self.__array_polygons[frame]], alpha=.5)
        p.set_color(color)
        p.set_edgecolor([0, 0, 0])
        self.__ax.add_collection(p)
        return

    def plot_animation(self):
        ani = animation.FuncAnimation(self.__fig,
                                      self.update,
                                      interval=300,
                                      frames=len(self.__array_polygons),
                                      init_func=self.init,
                                      repeat=False)
        plt.show()
        return ani

    def save_fig(self, name_image, directory):
        p = PatchCollection(self.__array_polygons, alpha=.5)
        p.set_facecolor([0, 0, 0])
        p.set_edgecolor([0, 0, 0])
        self.__ax.set_xlim((0, self.__x_lim))
        self.__ax.set_ylim((0, self.__y_lim))
        self.__ax.set_title(self.__title)
        self.__ax.add_collection(p)
        plt.title(self.__title)
        plt.plot()
        # plt.savefig('../Results/Images/' + name_image + ".svg")
        plt.savefig(directory + name_image + ".svg")


def main():
    polygons, limit_x, y_result, instance, time = File.polygons_from_txt_result("Visualizer_Module/polygons.txt")
    visualizer = Visualizer(polygons, limit_x, y_result, instance + " FO: " + str(y_result) + "  Time: " + str(time))
    visualizer.save_fig(instance, "Results/")
    # visualizer.plot_animation()
    os.system("rm Visualizer_Module/polygons.txt")


def main_for_tests():
    if len(sys.argv) == 4:
        heuristic = sys.argv[1]
        sort_function = sys.argv[2]
        rotate_function = sys.argv[3]
        title = "\n" + heuristic + " " + sort_function + " " + rotate_function
        polygons, limit_x, y_result, instance, time = File.polygons_from_txt_result("Visualizer_Module/polygons.txt")
        visualizer = Visualizer(
            polygons, limit_x, y_result, instance + " FO: " + str(y_result) + "  Time: " + str(time) + title)
        visualizer.save_fig(instance + "_" + sort_function + "_" + rotate_function, "Results/" + heuristic + "/")
        # visualizer.plot_animation()
        os.system("rm Visualizer_Module/polygons.txt")

    if len(sys.argv) == 3:
        heuristic = sys.argv[1]
        sort_function = sys.argv[2]
        title = "\n" + heuristic + " " + sort_function
        polygons, limit_x, y_result, instance, time = File.polygons_from_txt_result("Visualizer_Module/polygons.txt")
        visualizer = Visualizer(
            polygons, limit_x, y_result, instance + " FO: " + str(y_result) + "  Time: " + str(time) + title)
        visualizer.save_fig(instance + "_" + sort_function, "Results/" + heuristic + "/")
        # visualizer.plot_animation()
        os.system("rm Visualizer_Module/polygons.txt")


if __name__ == '__main__':
    # main()
    main_for_tests()
