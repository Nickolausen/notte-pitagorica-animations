from manim import *

class Tetraktys(Scene):
    def construct(self):
        colors = [MAROON, GREEN, TEAL, ORANGE]
        circles = VGroup()
        
        for i in range(0, 4):
            layer = VGroup()
            for j in range(0, i + 1):
                new_circ = Circle(color=colors[i])
                new_circ.set_fill(colors[i], opacity=1) 
                layer.add(new_circ)

            layer.arrange_in_grid(rows=1, buff=1)
            circles.add(layer)

        circles.arrange_in_grid(cols=1).move_to(ORIGIN).scale(.5)
        
        triangle = Polygon(
            circles.get_top(), 
            circles.get_right() + DOWN * 2, 
            circles.get_left() + DOWN * 2).scale(1.5).shift(UP * .35).set_color(MAROON)
        
        tetraktys = VGroup(circles, triangle).scale(.8)
        
        left_nrs = VGroup()
        for i in range(1, 5):
            left_nrs.add(Integer(i))
        left_nrs.arrange_in_grid(cols=1).next_to(tetraktys, LEFT, 1.2).scale_to_fit_height(circles.height).shift(DOWN * .25 + LEFT * .4).scale(.9)
        
        total_line = Line(LEFT, RIGHT)
        total = Integer(10).next_to(total_line, DOWN, .4).scale(1.5)
        tot_group = VGroup(total_line, total).next_to(left_nrs, DOWN, .7)
        
        right_txts = VGroup(Tex(r"\textsc{Punto}"), Tex(r"\textsc{Linea}"), Tex(r"\textsc{Piano}"), Tex(r"\textsc{Spazio}"))
        right_txts.arrange_in_grid(cols=1, buff=.4).next_to(tetraktys, RIGHT, 1.1).scale(1.2).shift(DOWN * .3)
        everything = VGroup(tetraktys, left_nrs, tot_group, right_txts).shift(UP * .6).scale(.8)

        title = Tex(r"\textsc{Tetraktys}").set_color(GREEN).scale(2.4)
        title.next_to(tetraktys, DOWN, 1)
        
        for i in range(0, 4):
            self.play(AnimationGroup(*[DrawBorderThenFill(circle) for circle in circles[i]], lag_ratio=.7))
            self.wait(.2)
            self.play(Write(left_nrs[i]))
            self.wait(.2)
            self.play(Write(right_txts[i]))

        self.play(Create(triangle), run_time=2)
        self.play(Create(total_line))
        self.wait(1)
        self.play(Write(total))
        self.wait(4)

        self.play(everything.animate.shift(UP * .4))
        self.wait(2)
        self.play(FadeIn(title))