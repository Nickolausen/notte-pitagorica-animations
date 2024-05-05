from manim import *
from random import randint

class Tetraktys_Sound(Scene):
    def construct(self):
        colors = [MAROON, GREEN, TEAL, ORANGE]
        circles = VGroup()
        
        def flash_triangle():
            self.play(ShowPassingFlash(triangle.copy(), time_width=1), run_time=2)

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
            circles.get_left() + DOWN * 2).scale(1.35).shift(UP * .35).set_color(MAROON).set_stroke(opacity=.6, width=1.5)
        
        tetraktys = VGroup(circles, triangle).scale(1.1).shift(DOWN * .2)
        
        self.play(GrowFromCenter(tetraktys), run_time=7)
        self.wait(.7)
        flash_triangle()
        self.play(AnimationGroup(*[ApplyWave(circle) for circle in circles], lag_ratio=.5))
        self.wait(.7)
        self.play(FadeOut(circles))

        flash_triangle()
        
        for i in range(0, 40):
            outer_rnd_index = randint(0, 3)
            inner_rnd_index = randint(0, len([*circles[outer_rnd_index]]) - 1)

            triangle.save_state()
            self.play(FadeIn(circles[outer_rnd_index][inner_rnd_index]), triangle.animate.scale(1.15), run_time=.1)
            self.wait(.4)
            self.play(FadeOut(circles[outer_rnd_index][inner_rnd_index]), triangle.animate.restore(),  run_time=.1)
            self.wait(.4)

        flash_triangle()
        self.wait(1)
        for i in [0, 1, 2, 3]:
            for j in range(0, len([*circles[i]])):
                self.play(FadeIn(circles[i][j]))

        self.play(Wiggle(tetraktys))
        self.wait(1)
        self.play(FadeOut(*self.mobjects), run_time=1)