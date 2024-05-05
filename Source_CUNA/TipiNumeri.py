from manim import *

class TipiNumeri(Scene):
    def construct(self):
        head_1 = Tex(r"\textsc{Numeri perfetti}").scale(1.5)
        num_perf = VGroup(
            MathTex("6"),
            MathTex("28"),
            MathTex("496")
        ).arrange_in_grid(rows=1, buff=3)
        head_1.shift(UP * 3)
        num_perf.next_to(head_1, DOWN, .5)

        divisori = MathTex(r"\textsc{Divisori}(28) = \{1,2,4,7,14\}").next_to(num_perf[1], DOWN, 2)
        arr = Arrow(start=num_perf[1], end=divisori)
        sum_divisori = MathTex(r"1+2+4+7+14 = 28").next_to(divisori, DOWN, .5)
        self.add(head_1, num_perf, divisori, sum_divisori, arr)