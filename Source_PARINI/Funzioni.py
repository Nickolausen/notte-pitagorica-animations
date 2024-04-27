from manim import *
# TO DO: Logarithmic Scale

class Funzioni(Scene):
    def construct(self):
        func_1 = lambda x: (1 + x)*(1 - .1 * np.log(.1 * x))
        func_2 = lambda x: (1 + x)*(1 - .11 * np.log(1 + .1 * x))
        func_3 = lambda x: (1 + x)*(1 - .119 * np.log(1 + .1 * x))

        ax = Axes(
            x_axis_config={
                "scaling": LogBase()
            },
            y_axis_config={
                "scaling": LogBase()
            }
        )

        f1 = ParametricFunction(func_1, t_range=[.1]).set_color(RED)
        f2 = ParametricFunction(func_2, discontinuities=[-10]).set_color(GREEN)
        f3 = ParametricFunction(func_3, discontinuities=[-10]).set_color(BLUE)

        self.add(ax, f1, f2, f3)