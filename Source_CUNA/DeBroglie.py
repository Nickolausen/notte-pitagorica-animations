from manim import *

class DisplayFormula(Scene):
    def construct(self):
        title = Title("Lunghezza d'onda termica di De Broglie")
        formula = MathTex(r"\lambda = {h\over{mv}}", substrings_to_isolate=["h"]).scale(2)
        formula.set_color_by_tex("h", GREEN)

        constant = MathTex(r"h = 6.63 \times 10^{-34}").next_to(formula, DOWN, 1).set_color(GREEN)
        self.play(Write(title), Write(formula))
        self.wait(1)
        self.play(Write(constant))