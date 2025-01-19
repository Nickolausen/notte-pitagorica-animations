from manim import *

class AdjustParams(Scene):
    def construct(self):
        formula = MathTex(r"w_i = w_i - lrate\times\frac{df}{dw_i}").scale(1.5)
        self.add(formula)