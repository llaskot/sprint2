import os
import time
import matplotlib
import flet as ft

matplotlib.use('Agg')
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, name, data=None):
        self.numeric_name = None
        self.analytic_name = None
        self.numeric = None
        self.analytics = None
        self.img = None
        if data is None:
            data = {'func': '-xy', 'x': [0.0, 1.0, 2.0],
                    'y Euler': [2.0, 1.8, 0.0],
                    'y Runge-Kutta 2': [2.0, 1.6, 0.0],
                    'y Runge-Kutta 3': [2.0, 1.4, 0.0],
                    'y Runge-Kutta 4': [2.0, 1.2, 0.0]}
        self.data = data
        self.graph_name = name
        self.dir_path = self.build_dir_path()
        self.save_path = None
        self.img = ft.Container(
            content=ft.Image(
                src=self.save_path,
                fit=ft.ImageFit.CONTAIN,
                expand=True
            ))

    def set_img(self):
        self.img.content = None
        self.img.content = ft.Image(
            src=self.save_path,
            fit=ft.ImageFit.CONTAIN,
            expand=True
        )
        self.img.update()

    def set_data(self, data: dict, name='f(x,y)'):
        self.graph_name = name
        self.img.content = None
        self.data = data

    def build_path(self):
        self.save_path = os.path.join(self.dir_path, f"graph_{int(time.time())}.png")

    def build_dir_path(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
        return os.path.join(project_root, "ui", "graph")

    def build_graph(self):
        plt.figure(facecolor='black', figsize=(20.05, 12))
        ax = plt.gca()
        ax.set_facecolor('black')
        ax.tick_params(colors='white', labelsize=18)
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        ax.xaxis.label.set_size(18)
        ax.yaxis.label.set_size(18)

        # print(self.data['x'])
        plt.plot(
            self.data['x'],
            self.data["y Euler"],
            label=f'Euler',
            color='#1f77b4',
            marker='o',
            linewidth=10,  # толщина линии
            markersize=20  # размер точек
        )

        plt.plot(
            self.data['x'],
            self.data['y Runge-Kutta 2'],
            label=f'Runge-Kutta 2',
            color='red',
            marker='o',
            linewidth=7,  # толщина линии
            markersize=15  # размер точек
        )

        plt.plot(
            self.data['x'],
            self.data['y Runge-Kutta 3'],
            label=f'Runge-Kutta 3',
            color='white',
            marker='o',
            linewidth=4,  # толщина линии
            markersize=10  # размер точек
        )

        plt.plot(
            self.data['x'],
            self.data['y Runge-Kutta 4'],
            label=f'Runge-Kutta 4',
            color='green',
            marker='o',
            linewidth=1.5,  # толщина линии
            markersize=5  # размер точек
        )

        # for xi, yi in zip(self.x, self.y):
        #     plt.axvline(x=xi, color='blue', linestyle='--', linewidth=0.5)
        #     plt.axhline(y=yi, color='blue', linestyle='--', linewidth=0.5)  # проекции на оси

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(self.graph_name)
        ax.title.set_size(30)
        plt.legend()
        plt.legend(fontsize=18)
        plt.grid(True)
        # plt.show()
        for file in os.listdir(self.dir_path):
            if file.endswith(".png"):
                self.img.content = None
                os.remove(os.path.join(self.dir_path, file))
        self.build_path()
        plt.savefig(self.save_path, dpi=300, bbox_inches='tight')
        plt.close()
