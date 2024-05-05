from manim import *
from math import sqrt

class Ciottoli(Scene):
    def construct(self):

        colors = [YELLOW, GREEN, TEAL, MAROON, ORANGE, PINK, GOLD, LIGHT_BROWN]
        n_triangoli_tutti = VGroup()
        n_quadrati_tutti = VGroup()

        colors_idx = 0
        n_triangoli_counts = [1, 3, 6, 10]
        for k in range(0, 4):
            n_triangoli = VGroup()
            for i in range(0, k + 1):
                layer = VGroup()
                for j in range(0, i + 1):
                    new_circ = Dot()
                    new_circ.set_fill(colors[colors_idx], opacity=1) 
                    layer.add(new_circ)

                layer.arrange_in_grid(rows=1, buff=.5)
                n_triangoli.add(layer)

            colors_idx += 1
            n_triangoli.arrange_in_grid(cols=1)
            n_triangoli_tutti.add(n_triangoli)

        n_triangoli_tutti.arrange_in_grid(rows=1, buff=1.5)

        first_row = VGroup(n_triangoli_tutti)
        for idx, triangolo in enumerate(n_triangoli_tutti):
            lbl = Integer(n_triangoli_counts[idx]).next_to(triangolo, UP, .5)
            first_row.add(lbl) 

        n_quadrati_counts = [1, 4, 9, 16]
        reference = None

        for i in [1, 4, 9, 16]:
            nquadrati = VGroup()
            for j in range(0, i):
                new_dot = Dot(color=colors[colors_idx])
                if i == 9 and j == 4:
                    reference = new_dot

                nquadrati.add(new_dot)
            
            colors_idx += 1
            nquadrati.arrange_in_grid(rows=int(sqrt(i)), cols=int(sqrt(i)), buff=.5)
            n_quadrati_tutti.add(nquadrati)

        n_quadrati_tutti.arrange_in_grid(rows=1, buff=1.5).move_to(ORIGIN)

        second_row = VGroup(n_quadrati_tutti)
        for idx, quad in enumerate(n_quadrati_tutti):
            lbl = Integer(n_quadrati_counts[idx]).next_to(quad, UP, .5)
            second_row.add(lbl)

        first_row.move_to(ORIGIN).shift(UP * 2 + LEFT * 1.2)
        second_row.move_to(ORIGIN).shift(DOWN + LEFT * 1.2)

        triangoli_lbl = Tex(r"Numeri\\triangolari").next_to(first_row, RIGHT, 1)
        first_row.add(triangoli_lbl)

        quadrati_lbl = Tex(r"Numeri\\quadrati").next_to(second_row, RIGHT, 1)
        second_row.add(quadrati_lbl)

        first_row.shift(UP * .65).scale(.9)
        second_row.shift(UP * .65).scale(.9)

        formula = MathTex(r"\frac{n(n+1)}{2} + \frac{(n+2)(n+1)}{2} = (n + 1)^2", substrings_to_isolate=[r"\frac{n(n+1)}{2}", r"\frac{(n+2)(n+1)}{2}", r"(n+1)^2"])
        formula.next_to(second_row, DOWN, .6)

        line = Line().rotate(45 * DEGREES).next_to(reference, UL).shift(DR * .875).set_color(PURE_RED)
        for obj in first_row:
            if isinstance(obj, Tex) or isinstance(obj, Integer):
                self.play(Write(obj))
            else:
                self.play(Create(obj), run_time=5)
            self.wait(1)

        for obj in second_row:
            if isinstance(obj, Tex) or isinstance(obj, Integer):
                self.play(Write(obj))
            else:
                self.play(Create(obj), run_time=5)
            self.wait(1)

        self.play(Create(line), run_time=4)
        self.play(n_quadrati_tutti[2][0].animate.set_color(GREEN), 
            n_quadrati_tutti[2][1].animate.set_color(GREEN), 
            n_quadrati_tutti[2][3].animate.set_color(GREEN))
        self.wait(1.5)
        self.play(
            n_quadrati_tutti[2][2].animate.set_color(TEAL), 
            n_quadrati_tutti[2][4].animate.set_color(TEAL), 
            n_quadrati_tutti[2][5].animate.set_color(TEAL),
            n_quadrati_tutti[2][6].animate.set_color(TEAL),
            n_quadrati_tutti[2][7].animate.set_color(TEAL),
            n_quadrati_tutti[2][8].animate.set_color(TEAL))
        self.wait(1.5)
        self.play(Write(formula), run_time=5)
        self.play(formula.animate.set_color_by_tex(r"\frac{n(n+1)}{2}", GREEN))
        self.play(formula.animate.set_color_by_tex(r"\frac{(n+2)(n+1)}{2}", TEAL))
        self.play(formula.animate.set_color_by_tex(r"(n+1)^2", GOLD))