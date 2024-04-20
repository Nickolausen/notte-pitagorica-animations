from manim import *
from _General import *

class FunctionSum(Scene):
    def construct(self):
        A = ValueTracker(0)
        omega = ValueTracker(0)
        alpha = ValueTracker(0)

        ax = Axes(
            x_range=[-4, 4],
            y_range=[-5, 5],
            axis_config={
                "include_numbers": True})

        def draw_sen_values_label():
            label = MathTex(f"y = {A.get_value()}\sin({omega.get_value()}x + {alpha.get_value()})", substrings_to_isolate=[f"{A.get_value()}", f"{omega.get_value()}", f"{alpha.get_value()}"])
            return label
        
        sin = always_redraw(lambda: ax.plot(lambda x: A.get_value() * np.sin(omega.get_value() * x + alpha.get_value()), color=RED))
        cos = always_redraw(lambda: ax.plot(lambda x: A.get_value() * np.cos(omega.get_value() * x + alpha.get_value()), color=GREEN))

        fsum = always_redraw(lambda: ax.plot(lambda x: A.get_value() * 
            (np.sin(omega.get_value() * x + alpha.get_value()) + np.cos(omega.get_value() * x + alpha.get_value())), color=BLUE))
        
        sen_values_label = always_redraw(lambda: draw_sen_values_label().move_to(ax.get_origin()).shift(UP * 2 + LEFT * 2.5))

        functions = VGroup(ax, sin, cos, fsum)
        functions.scale(.75)

        self.play(AnimationGroup(
            Create(ax),
            Create(sin),
            Create(cos),
            Create(fsum),
            Write(sen_values_label)
        ))

        for i in [1, 2]:
            self.play(A.animate.set_value(i ** 2))
            self.play(omega.animate.set_value(i * 2))
            self.play(alpha.animate.set_value(i / 2))
            self.wait(.3)

        for i in [-1, -2]:
            self.play(A.animate.set_value(i ** 2))
            self.play(omega.animate.set_value(i * 2))
            self.play(alpha.animate.set_value(i / 2))
            self.wait(.3)