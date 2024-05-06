from manim import *

class TipiNumeri(Scene):
    def construct(self):
        head_1 = Tex(r"\textsc{Numeri perfetti}").scale(1.5)
        num_perf = VGroup(
            MathTex("6").set_color(MAROON),
            MathTex("28"),
            MathTex("496").set_color(YELLOW)
        ).arrange_in_grid(rows=1, buff=3)
        head_1.shift(UP * 3)
        num_perf.next_to(head_1, DOWN, .5)

        divisori = MathTex(r"\textsc{Divisori}(28) = \{1,2,4,7,14\}", substrings_to_isolate=["28"]).next_to(num_perf[1], DOWN, 1.25)
        divisori.set_color_by_tex("28", GREEN)

        sum_divisori = MathTex(r"1+2+4+7+14 = ", "28", substrings_to_isolate=["28"]).next_to(divisori, DOWN, .5)
        sum_divisori.set_color_by_tex("28", GREEN)

        self.play(Write(head_1))
        for num in num_perf:
            self.play(Write(num), run_time=1.5)

        self.play(num_perf[1].animate.set_color(GREEN), Circumscribe(num_perf[1]))
        self.play(Write(divisori), run_time=3)
        self.play(Write(sum_divisori[0]))
        self.wait(1)
        self.play(Write(sum_divisori[1]), Flash(sum_divisori[1]))
        self.wait(3)

        self.play(
            divisori.animate.scale(.8),
            sum_divisori.animate.scale(.8)
        )

        self.play(divisori.animate.shift(UP * .7))
        self.play(sum_divisori.animate.next_to(divisori, DOWN, .35))

        head_2 = Tex(r"\textsc{Numeri amici}").scale(1.5).next_to(sum_divisori, DOWN, .75)
        self.play(Write(head_2))

        num_friends = VGroup(
            MathTex("220"),
            MathTex("284"),
        ).arrange_in_grid(rows=1, buff=5)
        num_friends.next_to(head_2, DOWN, .5)

        self.play(Write(num_friends[0]))
        self.play(Write(num_friends[1]))

        divisori_1 = MathTex("1,2,4,5,10,11,20,22,44,55,110")
        divisori_1.next_to(num_friends[0], DOWN, 1)
        divisori_2 = MathTex("1,2,4,71,142")
        divisori_2.next_to(num_friends[1], DOWN, 1)
        divisori_heading_1 = Tex(r"\textsc{Divisori}").scale(.6).next_to(divisori_1, UP)
        divisori_heading_2 = Tex(r"\textsc{Divisori}").scale(.6).next_to(divisori_2, UP)
        self.play(Write(divisori_heading_1))
        self.play(Write(divisori_1))
        self.play(Write(divisori_heading_2))
        self.play(Write(divisori_2))

        self.wait(1)
        self.play(divisori_1.animate.set_color(PINK), num_friends[1].animate.set_color(PINK), Flash(num_friends[1]))
        self.wait()
        self.play(divisori_2.animate.set_color(TEAL), num_friends[0].animate.set_color(TEAL), Flash(num_friends[0]))