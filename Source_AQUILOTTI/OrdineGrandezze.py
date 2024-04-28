from manim import *
import math

class OrdineGrandezze(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 12, 2],
            y_range=[0, 100, 20],
            axis_config={
                "tip_shape": StealthTip
            }
        ).add_coordinates()


        linear = ax.plot(lambda x: x, x_range=ax.x_range).set_color(RED)
        linear_label = ax.get_graph_label(linear, "f(x) = x").scale(.7).shift(UP * .6)
        
        quadratic = ax.plot(lambda x: x**2, x_range=ax.x_range).set_color(GREEN)
        quadratic_label = ax.get_graph_label(quadratic, "f(x) = x^2").scale(.7).shift(LEFT * .5)
        
        exponential = ax.plot(lambda x: np.exp2(x), x_range=ax.x_range).set_color(PURPLE)
        exponential_label = ax.get_graph_label(exponential, "f(x) = 2^x").scale(.7).shift(LEFT * .6)

        fact = ax.plot(lambda x: 10 * np.exp2(x) - 9, x_range=ax.x_range).set_color(MAROON)
        fact_label = ax.get_graph_label(fact, "f(x) = x!").scale(.7).shift(LEFT * .7)

        functions = VGroup(linear, quadratic, exponential, fact)
        labels = VGroup(linear_label, quadratic_label, exponential_label, fact_label)

        self.play(Create(ax))
        for idx, el in enumerate(functions):
            self.play(Create(functions[idx], rate_func=rate_functions.ease_in_expo), run_time=3)
            self.play(Write(labels[idx]))

        self.wait(10)
        self.play(FadeOut(*self.mobjects))
