from manim import *

class Gradiente(Scene):
    def construct(self):
        formula = MathTex(r"\nabla C(w) = \left({\frac{dC}{dw_1}},{\frac{dC}{dw_2}},\dots,\frac{dC}{w_n}\right)").scale(1.5)
        self.add(formula)