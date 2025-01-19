from manim import *

class OndaBrutta(Scene):
    def construct(self):

        ax = Axes(
            x_range=[0.1, 160],
            y_range=[-50, 50],
            axis_config={
                "tip_shape": StealthTip,
                "include_ticks": False  
            },
        )

        onda = ax.plot(lambda x: 20*np.cos(1000/x) * np.cos(10*x)).set_color(BLUE)

        self.play(Create(ax))
        self.play(Create(onda, rate_func = rate_functions.rush_into))