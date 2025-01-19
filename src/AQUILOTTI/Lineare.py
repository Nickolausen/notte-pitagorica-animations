from manim import *

class Lineare(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0.0001, 10],
            y_range=[0, 10]
        ).add_coordinates()

        ax_lbl = ax.get_axis_labels(
            "n", "y"
        )

        n = ax.plot(lambda x: x).set_color(GREEN)
        n_lbl = ax.get_graph_label(n, "f(n) = n").shift(DL + DOWN * .7)

        nlogn = ax.plot(lambda x: x * np.log(x)).set_color(BLUE)
        nlogn_lbl = ax.get_graph_label(nlogn, "f(n) = n\cdot\log(n)").shift(LEFT * .4)

        self.add(ax, n, n_lbl, nlogn, nlogn_lbl, ax_lbl)