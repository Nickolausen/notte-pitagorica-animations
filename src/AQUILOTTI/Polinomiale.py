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

        nsquared = ax.plot(lambda x: x**2).set_color(PINK)
        nsquared_lbl = ax.get_graph_label(nsquared, "f(n) = n^2")

        nsquareroot = ax.plot(lambda x: x**.5).set_color(YELLOW)
        nsquareroot_lbl = ax.get_graph_label(nsquareroot, r"f(n) = \sqrt{n}").shift(UP * .5)

        ncube = ax.plot(lambda x: x**3).set_color(ORANGE)
        ncube_lbl = ax.get_graph_label(ncube, r"f(n) = n^3").shift(LEFT * 2.7 + DOWN)

        self.add(
            ax, 
            n, 
            n_lbl, 
            nlogn, 
            nlogn_lbl,
            nsquared,
            nsquared_lbl,
            nsquareroot,
            nsquareroot_lbl,
            ncube,
            ncube_lbl,
            ax_lbl)