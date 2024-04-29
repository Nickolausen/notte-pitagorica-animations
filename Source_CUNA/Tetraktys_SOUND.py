from manim import *
from random import randint

class Tetraktys_Sound(Scene):
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
            circles.get_left() + DOWN * 2).scale(1.5).shift(UP * .35).set_color(MAROON).set_stroke(opacity=.6, width=1.5)
        
        tetraktys = VGroup(circles, triangle).scale(1.1).shift(DOWN * .2)
        
        self.play(GrowFromCenter(tetraktys), run_time=7)
        self.wait(.7)
        self.play(ShowPassingFlash(triangle.copy(), time_width=1), run_time=.6)
        self.play(AnimationGroup(*[ApplyWave(circle) for circle in circles], run_time=5, lag_ratio=.5))
        self.wait(.7)
        self.play(FadeOut(circles))

        self.play(ShowPassingFlash(triangle.copy(), time_width=1), run_time=.6)
        
        for i in range(0, 20):
            outer_rnd_index = randint(0, 3)
            inner_rnd_index = randint(0, len([*circles[outer_rnd_index]]) - 1)
            
            # if (outer_rnd_index in outer_idxs and inner_rnd_index in inner_idxs):
            #     self.play(FadeOut(circles[outer_rnd_index][inner_rnd_index]), run_time=.1)
            #     outer_idxs.remove(outer_rnd_index)
            #     inner_idxs.remove(inner_rnd_index)
            # else:
            #     self.play(Create(circles[outer_rnd_index][inner_rnd_index]), run_time=.1)
            #     outer_idxs.append(outer_rnd_index)
            #     inner_idxs.append(inner_rnd_index)
            self.play(Create(circles[outer_rnd_index][inner_rnd_index]), run_time=.1)
            self.wait(.4)
            self.play(FadeOut(circles[outer_rnd_index][inner_rnd_index]), run_time=.1)
            self.wait(.4)

        self.wait(.4)
        for i in range(0, len([*circles])):
            for j in range(0, len([*circles[i]])):
                self.play(FadeIn(circles[i][j]), run_time=.3)

        self.play(ShowPassingFlash(triangle.copy(), time_width=1), run_time=.6)

        self.play(FadeOut(circles[3]), run_time=.3)
        for i in range(0, 27):
            self.play(FadeIn(circles[3][i % 4]), run_time=.15)
            self.wait(.3)
            self.play(FadeOut(circles[3][i % 4]), run_time=.15)

        self.play(ShowPassingFlash(triangle.copy(), time_width=1), run_time=.6)

        self.play(FadeOut(circles[2]), run_time=.3)
        for i in range(0, 20):
            self.play(FadeIn(circles[2][i % 3]), run_time=.15)
            self.wait(.3)
            self.play(FadeOut(circles[2][i % 3]), run_time=.15)

        self.play(ShowPassingFlash(triangle.copy(), time_width=1), run_time=.6)

        self.play(FadeOut(circles[1]), run_time=.3)
        for i in range(0, 15):
            self.play(FadeIn(circles[1][i % 2]), run_time=.15)
            self.wait(.3)
            self.play(FadeOut(circles[1][i % 2]), run_time=.15)

        self.play(FadeOut(circles[0]), run_time=.3)
        for i in range(0, 9):
            self.play(FadeIn(circles[0][i % 1]), run_time=.15)
            self.wait(.3)
            self.play(FadeOut(circles[0][i % 1]), run_time=.15)

        self.play(ShowPassingFlash(triangle.copy(), time_width=1), run_time=.6)

        for i in range(0, 20):
            self.play(FadeIn(circles[2][i % 3]), FadeIn(circles[0][i % 1]), run_time=.15)
            self.wait(.3)
            self.play(FadeOut(circles[2][i % 3]), FadeOut(circles[0][i % 1]), run_time=.15)

        self.play(ShowPassingFlash(triangle.copy(), time_width=1), run_time=.6)

        for i in range(0, 20):
            self.play(FadeIn(circles[3][i % 4]), FadeIn(circles[1][i % 2]), run_time=.15)
            self.wait(.3)
            self.play(FadeOut(circles[3][i % 4]), FadeOut(circles[1][i % 2]), run_time=.15)

        self.wait(.4)
        for i in range(0, 4):
            for j in range(0, len([*circles[i]])):
                self.play(Create(circles[i][j]))

        self.play(Wiggle(tetraktys))
        self.wait(1)
        self.play(FadeOut(*self.mobjects), run_time=1)